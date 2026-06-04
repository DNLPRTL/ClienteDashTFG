From Theory to Practice: Improving Bitrate Adaptation
in the DASH Reference Player
KEVINSPITERI,UniversityofMassachusetts,Amherst
RAMESHSITARAMAN,UniversityofMassachusetts,Amherst&AkamaiTechnologies
DANIELSPARACIO,CBSInteractive
Modernvideostreamingusesadaptivebitrate(ABR)algorithmsthatruninsidevideoplayersandcontinu-
allyadjustthequality(i.e.,bitrate)ofthevideosegmentsthataredownloadedandrenderedtotheuser.To
maximizethequality-of-experience(QoE)oftheuser,ABRalgorithmsmuststreamatahighbitratewithlow
rebufferingandlowbitrateoscillations.Further,agoodABRalgorithmisresponsivetouserandnetwork
eventsandcanbeusedindemandingscenariossuchaslow-latencylivestreaming.Recentresearchpapers
provideanabundanceofABRalgorithmsbutfallshortonmanyoftheabovereal-worldrequirements.
WedevelopSabre,anopen-sourcepubliclyavailablesimulationtoolthatenablesfastandaccuratesimula-
tionofadaptivestreamingenvironments.WeempiricallyvalidatedSabretoshowthatitaccuratelysimulates
real-worldenvironments.WeusedSabretodesignandevaluateBOLA-EandDYNAMIC,twonovelABRalgo-
rithms.WealsodevelopedaFAST SWITCHINGalgorithmthatcanreplacesegmentsthathavealreadybeen
downloadedwithhigher-bitrate(thus,higher-quality)segments.ThenewalgorithmsprovidehigherQoEto
theuserintermsofhigherbitrate,fewerrebuffers,andlesserbitrateoscillations.Inaddition,thesealgorithms 67
reactfastertousereventssuchasstartupandseek,andtheyrespondmorequicklytonetworkeventssuchas
improvementsinthroughput.Further,theyperformverywellforlivestreamsthatrequirelowlatency,achal-
lengingscenarioforABRalgorithms.Overall,ouralgorithmsoffersuperiorvideoQoEandresponsiveness
forreal-lifeadaptivevideostreaming,incomparisontothestate-of-the-art.Importantly,allthreealgorithms
presentedinthisarticlearenowpartoftheofficialDASHreferenceplayerdash.jsandarebeingusedbyvideo
providersinproductionenvironments.WhileourevaluationandimplementationarefocusedontheDASH
environment,ouralgorithmsareequallyapplicabletootheradaptivestreamingformatssuchasAppleHLS.
CCSConcepts:•Informationsystems→Multimediastreaming;
AdditionalKeyWordsandPhrases:Videostreaming,videoQoE,bitrateadaptation
ApreliminaryversionofthisarticleappearedinACMMultimediaSystemsConference,2018[21].
ThisworkwasperformedwhenDanielSparaciowasatAkamaiTechnologies.
ThisworkissupportedinpartbytheNSFunderGrantsNo.CNS-1413998andNo.CNS-1763617.
Authors’ addresses: K. Spiteri, College of Information and Computer Sciences, University of Massachusetts Amherst,
ComputerScienceBuilding,140GovernorsDrive,Amherst,MA01003,USA;email:kspiteri@cs.umass.edu;R.Sitaraman,
CollegeofInformationandComputerSciences,UniversityofMassachusettsAmherst,ComputerScienceBuilding,140
GovernorsDrive,Amherst,MA01003,USA&AkamaiTechnologies,150Broadway,Cambridge,MA02142,USA;email:
ramesh@cs.umass.edu; D. Sparacio, CBS Interactive, 235 Second Street, San Francisco, CA 94105, USA; email: daniel.
sparacio@cbsinteractive.com.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfee
providedthatcopiesarenotmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeand
thefullcitationonthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthantheauthor(s)mustbe
honored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,topostonserversortoredistributetolists,
requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2019Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
1551-6857/2019/07-ART67$15.00
https://doi.org/10.1145/3336497
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:2 K.Spiterietal.
ACMReferenceformat:
Kevin Spiteri, Ramesh Sitaraman, and Daniel Sparacio. 2019. From Theory to Practice: Improving Bitrate
AdaptationintheDASHReferencePlayer.ACMTrans.MultimediaComput.Commun.Appl.15,2s,Article67
(July2019),29pages.
https://doi.org/10.1145/3336497
1 INTRODUCTION
OnlinevideoviewershipisgrowingatarapidpaceandvideotrafficnowdominatestheInternet.
Videos accounted for 75% of all Internet traffic (both business and consumer) in 2017 and that
share is predicted to increase to 82% by 2022 [3]. The rapid increase in online video viewership
hasresultedinamajorriseinthediversityofuserswhowatchvideos.Usersuseawiderangeof
devicestowatchvideos,includingInternet-enabledtelevisions,desktops,tablets,andcellphones.
Further, they are connected to the Internet with widely different data rates. Such connections
includemultiplegenerationsofcellulartechnology,WiFi,cable,DSL,andfiber-to-the-home.
Video providers are equally diverse and include movie sites (such as Hulu and Netflix), news
portals (such as CNN and BBC), social networks (such as Facebook), and live sports channels
(suchasESPNandMLB).Thequalityofexperience(QoE)ofuserswhowatchvideosisacentral
concernforvideoproviders.Recentresearch[7,15]hasunderscoredtheimpactofpoorvideoQoE
onusers.Itisknownthatavideothatstartsupslowly,orrebuffers(i.e.,freezes)inthemiddle,or
playsatalowquality(i.e.,bitrate)canleaduserstoabandoningthevideoorwatchinglessofit.
Consequently,videoproviderswhorelyonengagingtheiraudiencefortheirbusinessgoalsplace
strongemphasisonprovidingahighQoEfortheirusers.
Maximizing the QoE of the user involves factors that are often in conflict. On the one hand,
it is desirable to play the video at the best quality at the highest encoded bitrate. On the other
hand,itisalsodesirabletoplaythevideocontinuouslywithoutthefreezescausedbyrebuffering.
However, these two factors can conflict. For instance, playing the video at high-definition (HD)
qualityatafewMbpsprovidesaricherexperiencethanplayingitatstandarddefinition(SD)of
afewhundredkbps.However,playingavideoatahighbitratethatismorethanthesustainable
networkthroughputbetweentheserverandtheclient(i.e.,videoplayer)willcausetheclienttore-
buffer,sincetheclientisunabletodownloadthevideoattherateatwhichitisbeingplayed.Thus,
providinggoodQoErequiresdynamicallyadaptingthevideobitratetothenetworkthroughput,
providingthehighestvideoqualitywithoutrebuffering.
1.1 AdaptiveVideoStreaming
Adaptivevideostreamingisapopularapproachforadaptingthevideopresentationtotheuser’s
deviceandconnectivity.Inthisapproach,eachvideoispartitionedintosegmentswhereeachseg-
ment corresponds to a few seconds of play. Each segment is encoded in a number of different
bitrates to accommodate the vastly different devices and network connectivities. Video bitrates
rangewidelyfrom4Kquality(∼25Mbps)toSDquality(∼fewhundredkbps).Whenaclientplays
avideo,itfetchesthesegmentsinsequenceoverHTTP.Anadaptivebitrate(ABR)algorithmthat
isexecutedwithintheclientcanvarythebitrateofeachdownloadedsegmentinaccordancewith
thecurrentnetworkthroughput.Specifically,duringthecourseofthevideoplayback,theclient
stepsdownthebitratewhenthenetworkconnectiondegradesandstepsupthebitratetoprovide
aricherexperiencewhenthenetworkimproves.
Topreventvideofreezes,theclienthasabufferthatcanstoreanumberofsegments.Theclient
prefetchessegmentsfromtheserveraheadofwhentheyneedtobeplayedoutandstoresthemin
thebuffer.ThesegmentsareremovedfromthebufferinFIFOorderandplayedoutfortheuser.
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:3
Ifthebufferisemptyandtherearenomoresegmentstoplayout,thenthevideoplaybackmust
freezeuntilthenextsegmentisreceived,resultinginarebufferingevent.
1.1.1 ABRAlgorithms. ThedesignandimplementationofABRalgorithmsisthefocusofourwork.
AkeygoaloftheABRalgorithmistoplaythevideoatthehighestbitrateswithoutrebuffering.To
achievethatend,theABRalgorithmcarefullyorchestrateswhatsegmentsaredownloaded,when,
and at what bitrates. Additionally, ABR algorithms also attempt to minimize bitrate oscillations
wherethebitratesareswitchedfrequentlycausingtheusertoperceivefrequentchangesinvideo
quality.ABRalgorithmshavereceivedsignificantattentioninrecentyearsandareclassifiedinto
threebroadcategories:throughput-based,buffer-based,andhybridschemes.
(1) Throughput-basedalgorithmsworkbyestimatingthenetworkthroughputavailablebe-
tweentheclientandserverandusingthatestimatetodecideonthebitrateofnextsegment
thatistobedownloaded.SuchalgorithmsincludeFestive[14],PANDA[16],andSquad
[29].
(2) Buffer-basedalgorithmspredominantlyusetheleveltowhichthebufferisfulltodecide
onthebitrateofthenextsegment.Notethatthebufferlevelisan(indirect)indicatorof
networkthroughput,asalower(respectively,higher)bufferlevelwouldindicatethatthe
networkthroughputhasrecentlybeenless(respectively,more)thananticipated.Thus,a
buffer-basedalgorithmwouldchooseahigherbitratewhenthebufferlevelishigherand
lowerifbufferlevelislower.SuchalgorithmsincludeBBA[13]andBOLA[22].
(3) Hybridalgorithmsuseboththroughputpredictionandbufferlevelsinanattempttoex-
ploittheadvantagesofboth.SuchalgorithmsincludeELASTIC[6],MPC[30],andABMA+[2].
1.1.2 Adaptive Video Streaming Formats. A significant fraction of the world’s online videos
usesHTTPadaptivestreaming(HAS).ThepopularproprietaryformatsincludeAppleHTTPLive
Streaming(HLS)[19],MicrosoftSmoothStreaming[31],andAdobeHTTPDynamicStreaming[1].
In2012,theInternationalOrganizationforStandardization(ISO)ratifiedanewopenstandardfor
adaptivevideostreamingcalledMPEG-DASH(or,simply,DASH)[23].Whileboththeproprietary
formatsandDASHaresimilarintechnology,DASHhasenormouspotentialforbeingthesingle
openstandardthatcouldreplacemultipleproprietarystandardsinthefuture.
ThesignificantpotentialofDASHhasbroughttogethermostofthemajorplayersinthevideo
industry together to form the DASH Industry Forum (DASH-IF) that maintains and promotes
theDASHstandard.Inparticular,itmaintainsaDASHreferenceclient(i.e.,videoplayer)called
dash.js[9]thatencapsulatesthestandardanditsbestpractices.Videoproviderswishingtouse
DASH often use the reference client dash.js to build their own video players. While our work
onABRalgorithmsisapplicabletoanyHASprotocol,weimplementandempiricallyevaluateour
approachwithintheDASHframework.
1.2 OurContributions
Theprimarycontributionsofourworkareasfollows.
(1) We design and implement two novel ABR algorithms: BOLA-E and DYNAMIC. Both algo-
rithmseffectivelyminimizerebufferingandbitrateoscillations,whilemaximizingtheav-
erage bitrate of the video stream viewed by the user. Further, both algorithms respond
quicklytousereventssuchaswhentheuserstartsorseeksinavideo.Finally,weshow
thatbothBOLA-EandDYNAMICprovideahighQoEevenforvideoswiththemoststringent
requirements,suchaslow-latencylivestreaming.
(2) We design and implement a segment replacement algorithm called FAST SWITCHING
that judiciously replaces low-bitrate segments in the client’s buffer with high-bitrate
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:4 K.Spiterietal.
ones, whenever possible. If the network throughput increases during playback, then
FAST SWITCHINGrespondsquicklytothenetworkeventandallowsausertoexperience
the positive effects of that increase more quickly, since the low-bitrate segments in the
client’sbuffercanbereplacedwithhigh-bitrateoneswhenthethroughputishigh.Inour
experiments, we showed that when the networkthroughputincreases during playback,
theclientwouldseeahigher-qualityvideo50ssoonerwithFAST SWITCHINGthanwithout.
(3) WehavecreatedatoolcalledSabrethatisvaluableforsimulatingABRenvironments.Its
architectureissimilartothatoftheDASHreferenceplayerdash.jsanditcanbeusedto
developandevaluateABRalgorithms.Sabresimulatestheplayerenvironmentaccurately
foranyspecifiedvideodescriptionandnetworktraces.ItoutputsQoEmetricsofinterest
suchassegmentbitratesandrebufferevents.WevalidatedSabrebyshowingthattheQoE
metricsthatitproducedclosely agreeswiththesame metricsproducedbya real-world
productionvideoplayer(dash.js).Wepublishedthetoolasanopen-sourceprojectthatis
availablepubliclyathttps://github.com/UMass-LIDS/sabresothatotherscanuseitforABR
algorithmdevelopment.Whilethetoolcanbeusedwithanyadaptivestreamingformat,
weexpectittobeparticularusefultotheDASHcommunity.
(4) Finally, the foremost contribution of our work is that we have implemented BOLA-E,
DYNAMIC and FAST SWITCHING in the standard DASH reference player dash.js. As of
the current version (dash.js version 3.0.0) [9], DYNAMIC is the default ABR algorithm
provided by the standard player. Both BOLA-E (referred to as just BOLA in the standard
implementation)andFAST SWITCHINGareoptionsthatuserscanselect.1 Consequently,
our work has significantly improved the standard DASH reference player, as noted by
thedash.jscommunity[8].And,thealgorithmsdescribedinthisarticleareactivelyused
byvideoproviders(includingAkamai,BBC,CBS,andOrange)inproduction,astheybuild
theirownvideoplayersbasedonthestandardreferenceplayer.InAppendixA,wedescribe
thedash.jsarchitecturethatisofindependentinterest,andwedescribehowweimple-
mentedouralgorithmswithinthatarchitecture.
Roadmap. Therest of thearticle is organized as follows. First, we provide some background
onadaptivebitratestreaminganddescribeourapproachtodesigningABRalgorithms(Section2).
Next,wedescribeSabre,atoolthatwedevelopedforsimulatingABRenvironmentsandthatwill
be publicly available as open source (Section 3). Sabre is used for evaluating our algorithms in
therestofthearticle.WethendevelopandevaluateBOLA-E(Section4),DYNAMIC(Section5),and
FAST SWITCHING(Section6).Wethendescriberelatedwork(Section7)andconclude(Section8).
Finally,wedescribehowweimplementedouralgorithmsindash.js(AppendixA)andgiveim-
plementationdetailsaboutSabre(AppendixB).
2 OURAPPROACHTOIMPROVINGABRALGORITHMS
OurgoalistoimproveABRalgorithmsthatarecurrentlyusedinpractice.Whileouralgorithmic
techniquesapplyequallytobothproprietaryandopenadaptivevideostreamingformats,wefocus
ourimplementationandevaluationonDASH.OurfocusonDASHisfortworeasons.First,webe-
lievethattheopenstandardallowsforgreaterflexibilityfortryingoutnewideasandinnovations.
Infact,theABRalgorithmsdescribedinthisarticle(BOLA-E,DYNAMIC,andFAST SWITCHING)are
currentlypartofthestandardreferenceplayerdash.js.Second,webelievethattheDASHopen
standard will become increasingly important as more video providers migrate to the standard,
amplifyingthereal-worldimpactofourwork.
1TheABRalgorithmscanbeselectedbyclickingthe“ShowOptions”buttoninReference[9].
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:5
2.1 RequirementsforABRAlgorithms
WestartedourABRresearchbygettingextensivefeedbackfromvideoprovidersandusersacrossa
spectrumofthemediaindustry.Particularly,weutilizedabiweeklyconferencecallbythedash.js
community for feedback [10]. There was near consensus on the requirements for a good ABR
algorithmthatwestatebelow.
(1) HighBitrate.Shouldplaythevideoatthehighestsustainablequality(i.e.,bitrate).
(2) LowRebuffering.Shouldavoidrebufferingevents(i.e.,freezes)thatoccurduetotheclient
bufferbeingempty.
(3) Low Oscillations. Should avoid excessive bitrate oscillations where the video quality is
frequentlymodifiedduringtheplayback.
(4) ResponsivenesstoNetworkEvents.Shouldreactquicklytonetworkevents.Forinstance,if
thenetworkthroughputsuddenlydrops(respectively,increases),theABRalgorithmshou-
lddecrease(respectively,increase)thevideobitratetoadjusttothenewnetworkstate.
(5) ResponsivenesstoUserEvents.Shouldreactquicklytouserevents.Forinstance,ifauser
startsupanewvideo,orseekstoanewspotwithinthesamevideo,theplaybackshould
starttoplayquicklyatthehighestsustainablebitrate.
(6) Low-LatencyLiveStreaming.Shouldperformwellwhenstreaminglivevideosthatrequires
lowlatency,wherelatencyisthemaximumtimebetweenwhenthevideoiscapturedand
whentheuserseesit.Akeychallengeisthatsincelatencymustbelow,theclientbufferis
necessarilysmallandcanholdnomorethanafewsegments.Thus,videosegmentscannot
befetchedbytheclientwellinadvanceofwhentheyareplayedout.Asmallbufferleaves
littleroomforerrorasasinglesuboptimalABRdecisioncouldresultindrainingthebuffer,
resulting in rebuffering. The precise definition of low latency is subjective and depends
ontheusecase[26,27].Inthisarticle,bylowlatency,wemeanlatenciesunder10s.
State-of-the-artABRalgorithmsknownintheliteratureoftenfallshortonsomeoftheserequire-
ments.Forexample,BBA,BOLA, andMPC[13,22,30]allrespondinadelayedfashiontonetwork
eventsaddressedinSection6.TheserequirementsformedtheguidingprinciplefortheABRalgo-
rithmdevelopmentandimplementationwedescribeintherestofthearticle.
2.2 OverviewofOurDesignandImplementationofABRAlgorithms
Westartedoutbyimplementingabuffer-basedschemecalledBOLA[22]thatistoourknowledge
theonlyknownonlineABRalgorithmwithprovableoptimalityguaranteeswithinautilityframe-
work. BOLA utilizes Lyapunov optimal control to make ABR decisions based on buffer levels to
maximizeanarbitraryutilityfunctionthatcombinesthetwokeyQoEmetricsofvideobitrateand
rebuffering.Inparticular,itisshowninReference[22]thatBOLAasymptoticallyachievesutility
that is within an additive factor of optimal. While BOLA achieves near-optimal utility in steady-
stateconditions,thetheorydoesnotapplytotransientconditions.Theoreticalmodelsgenerally
cannot capture all the complexity of production systems. But, our approach is to start with the
sound theoretical foundations provided by BOLA and then adapt it to practical implementations
thatmodeltheintricaciesofproductionsettings[17].
Like other buffer-based ABR algorithms, BOLA uses a bitrate selection function that maps the
current buffer level to the bitrate (in kbps) of the next segment to be downloaded, where buffer
level is the total number of seconds of video segments stored in the buffer. The buffer may not
exceedthebuffercapacity,whichisthetotalnumberofseconds2ofvideothatthebuffercanstore.
Asnotedearlier,buffercapacityisalowerboundonlivestreamlatency,andsoalivestreamthat
2Byconvention,wemeasurethebufferinsecondsratherthaninbytes.
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:6 K.Spiterietal.
Fig. 1. Example of a bitrate selection function with a buffer capacity is 18s and with thresholds at 5, 10,
and15s.
Fig. 2. Overview of our design Fig. 3. Sabre: Inputs, Outputs, and
andproductionimplementationof Primitives.
ABRalgorithmsfordash.js.
uses low latency can only use a small buffer. Figure 1 shows an example of a bitrate selection
functionforavideothatisencodedinthreebitrates(1,000,2,500,and5,000kbps)andhasabuffer
capacityof18s.
VideosegmentstypicallyenterandexitthebufferinFIFOfashion.Assegmentsgetplayedout
fromthefrontofthebuffer,newsegmentsgetaddedtothetailofthebuffer.Segmentlengthisthe
numberofsecondsofvideointhesegment,andsegmentsizeisthenumberofbitsinthesegment.
Notethatsegmentlengthsareusuallyfixed(say,3s),whilesegmentsizescanvary,especiallyfor
VBRvideos.Asthebufferlevelincreases,theABRalgorithmviewsthatasasignofgoodnetwork
throughput,anditincreasesthevideobitratebyconsultingitsbitrateselectionfunction.Thebuffer
levelswherethebitratechangesarecalledthresholds.InFigure1,thethresholdsare5,10,and15s.
WestartedoutbyimplementingandevaluatingBOLAintheDASHreferenceplayerdash.js.
WhileBOLAprovidedahighbitratewithoutsignificantbufferingoroscillations,itfellshortonthe
otherrequirementsofSection2.1thatareimportantforareal-worldproductionimplementation.
Inparticular,sinceBOLApredominantlyusedthebufferlevelsfordecisionmaking,itdidnotre-
spondquicklytousereventssuchasstartupandseekingwhenthebufferstartsoutempty.Italso
did not respond quickly enough to rapid changes in the network throughput profile. Further, it
didnotperformsufficientlywellinthelivestreamingcontextwherethelow-latencyrequirement
mandatessmallbuffers.SuchdeficienciesarenotspecifictoBOLAandarecommoninotherknown
state-of-the-artalgorithmssuchasBBA[13].ToimproveBOLA,wetookdifferentapproachesshown
inFigure2anddescribedbelow.
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:7
2.2.1 Algorithm BOLA-E. We introduced the notion of a virtual segment that contains no
videodata.Wedevelopedanewplaceholderalgorithmthatjudiciouslyaddsandremovesvirtual
segmentstochangethebufferlevelsusedbyBOLAforbitrateswitchingdecisions.Theplaceholder
algorithmsignificantlyimprovestheresponsivenessofBOLAtonetworkanduserevents.Further,
wedevisedtheinsufficientbufferrulethathelpsavoidrebufferingwhenbufferlevelsarelow,es-
peciallyinlivestreamingsituationswhenbuffersaresmall.BOLAwiththeplaceholderalgorithm
andtheinsufficientbufferruleconstitutesanenhancedversionofBOLAthatwecallBOLA-E.
BOLA-Ewasfirstreleasedasanexperimentalversionindash.jsversion2.0.0onFebruary12,
2016.Astableversionwasreleasedinversion2.6.0onSeptember1, 2017,andhasbeeninuseby
videoproviderssince.BOLA-EisnotturnedonintheDASHreferenceplayerbydefault,butitis
oneoftwooptionalABRalgorithmsavailableforvideoproviders.WepresentBOLA-Eandevaluate
itinSection4.
2.2.2 AlgorithmDYNAMIC. AnotherapproachtoimprovingBOLAistouseathroughput-based
ABRalgorithmwhenthebufferlevelislowandthendynamicallyswitchtoBOLAwhenthebuffer
level is high. The rationale for this approach is that throughput-based ABR performs better in
situations such as startup and seek when the buffer is low or empty. And BOLA performs better
when the buffer levels are sufficient large. DYNAMIC was also first released as part of dash.js
version 2.6.0 on September 1, 2017, and has been in use by video providers since. DYNAMIC is
currentlytheprimaryABRalgorithmintheDASHreferenceplayerandisturnedonbydefault
forvideoproviders.WepresentDYNAMICandevaluateitinSection5.
2.2.3 AlgorithmFAST SWITCHING. WedevelopedatechniquecalledFAST SWITCHINGthatcan
beusedwithanyABRalgorithmtoimprovevideoqualitybyreplacinglower-bitratesegmentsin
the client buffer with higher-bitrate segments. Consider a situation where a wireless client has
downloadedasequenceoflow-bitratevideosegmentswhentheconnectivitywaspoor.Suppose
nowthattheclient’sconnectivityimproves.FAST SWITCHINGallowstheclienttoreplacethelow-
bitratesegmentsinthebufferbyhigher-bitratesegmentsthatcannowbedownloadedwiththe
improvedconnectivity.Thus,FAST SWITCHINGallowstheusertoswitchtohigher-qualityviewing
soonerthanitwouldhavebeenotherwisepossible.WeimplementedFAST SWITCHINGindash.js
version2.2.0onJuly6,2016.FAST SWITCHINGcanbeturnedonbyvideoprovidersinconjunction
withanyABRalgorithm,includingthedefaultDYNAMICortheoptionalBOLA-E.WepresentFAST
SWITCHINGandevaluateitinSection6.
3 SABRE:ANOPEN-SOURCETOOLFORSIMULATINGABRENVIRONMENTS
AnaccuratesimulationtoolforABRiscriticalforalgorithmdevelopment.However,simulation
resultsarenotusefulifthesimulationtooldoesnotreflecttheconditionsofapracticalplayer.We
developedSabre,anaccuratetoolforsimulatingABRenvironmentsthatcanbeusedfordesign-
ingandevaluatingnewABRalgorithms.Forsimulationaccuracy,webasedthedesignofSabre
on the architecture of the DASH reference player dash.js. However, other video players, such
as Google’s Shaka Player and the HLS player hls.js, are functionally similar to dash.js, al-
lowingSabretobeusedasaneffectivetoolforsimulatingotherplayersaswell.Furtherdetails
aboutSabreareprovidedinAppendixB.WemadeSabreopensourceandpubliclyavailabletothe
communityonGitHub,sothatotherscanuseandcontinuetodevelopthetool.WealsousedSabreto
empiricallyevaluatealgorithmspresentedinthisarticlepriortotheirproductionimplementationin
dash.js.
UsingSabreoffersseveralmajorbenefits.Playingalongvideocanbesimulatedinafraction
of the time, e.g., a one-hour video can be simulated in less than one second. Further, it is easy
tosimulateveryspecificnetworkconditionsinareliableandreproducibleway.Inaddition,itis
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:8 K.Spiterietal.
possible to perform simulations at a large scale using several videos and thousands of network
traces,aswedoinourwork.
Tosimulatevideostreaming,SabreinvokestheABRalgorithmbeforedownloadingasegment.
TheABRalgorithmprovidesthebitrateofthesegmenttobedownloaded.Ifsegmentreplacement
is enabled, then it also provides information on whether the segment to be downloaded is new
or a replacement for an existing segment. As the segment is being downloaded, Sabre collects
and periodically reports metrics to the ABR algorithm for use in its decision making. Similar to
dash.js,Sabreallowsabandonmentofasegmentdownloadinprogress.Further,dash.jsuses
theXMLHTTPRequestprogresseventsprovidedbythebrowser.Sabresimulatestheprogressevents
toallowsimulationofsegmentabandonmentstrategies.
3.1 Inputs
TheinputstoSabrearedescribedbelow,andaredescribedinmoredetailinAppendixB.
(1) NetworkTrace.Sabrerequiresanetworktracetosimulateavideosession.Atraceshould
have a sequence of records where each record contains the time duration, and network
throughputandlatencyforthatduration.Thetracesallowsreproduciblesimulationofreal-
worldnetworkconditions,facilitatingcomparisonbetweendifferentalgorithmsorbetween
different settings for tuning a particular algorithm. The network traces can be measured
fromanactualsystemortheycanbesynthetic.
(2) Video Description. Sabre also requires a video description that is analogous to the DASH
manifest.Thevideodescriptionincludesthesegmentlength(inseconds),theencodedbi-
trates,andasegmentsizematrixC[i,j].1 ≤i ≤ N,1 ≤ j ≤M,whereN isthetotalnumber
ofsegmentsinthevideoandMisthenumberofencodedbitrates.ThevalueofC[i,j]repre-
sentsthesize(inbits)oftheithsegmentofthevideoencodedatthejthbitrate.Byallowing
thesegmentsizematrixtobespecified,weenableSabretoaccuratelysimulatevariablebi-
trate(VBR)videos.Notethatthevideodescriptioncouldrepresentanactualvideoorcould
begeneratedsynthetically.
(3) ABR Algorithm. The ABR algorithm is invoked before downloading a new segment. The
algorithmsinthisarticlesuchasBOLA-EandDYNAMICareavailablewiththeSabresoftware.
However,theusermayalsodeveloptheirownABRalgorithmsasPythonmodulesandtest
themwithSabre.
3.2 Outputs
Sabrecontinuouslycollectsandreportsadetailedlistofeventsandmetricssuchasbitrate,down-
loadtime,andsizeofeachdownloadedsegment,thedurationofeachrebufferevent,eachchange
inbitrateasthesegmentsareplayedout,andallsegmentabandonmentsandreplacements.
The Sabre output includes three important metrics that we use throughout the article. The
rebufferratioisthefractionoftimeavideosessionspendsintherebufferstate.Therebufferratio
equalsthetotalrebuffertimedividedbythesumofthetotalrebuffertimeandthetotalplaytime.
The average bitrate is the average of the encoded segment bitrate over all rendered segments.
The average bitrate oscillationis the average difference in the bitrates of consecutively rendered
segments.Thatis,theaverageoscillationequals
1
N(cid:2)−1(cid:2)
(cid:2)
N −1
(cid:2) (cid:2)bitrate(i)−bitrate(i+1)(cid:2) (cid:2),
i=1
where bitrate(i) is the encoded bitrate of the ith rendered segment and N is the number of
segments.
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:9
NotethatthebitrateitselfmaynotbedirectlyproportionaltoQoE.Forexample,theQoEim-
provementobtainedbyupgradinga1Mbpsvideotoa2MbpsvideoismuchlargerthantheQoE
improvement obtained by upgrading a 10Mbps video to an 11Mbps video, even though the bi-
trate increase is the same. However, the bitrate-to-QoE relationship is generally monotonic and
increasingoneincreasestheother.Thus,weusebitrateasameasureofQoEthoughoutthisarticle.
3.3 Primitives
SabrealsoprovidesprimitivesthatcapturecommonfunctionsthatanABRalgorithmdeveloper
can use. Currently, we only offer three throughput estimation primitives. These primitives pro-
duceanetworkthroughputestimatebasedonthehistoryofpastsegmentdownloadtimes.The
sliding-windowthroughputprimitiveproducesanestimatebyaveragingtheachievedthroughput
for the pastk successful segment downloads, wherek is the window size specified by the user.
The exponential-window throughput primitive produces an estimate by exponentially averaging
thepastdownloadswithahalf-lifeofλ,whereλcanbespecifiedbytheuser.Wealsosupportthe
dual-exponential throughput primitive that uses the exponential-window throughput primitive
withhalf-livesofλ andλ andtakesthesmallerofthetwoestimates.Wesupportthisprimitive,
1 2
since it is used in Google’s Shaka Player [12] and in the open source HLS player hls.js [5].
TheimplementationofSabreismodularenoughfortheusertoprovideadditionalthroughputor
otherprimitives.
3.4 Caveats
Sabredoesnotsimulatelow-levelprotocolssuchasTCP,andreliesondownloadtracescollected
bytheplayerduringreal-worldtesting.Also,Sabredoesnotsimulatelow-levelimplementation
detailssuchastheexactbehaviorofthebrowser’sMediaSourceExtensionsbuffer.However,omit-
tingthatlevelofdetaildoesnotsignificantlyaffectABRalgorithmperformance.SeeAppendixB
formoredetails.
Sabredoesnotsimulateaudio.TheDASHstandardrequiresthatvideoandaudioaredelivered
separately,andtheaudiodownloadusuallyhappensonaTCPsession,whichrunsparalleltothe
video download. Again, simulating the interaction accurately requires simulation of lower-level
protocols. However, the size of the audio stream is usually only a small fraction of the size of
thevideostream,allowingasimpleworkaround.Consideranexamplevideothatisaccompanied
bya160kbpsaudio.Wecanreducethenetworkbandwidthavailableby160kbpsthroughoutthe
networktracetosimulatethevideoinSabre.
3.5 NetworkTracesUsedwithSabreinOurWork
(1) 3G traces. We use 3G traces from Reference [20], a collection of 86 traces gathered in
Norwayusinga3G/HSDPAconnectionontripsbybus,metro,tram,ferry,carandtrain.
Thetraceshavea1sgranularity.
(2) 4Gtraces.Weuse4GtracesfromReference[28],asimilarcollectionof40tracesgathered
in Belgium using a 4G/LTE connection on trips by bicycle, bus, car, train, tram, and on
foot,witha1sgranularity.
(3) FCCtraces.TheFCCprovidesapublicsetofbroadbandtraces[4].Weobtainthroughput
tracesfrommeasurementsinthewebbrowsingcategory,3witheachdatapointrepresent-
ingthethroughputfor5s.Thetraceshavea5sgranularity.
3WeparseandusethetracesinamannersimilartoReference[18](https://github.com/hongzimao/pensieve/tree/master/
traces/fcc).
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:10 K.Spiterietal.
Table1. SegmentBitratesfortheBigBuckBunnyMovie
SD Mean 6.00 5.03 2.96 2.06 1.43 0.99 0.69 0.48 0.33 0.23
Bitrate(Mbps) Std.dev. 1.08 0.89 0.56 0.39 0.28 0.18 0.12 0.10 0.05 0.04
HD Mean 35.0 16.0 8.0 5.0 2.5 1.0
Bitrate(Mbps) Std.dev. 6.3 2.8 1.5 1.0 0.5 0.2
3.6 VideoDescriptionsforSabreinOurWork
WeusedtheBigBuckBunnyMovie[11],a10minmovie,foroursimulations.Table1showsthe
bitratesforboththeSDandHDvideodescriptions,withthestandarddeviationcausedbyVBR.We
useastandarddefinition(SD)encoding4withtenbitratesrangingfrom230kbpsto6Mbps,witha
segmentlengthof3s.TheinputtoSabrecontainsthesizeinbitsforeachsegmentC[i,j].Wealso
generated a high definition (HD) video description with six bitrates5 ranging from 1 to 35Mbps
byscalingthesizesoftheSDvideosegmentsdrawnfromthehighestsixSDbitrates.Usingthis
scaling,weobtainedHDbitrateswhilestillmaintainingtheVBRvariability.
3.7 SabreValidation
ForSabretobeusefulduringdevelopmentofABRalgorithms,weneedtoensurethatitsresults
accuratelypredicttheresultsthatwouldbeobtainedbyanactualreal-worldvideoplayer.Inthis
section,weevaluatehowaccuratelySabreemulatesreal-worldvideoplayerssuchasdash.js.
We first ran 20 video sessions in dash.js. We used a step function to modulate the network
throughput,spending2mineachat5,10,20,and10Mbps,thenrepeatingfromthestart.Byfre-
quentlymodulatingthethroughput,wecantesttheaccuracyofSabreunderacircumstancewhere
theABRalgorithmisfrequentlyswitchingbitrates.WeusedtheBigBuckBunnyMoviethatcan
beloadedinthereferencedash.jsplayer[9],a10min,34svideowithanencodingthatusesten
bitratesrangingfrom250kbpsto15Mbps.WeselectedtheBOLA-Ealgorithmandsetthebufferca-
pacityto25s.Foreachvideosession,werecordedthethroughputasseenbytheplayerandthree
QoEmetrics:rebufferratio,averagebitrateandaveragebitrateoscillations.
Tocompareourresultsfromthedash.jsvideoplayerwithSabre,wesimulatedthesame20
videosessionsinSabreusingBOLA-Eanda25sbuffer.TogiveSabreamatchingvideodescription
input,wemeasuredthesizeofeachvideosegment.Then,wegeneratedthenetworktraceinputs
fromthethroughputmeasurementsmadeduringthecorrespondingdash.jssessions.Aftersim-
ulating each session, we compared the QoE metrics given by the Sabre simulation to the QoE
metricsrecordedinthecorrespondingdash.jssession.
Figure4showsthebitratesselectedbytheABRalgorithmforatypicalsessionasmeasuredon
dash.jsandSabre.Theactualplayer(dash.js)andthesimulatedplayer(Sabre)showsimilar
bitrateswitchingbehavior,asnetworkconditionschangeinaccordancewiththestep-modulated
networkthroughput.Table2showstheerrorbetweenQoEmeasurementsderivedfromdash.js
andthecorrespondingSabresession.TheaveragebitratereportedbySabrehasanaverageerror
of2.3%,whiletheaveragebitrateoscillationhasanaverageerrorof5.0%.Wealsorantestsessions
withnetworkconditionscorrespondingtothe3Gand4GtracesdescribedinSection3.5.Forthese
tracesaswell,theQoEmetricsgivenbySabrecloselymatchthemetricsgivenbydash.js.Thus,
Sabre producesQoEmetricsthataccuratelyreflectmeasurementsfromthereal-worlddash.js
player.
4WeusethesameencodingusedbyReference[22].
5WeusethesetofbitratesrecommendedforYouTube(https://support.google.com/youtube/answer/1722171).
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:11
Fig.4. Thebitrateofthesegmentsdownloadedandplayedbythedash.jsplayerandbytheSabresimulator
foratypicalsession.Thethroughputshowniswhatwemeasuredindash.jstobereplayedbySabre.
Table2. TheErrorinQoEMetricsbetweendash.js
andtheCorrespondingSabreMeasurements
| Network   |       | RebufferRatio |           | AverageBitrate |          | AverageOscillation |          |
| --------- | ----- | ------------- | --------- | -------------- | -------- | ------------------ | -------- |
| condition |       | Error         |           | %Error         |          | %Error             |          |
|           | Mean  |               | Std.dev.  | Mean           | Std.dev. | Mean               | Std.dev. |
|           | 88×10 | −6            | 307×10 −6 |                |          |                    |          |
| Step      |       |               |           | 2.32           | 2.83     | 5.03               | 11.39    |
|           |       | −3            | −3        |                |          |                    |          |
| 3G        | 14×10 |               | 22×10     | 1.88           | 1.68     | 5.25               | 7.01     |
| 4G        |       | 0             | 0         | 1.41           | 1.72     | 5.91               | 11.49    |
4 BOLA-E:ENHANCEMENTSTOBOLA
Buffer-basedABRalgorithmssuchasBOLAworkbestduringsteady-stateconditions,butarenot
very responsive to user events such as startup and seeking. The buffer is usually empty at these
events, and a naive buffer-based ABR algorithm might download many lower-bitrate segments
before reaching a sufficient buffer level to download at the highest sustainable bitrate. A num-
berofheuristicshavebeenproposedtomitigateslowstartupinbuffer-basedalgorithms[13,22],
buttheheuristicsstillfallshortoftheperformanceachievedbythroughput-basedalgorithmsin
the transient period. In Section 4.1, we design and implement the placeholder algorithm as an
improvementtoBOLAtoovercomethisissue.
Further,buffer-basedalgorithmsrequireasufficientbuffercapacityforstableoperation.How-
ever,thisisnotpossibleforlivestreams,suchaslivesportingevents,thatrequirelowlatency.In
thiscase,thebuffercapacitymustbesmallerthanthelatencyboundthatwearetryingtoachieve.
Ifthebuffercapacityissmall,thenthethresholdsbetweendifferentbitratechoicesgettooclose.
Consider a typical video encoded at ten bitrates with a segment length of 3s being streamed to
avideoplayerwitha10sbuffercapacity.Thisbuffercapacityallowslessthan1sseparationbe-
tweenmanyconsecutivethresholdsasseeninFigure5(a).Evensmallsegmentsizevariabilitydue
to VBR could cause variability in the buffer level. With a small separation between thresholds,
thisbufferlevelvariabilitywouldthenbeenoughtomaketheABRalgorithmfrequentlyswitch
betweenbitrates,causingexcessiveoscillations.InSection4.2,wedesignandimplementthein-
sufficientbufferruleanduseit,togetherwithbufferexpansion,toovercomethisissue.Figure6
graphicallyshowshowweputtogetherthenewalgorithmBOLA-EfromtheoriginalBOLAusing
theplaceholderalgorithm,andtheinsufficientbufferrule.
4.1 ThePlaceholderAlgorithm
A fundamental problem with buffer-based algorithms is that the buffer level is not a good
proxy for the available network throughput in certain situations. In particular, the buffer level
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:12 K.Spiterietal.
Fig.5. BufferexpansionallowsBOLA-Etohavealargerseparationbetweenthresholds,reducingoscillations.
Fig.6. TheevolutionofBOLA-E.(a)TheoriginalBOLA.(b)AddingtheplaceholderalgorithmforBOLA-PL.
(c)AddingtheinsufficientbufferruleforBOLA-E.
underestimatesorprovidesnoinformationaboutthecurrentthroughputwhentheuserstartsup
orseeksavideo.Infact,inthecaseofastartuporaseekthebufferstartsoutempty.Themain
idea of the placeholder algorithm is that the buffer levels could be made to appear larger by ju-
diciouslyinsertingandremovingvirtualplaceholdersegmentsinthebuffer,asandwhenneeded.
ThebufferlevelusedforABRdecisionsincludesbothplaceholderandactualvideosegments.Note
thatplaceholdersegmentshavenovideocontentandcannotbeplayedout.Theyareusedpurely
tomanipulatethebufferlevelthatisusedfordecisionmakingbytheABRalgorithm.
The placeholder algorithm improves responsiveness to startup and seek events by inserting
placeholdersegmentsusingthefollowingsteps.
(1) Obtainathroughputestimate.
(2) Choose the appropriate bitrate corresponding to the throughput estimate derived in
step(1).
(3) CalculatethebufferlevelthatwouldallowBOLAtopickthechosenbitrate.Todothat,it
usesthebitrateselectionfunctionusedbyBOLA,suchastheoneshowninFigure5(a).We
canpickthebufferlevel(x-axis)thatcorrespondstothebitrate(y-axis)choseninstep(2).
(4) Insertenoughvirtualplaceholdersegmentsinthebuffertoobtainthedesiredbufferlevel.
That is, the number of placeholder segments that are inserted equals the desired buffer
levelfromstep(3)minusthetotalsizeoftheactualsegmentsinthebuffer.
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:13
Fig.7. Bitrateofthevideoplayoutasafunctionofthevideoplaytime.BOLAwiththeplaceholderalgorithm
(BOLA-PL)reactsmorequicklybyreachingthehighestsustainablebitratewithinamuchshorterperiodof
timeafterastartuporaseekthanBOLAalone.
Notethatthealgorithmneedstodownloadonelow-bitratesegmentatstartuptoobtainathrough-
putestimateinstep(1)above.However,inthecaseofseek,itwillalreadyhaveagoodestimate
availablefrompriorsegmentdownloads.
Theplaceholderalgorithmalsoremovesplaceholdersegmentswhenasituationdemandsthat
the bitrate must be held steady and not stepped up. One such situation is when BOLA disallows
switchinguptoabitratewhensuchaswitchislikelytobefollowedbyaswitchtoalowerbitrate
withinashorttime.Inthissituation,theplaceholderalgorithmattemptstoreducethebufferlevel
totheappropriatevaluebyremovingplaceholdersegments.
4.1.1 Evaluation. Wenowevaluatetheplaceholderalgorithmforresponsivenesstouserevents
such as startups and seeks. First, we use a synthetic network trace that keeps the throughput
relatively steadyat 8Mbps.We usetheSDvideo describedinSection 3.6.WethenuseSabre to
evaluateBOLAwithouttheplaceholderalgorithmandBOLA-PL,whichisBOLAwiththeplaceholder
algorithm.Bothalgorithmsuseabuffercapacityof25sintheevaluation.Ideally,thevideoshould
startplayingasquicklyaspossibleafterthestartup/seekeventatabitrateof6Mbps,whichisthe
highestencodedbitrateoftheSDvideo.
Figure7evaluatesBOLA-PLandBOLAforastartupeventwhentheuserclicksthestartbutton
andforaseekeventwheretheuserseekstothe3minpointinthevideo.BOLA-PLstartsplaying
atthehighestbitrateat3.1sforthestartupscenario.Specifically,itswitchedtohighqualityfrom
thesecondsegmentonwards.Thatisbecausetheplaceholderalgorithmneededthefirstsegment
downloadtoobtainaninitialthroughputestimate.However,BOLA-PLstartedtoplayatthehighest
bitratestartingfromthefirstsegmentafteraseek,i.e.,thehighbitrateplaybackstartedafterthe
2.4sittooktocompletedownloadingthefirstsegment.However,BOLAismuchlessresponsivefor
bothstartupandseekscenariosasithastowaitforthebufferleveltorisebeforeswitchingtothe
highestbitrate.Inparticular,ittookBOLA24.1stoswitchthehighestbitrateforboththestartup
andseekscenarios.
Figure 8 compares the startup and seek performance of BOLA and BOLA-PL for the 4G traces
describedinSection3.5.WerepeatedthestartupandseekexperimentsfortheHDvideoforeach
ofthe40tracesandcomputedtheCDFofthereactiontime,wherethereactiontimeisthetime
thatittakesforthevideotoplayatthehighestsustainablebitrate.Themedianstartupreaction
time for BOLA-PL is 9.3s, whereas BOLA took much longer to respond at 21.3s. The median seek
reactiontimeforBOLA-PLis3.1s,BOLAagaintookmuchlongertorespondat21.1s.
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:14 K.Spiterietal.
Fig.8. CDFsofthereactiontimeforBOLAversusBOLA-PLduringstartupandseekfor404Gnetworktraces.
BOLA-PLreactsmuchmorequicklyandstreamsatthehighestsustainablebitratesoonerthanBOLA.
4.2 InsufficientBufferRule
Wenowproposeasolutiontotheproblemofavoidingoscillationsinlow-latencylivestreaming.
Thelowlatencyrequirementimpliesthatthebuffercapacitymustbesmall.Foranybuffer-based
algorithmsuchasBOLA,thismeansthatthresholdswherethebitratechangesaremadeareclose
together,andevenasmallvarianceinsegmentsizeornetworkthroughputcancauseoscillations.
Using placeholder segments allows a novel approach to this problem by allowing the buffer
capacity to be large, but still restricting the total size of the actual segments in the buffer to be
nomorethanasmallvalue.Thatis,weallowalargebufferwithsignificantseparationbetween
thresholds for bitrate switching. However, we let only a small number of actual segments to be
storedinthebuffer,theremainderbeingplaceholdersegments.Withthisapproach,thelatencyis
keptsmall,sinceonlytheactualsegmentscontributetolatency.Notethatsinceonlyafewactual
segmentscanbestoredinabufferofmuchlargersize,therewillbeinstanceswhenthereisenough
spaceinthebufferandthenetworkthroughputishighenoughforasegmenttobedownloaded.
But,thealgorithmmustpauseasanewsegmentisnotyetavailableasitfallsoutsidethelatency
window. In these instances, a placeholder segment is placed in buffer to indicate that an actual
segmentcouldhavebeendownloadedifthatsegmentwasavailable.
Wenowillustratethebufferexpansiondescribedabovewithanexample.Figure5(a)showsan
exampleofBOLA’sbitrateswitchingthresholdsforalowlatencylivestreamwithabuffercapacity
of 10s. Figure 5(b) shows how it can be “stretched” to a larger buffer by modifying BOLA’s pa-
rametersV andγ. The thresholds in Figure 5(b) are at least 2s apart, reducing the potential for
oscillations.However,thetotalsizeoftheactualsegmentsthatcanbestoredinthebufferisstill
atmosttheoriginalbuffercapacityof10s.
Unfortunately,bufferexpansionresultsinalargebufferwithmanyplaceholdersegmentsbut
with few actual segments. This can increase rebuffering, even though it cuts down on the os-
cillations.PlaceholdersegmentsinduceBOLA-PLtodownloadatahigherbitrateasshowninFig-
ure5(b),butitcancauserebufferingwhenthevideosegmentsrunout,astheplaceholdersegments
arevirtualandcannotbeplayedout.Weproposetheinsufficientbufferruletosolvethisrebuffer-
ingissue.TheruleverifieseachABRchoicebyBOLA-PLtomakesurethedownloadisunlikelyto
causearebufferingeventusingthefollowingsteps.
(1) Multiplythecurrentthroughputestimateby50%toobtainasafethroughput.
(2) Multiplythesafethroughputbythevideobufferlevel(notcountingtheplaceholderseg-
ments)toobtainasafedownloadsize.
(3) LimittheABRchoicetosegmentswithsizenotlargerthanthesafedownloadsize,always
allowingthelowestbitrate.
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:15
Fig.9. CDFsoftheQoEmetricsforBOLA,BOLA-PLandBOLA-EwhenstreamingtheSDvideowithabuffer
capacityof10sfor863Gtraces.BOLA-Esignificantlyreducesoscillations.
Fig.10. TheDYNAMICalgorithmscombinesBOLAandTHROUGHPUT.
Combiningabuffer-basedalgorithmwiththeplaceholderalgorithmandtheinsufficientbuffer
produces a hybrid algorithm, which has the benefits of buffer-based algorithms while avoiding
theirusualdrawbacks.
4.2.1 Evaluation. We now compare BOLA-E that includes the buffer expansion and the insuf-
ficient buffer rule with BOLA-PL that does not include either. First, we note that we empirically
confirmed that the responsiveness of BOLA-E to startup and seek events are identically to that
of BOLA-PL shown in Figures 7 and 8. Next, we evaluated these algorithms on both 3G and 4G
tracesdescribedinSection3.5witha10sbuffercapacitytoevaluatetheirpotentialforrebuffering
and oscillations. Figure9 shows that BOLA-PL and BOLA-E have nearly identical rebuffering and
average bitrate behavior for the 3G traces. However, BOLA-E that uses the buffer expansion and
theinsufficientbufferrulehasmuchfeweroscillationsthanBOLA-PL.Inparticular,BOLA-Ehada
medianbitrateoscillationof65versus95kbpsforBOLA-PL.WealsoincludedmetricsforBOLAin
Figure9toshowthat,whileBOLA-Eimprovesreactiontime,itdoesnotdegradethesteady-state
QoE metrics. In fact, it reduces bitrate oscillations. Note that BOLA-PL without buffer expansion
andwithouttheinsufficientbufferruleincreasesbitrateoscillationswhencomparedtoBOLA.The
empiricalresultsfor4Gtracesweresimilartothatofthe3Gtraces,andwedonotincludethem
hereduetospacelimitations.
5 DYNAMIC:BOLAWITHTHROUGHPUT
Section 4 introduced enhancements to the buffer-based algorithm BOLA to mitigate issues with
startup,seekandlow-latencystreamingandcreatedanewalgorithmBOLA-E.Inthissection,we
describeadifferentapproachtomitigatethesameissues,leadingtothecreationofDYNAMICthat
iscurrentlythedefaultABRalgorithmintheDASHreferenceplayerdash.js(seeFigure2).
We observed that throughput-based algorithms perform well in low-buffer-level situations,
whereas buffer-based algorithms such as BOLA perform better at larger buffer levels. Thus, we
proposetheDYNAMICalgorithmthatusesasimplethroughput-basedalgorithmcalledTHROUGHPUT
whenthebufferlevelsarelow(suchasduringstartupandseekevents),andusesBOLAwhenthe
bufferlevelsarehighasshowninFigure10.
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:16 K.Spiterietal.
Fig.11. CDFofthereactiontimeforBOLAversusTHROUGHPUTversusDYNAMICduringstartupandseekfor40
4Gnetworktraces.THROUGHPUTandDYNAMICreactmuchmorequicklyandstreamatthehighestsustainable
bitratesoonerthanBOLA.
THROUGHPUT is a simple heuristic that first estimates the network throughput by using the
sliding-windowprimitivedescribedinSection3.3andthenpicksthehighestencodedbitratethat
islowerthanasafetyfactorof90%oftheestimatedthroughput.
AlgorithmDYNAMICworksasfollows.Atstartup,DYNAMICstartsbyinvokingTHROUGHPUT. At
thisstage,BOLAstillprefersabitratethatistoolow.Whenthebufferlevelreaches10sormore6
andBOLAchoosesabitrateatleastashighasthebitratechosenbyTHROUGHPUT,DYNAMICswitches
to BOLA. DYNAMIC switches back to THROUGHPUT when the buffer level falls below 10s and BOLA
choosesabitratelowerthanTHROUGHPUT.
5.1 Evaluation
First,westudythereactiontimeofDYNAMICwithrespecttoBOLAandTHROUGHPUTforstartupand
seekeventsusinga25sbuffer.Figure11plotstheCDFofthereactiontimewhentheABRalgorithm
reachesthehighestsustainablebitrate.Asexpected,bothTHROUGHPUTandDYNAMICprovidefast
reaction time(s), while BOLA responds slower, since it needs to build up its buffer to a sufficient
leveltoswitchuptothehighestsustainablebitrate.Notethattheimprovementinreactiontime
doesnotincurdegradationinotherQoEmetrics,asshowninFigure12.
Figure 12 compares DYNAMIC, BOLA and THROUGHPUT individually for two scenarios on 40 4G
tracesandplotstheCDFsfortherebufferratio,averagebitrate,andaveragebitrateoscillations.
Thefirstscenario,showninFigure12(a),isderivedbysimulatingourHDvideoover4Gtraceswith
a buffer capacity of 25s to emulate a typical VOD viewing experience. In this scenario, all three
algorithms achieve similar rebuffer ratios. However, both BOLA and DYNAMIC achieve a greater
throughput than THROUGHPUT. In particular, both BOLA and DYNAMIC achieve 19% and 22% more
median throughput, respectively, than THROUGHPUT. Further, THROUGHPUT has more oscillations
than either BOLA or DYNAMIC. In particular, at the 90th percentile, both BOLA and DYNAMIC have
lessoscillationsof1,301and1,421kbps,respectively,whileTHROUGHPUThashigheroscillationsat
1929kbps. In summary, for a typical VOD setting, both BOLA and DYNAMIC perform consistently
betterthanTHROUGHPUT.
Thesecondscenario,showninFigure12(b),evaluatesthethreealgorithmsoverthe4Gtraces
withasmall10sbuffertosimulatealow-latencylivestreamingscenario.Notethatwiththislow
buffercapacityDYNAMICcannevercrossthe10sbufferlevelthresholdtoselectBOLA.Inthissce-
nario,allthreealgorithmsachievesimilarrebufferratios.BOLAachievesagreaterthroughputthan
6Wechoose10sbecauseBOLAcanhaveissueswithlowerbuffercapacities(https://github.com/Dash-Industry-Forum/dash.
js/issues/1204).
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:17
Fig.12. DYNAMICcombinesstrengthsofBOLAandTHROUGHPUT:IthasthehigherbitrateofBOLAforVOD
withalargebuffercapacityandthelowoscillationsofTHROUGHPUTforlivestreamingwithasmallbuffer
capacity.
THROUGHPUT and DYNAMIC. In particular, THROUGHPUT and DYNAMIC achieve 11% (i.e., 2,049kbps)
lessmedianthroughputthanBOLA.However,BOLA’shighthroughputcomesatthecostofexces-
sive oscillations. BOLA has more oscillations than THROUGHPUT and DYNAMIC. In particular, at the
medianvalue,THROUGHPUTandDYNAMIChave1089kbpsbitrateoscillations,whileBOLAhashigher
oscillationsat2,465kbps.Insummary,foratypicallivesetting,THROUGHPUTandDYNAMICperform
consistentlybetterthanBOLA.
The main conclusion we can draw from our experiments is that, while BOLA works better in
a VOD scenario with larger buffers, and THROUGHPUT works better for smaller buffer scenarios
likelow-latencylivestreaming,DYNAMICcombinestheadvantageofbothandworkswellinboth
situations.DYNAMICalsoprovidesafastresponseinstartupandseekscenarios,makingitagood
choiceoverallasanABRalgorithm.
6 FAST SWITCHING:ASEGMENTREPLACEMENTALGORITHM
AlargebuffercanimprovestabilityinABRperformance,becauseitcanabsorbminorvariations
innetworkconditions,butitmaydeterioratethevideoplayerresponsivenesstonetworkevents.If
thenetworkthroughputsuddenlyincreasessignificantly,thentheABRalgorithmmaydownload
segmentsatahigherbitrate.However,thevideoplayermustfirstplayoutthelow-bitratesegments
that are already in the buffer before it can render the newly-fetched high-bitrate segments. The
biggerthebuffercapacity,themorelow-bitratesegmentsitmighthold,andthelongerthewait
beforetheusercanswitchtoahigherquality.
WeproposeanalgorithmcalledFAST SWITCHINGthatimprovesthevideoplayerresponsiveness
to higher network throughput by replacing segments already in the buffer. In particular, FAST
SWITCHINGallowsvideoproviderstohavelargerbuffersforreasonsofABRstability,butyethave
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:18 K.Spiterietal.
quicker response times to network events. We have found that FAST SWITCHING is particularly
usefulforvideoproviderswithlongerVODcontent,suchasTVepisodesandmovies,wherelarger
buffersaredesirableandthereisnolowlatencyrequirement.NotethatFAST SWITCHINGcanbe
usedwithanybitrateselectionstrategy,includingBOLA-E,THROUGHPUT,andDYNAMIC.Infact,the
currentimplementationofdash.jsallowsFAST SWITCHINGtobeaddedtoallthreeoptions.
FAST SWITCHINGworksusingthefollowingsteps.
(1) Decidewhethertodownloadanewsegmentorareplacementsegment.Beforedownloading
asegment,thealgorithminvokesabitrateselectionalgorithm(e.g.,BOLA-E)todetermine
thebitrateb thatcanbeusedatthecurrenttime.Ifthereissegmentinthebufferwitha
bitratelowerthanb andifsuchasegmentcanbesafelyreplaced,thenFAST SWITCHING
decides that the next segment downloaded will be a replacement. Otherwise, the next
segment downloaded will be a new segment that is appended to the end of the buffer.
Intuitively,asegmentcannotbesafelyreplacedifitistooclosetotheplayheadanditwill
likelystarttobeplayedoutbeforethereplacementcanbedownloaded.Thatwouldresult
inawasteddownload.FAST SWITCHINGconsidersanysegmentthatisscheduledtostart
renderingwithinthenext1.5×(thesegmentlength)secondstobenotsafelyreplaceable.
(2) Determinewhichsegmenttoreplace.Ifitisdeterminedinstep(1)thatasegmentneedsto
bereplaced,thenFAST SWITCHINGdownloadsareplacementfortheearliestsegmentin
thebufferthatisbothsafelyreplaceableandhasalowerbitratethanthecurrentbitrateb.
Thechoiceof1.5×(thesegmentlength)indefiningasafereplacementgivesa50%safetyfac-
tortoaccountforpossiblevariationsinthedownloadtimeduetonetworkand/orsegmentsize
variability.NotealsothatFAST SWITCHINGreplacessegmentsintheearliest-deadline-first(EDF)
order,startingfromthesegmentthathastheearliestdeadlinetobeplayedout(i.e.,closesttothe
playhead).Thisorderingmaymakeitpossibletoreplacemoresegments,sincesegmentsfurther
downintheorderinghavemoretimeforreplacement.
TheFAST SWITCHINGalgorithmworkswithboththroughput-basedandbuffer-basedABRal-
gorithms. However, buffer-based algorithms might need adjustments. When FAST SWITCHING
choosestoreplaceanexistingsegment,thebufferlevelisdepleted,sincesegmentsarebeingplayed
out,butthebufferlevelisnotincreasedbythedownloadedsegment.Thislowerbufferlevelmight
inducebuffer-basedABRalgorithmstochoosealowerbitrateandthusincreasingoscillations.
We handle this problem using two different approaches when integrating FAST SWITCHING
withBOLA-EandDYNAMIC.BOLA-Einsertsoneplaceholdersegmentinthebufferaftereverysuc-
cessful segment replacement. This solution does not work for DYNAMIC, because it does not use
theplaceholderalgorithm.Instead,DYNAMICswitchestoTHROUGHPUTwheneverthereissegment
replacement,tillthebufferlevelstabilizes,afterwhichitcanswitchbacktoBOLA.
When using FAST SWITCHING, the player discards some lower-bitrate segments by replacing
themwithhigher-bitratesegments,increasingthetotalbitsdownloadedbytheclient.IntheSD
examplebelow,whentheclientexperiencesa48%improvementinmedianaveragebitrate,10%of
thebitsweredownloadedanddiscardedbytheclient.However,bitsaredownloadedanddiscarded
onlyfortheshortperiodoftimewhennetworkthroughputchangesdrasticallyandsegmentre-
placementisnecessary.So,theoverallimpactofFAST SWITCHINGonserver-clienttrafficisless
significant.
6.1 Evaluation
We now evaluate FAST SWITCHING by integrating it with both BOLA-E and DYNAMIC. To effec-
tivelysimulateFAST SWITCHING, weneedtogeneratescenarioswherethenetworkthroughput
increases. We use two videos for the simulation, the SD video and the HD video described in
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:19
Fig.13. CDFsofreactiontimewhenincreasingthenetworkthroughputusingBOLA-EandDYNAMICwithand
withoutFAST SWITCHINGusinga25sbuffer.Thereactiontimeshowshowlongittakestostartrenderingat
thehighestsustainablebitrateafterthenetworkthroughputincreases.
Section 3.6. For the SD video, we use the FCC traces described in Section 3.5 to generate 1,000
networktraces,whereeachtraceconsistsof60satalowaveragethroughputlessthan1Mbpsand
120satahighaveragethroughputbetween6and12Mbps.FortheHDvideo,weusetheFCCtraces
togenerate1,000networktraces,whereeachtraceconsistsof60satalowaveragethroughputless
than2.5Mbpsand120satahighaveragethroughputabove16Mbps.Foreachvideo,the1,000net-
worktracesweregeneratedbyrandomlypickingtwotraceswiththedesiredpropertiesfromthe
FCCtraces,onetracethatisrandomlypickedforthelowthroughputperiodthatisconcatenated
withanotherthatisrandomlypickedforthehighthroughputperiod.Thetracesarepickedran-
domlywithoutreplacement,sothatwedonothavethesametracepickedtwiceandallthe1,000
tracesthatarepickedforavideoareunique.
Foreachtrace,sometimeafterthenetworkthroughputincreases,theviewerstartstoseethe
videoatahigherbitratethatcanbesustainedbythehigherthroughput.Wemeasurethereaction
timeastheelapsedtimefromwhenthenetworkthroughputincreasedtowhentheuserstarted
viewing the video at the highest sustainable bitrate. Specifically, for the SD (respectively, HD)
video, we measure the time until the video starts rendering at 6Mbps (respectively, 16Mbps). In
bothcases,wesimulateavideoplayerwitha25sbuffer.
Figure13showsthereactiontimesforBOLA-EandDYNAMICwithFAST SWITCHING,denotedby
“BOLA-E-FS”and“DYNAMIC-FS,”respectively,incomparisonwithBOLA-EandDYNAMICbythem-
selves.WecanseethatFAST SWITCHINGimprovesthemedianreactiontimebyabout50sforboth
ABRalgorithmsandforboththeSDandtheHDvideos.Thismeansthattheuserwillseeahigher
qualityvideoabout50searlierwithFAST SWITCHINGthanwithout.
Notethattheimprovementof50sismorethanthebuffercapacityof25s.Thisispossiblebecause
therearetwocomponentstothereactiontimeforanABRalgorithmwithoutFAST SWITCHING.
First, the ABR algorithm needs to determine that the throughput has increased and choose the
corresponding higher bitrate. Second, the low-bitrate segments already in the buffer need to be
playedoutbeforethenewhigher-bitratesegmentscanbeplayed.FAST SWITCHINGmitigatesboth
componentsofthereactiontime,asitcanreplacelow-bitratesegmentsdownloadedinbothphases.
Since FAST SWITCHING switches to a higher bitrate sooner, we expect it to also improve the
averagebitratefortheaboveexperiments.Infact,themiddlecolumninFigure14showsitgives
asignificantimprovement.Itimprovesthemedianbitratebyabout45%forbothABRalgorithms
andforboththeSDandHDvideos.
Figure 14 also shows that for the experiments above, for all cases FAST SWITCHING does
not noticeably increase rebuffering and for most cases it does not significantly increase bitrate
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:20 K.Spiterietal.
Fig.14. CDFofQoEmetricswithandwithoutFAST SWITCHINGusinga25sbuffer.
Fig.15. CDFofQoEmetricswithFAST SWITCHINGusing4Gtraces.Thediscardedfractionisthefractionof
totaldownloadedbitsthatwerereplacedandhenceneverplayedbacktotheviewer.
oscillations.ItonlyincreasesthebitrateoscillationssignificantlyforsomeoftheDYNAMICtestsfor
theHDvideo.Inparticular,atthe90thpercentile,itincreasesbitrateoscillationsby306kbps.
Note that while the QoE metrics for BOLA-E and DYNAMIC are similar, there is a noticable
differene in bitrateoscillations in Figure14(b). FAST SWITCHING causesthe bufferlevel to drop,
leading DYNAMIC to switch to the THROUGHPUT algorithm. Since the network traces have high
bandwidth variability, the THROUGHPUT algorithm gives higher bitrate oscillations. This problem
doesnotaffectBOLA-E.
AdrawbackofFAST SWITCHINGisdownloadoverhead.Whenareplacementsegmentisdown-
loaded,thepreviously-downloadedsegmentisdiscardedandneverplayedbacktotheviewer.Thus
suchanoverheadinducesadditionalbandwidthcosts.Tomeasuretheoverhead,wetestedFAST
SWITCHINGwiththe4Gtraces;the4Gtraceshavethroughputvariationsoccurringatfrequencies
thataretypicalinreal-worldscenarios.Figure15showsthediscardedfraction;thediscardedfrac-
tionisthenumberofdiscardedbitsasafractionofthetotaldownloadedbitsforasession.The
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:21
Fig.16. CDFofQoEmetricsofBOLA-EwithFAST SWITCHINGwithdifferentreplacementoffsets.
mediandiscardedfractionis6%.Thebenefitsobtainedfromthisoverheadarefasterreactionstimes
andanimprovementintheaveragebitrate,witha5%improvementinbitrateinthemediancase.
6.2 RationalefortheDesignChoicesMadeinFAST SWITCHING
Figures13and14showthatusingFAST SWITCHINGimprovesthereactiontimetonetworkevents
and consequently also improves the QoE metrics. In this section, we outline and evaluate the
differentdesignchoicesthatarepossiblewithinthecontextofsegmentreplacementandjustify
thechoicesmadeinFAST SWITCHING.
(1) Replacement offset. FAST SWITCHING replaces segments in an earliest-deadline-first(EDF)
fashion, starting with segments that are closest to the play head. However, starting with
segmentsthatare“tooclose”totheplayheadentailstheriskofthesegmentbeingplayed
out before the download of the replacement is complete. Therefore, we use a time offset
to determine the distance (in seconds) from the play head that a segment must have to
beconsideredtobesafelyreplaceable.Weexperimentedwithdifferentvaluesfortheoffset
including0×,1.5×,and3×(thesegmentlength)usingtheFCCtracesusedinSection6.1that
stepupfromlowthroughputtohighthroughput.A0×offsetmeansthatthefirstsegment
after the currently playing segment is replaced. Figure 16 shows the QoE metrics for the
different factors when using BOLA-E with FAST SWITCHING for the SD video. A 0× offset
introduces excessive oscillations and causes a significant drop in average bitrate for half
the traces. However, a 3× offset is slow to react and does not get the full average bitrate
improvement from replacement. We also ran tests for other videos such a HD video, and
otherABRalgorithmssuchasDYNAMICandotherreplacementoffsetsbetween0×and3×.
We found that a 1.5× offset is the sweet spot. It is the lowest factor that consistently has
oscillationsaslowasthe3×offset,buthasafasterreactiontimeandhigheraveragebitrate.
Thus, we choose a replacement offset of 1.5× in our production implementation of FAST
SWITCHING.
(2) Replacementorder.BesidesEDF,weexploredotherwaysoforderingthesegmentsthatneed
tobereplaced.Inparticular,weevaluatedlatest-deadline-first(LDF)orderwherereplace-
ment starts from the segments that are farthest from the play head. We also evaluated
lowest-quality-first(LQF)wherethelowestqualitysegmentsinthebufferarereplacedfirst,
thoughnosegmentthatiswithinareplacementoffsetof1.5×(thesegmentlength)canbe
replaced.WhenthereareseveralLQFcandidateswiththesamelowbitrate,wereplacedthe
segmentthatwouldgivethelowestoscillationmetricafterreplacement.Weevaluatedand
comparedEDF,LDF,andLQFempirically,againwiththeFCCnetworktracesusedinSec-
tion6.1.Figure17showstheQoEmetricsforthedifferentreplacementorderswhenusing
BOLA-EwithFAST SWITCHINGfortheSDvideo.EDFreactsfasterthanLDFandLQF.For
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:22 K.Spiterietal.
Fig.17. CDFofQoEmetricsofBOLA-EwithFAST SWITCHINGfordifferentreplacementorders.
example,themedianreactiontimeforEDFis21s(respectively,33s),whereasLDFtook24s
(respectively,42s)andLQFtook22s(respectively,36s)whenplayingtheSD(respectively,
HD)video.Consequently,wechoseEDFforourproductionimplementationofdash.js.
7 RELATEDWORK
Throughput-based algorithms use past download history to predict the future. Festive [14] is
one such algorithm that also aims to aid fairness by delaying downloads. PANDA [16] is another
throughput-based approach that aims to improve fairness by probing the network capacity. By
accountingforfairness,FestiveandPANDAchoosebitratesconservatively.Squad[29]performs
bitrateswitchingwhileminimizingbitratevariabilityusinganovelmetriccalledspectrum.
Alternatively,buffer-basedalgorithmsuseabitrateselectionfunctiontochoosethebitratebased
onthebufferlevel.OnesuchalgorithmisBBA[13].Itneedsalargebuffercapacity(afour-minute
bufferisusedforevaluation)forstableoperation.BOLA[22]derivesabitrateselectionfunction,
presentingautilityframeworkandusingLyapunovoptimizationtechniquestoprovetheapproach
isasymptoticallynear-optimalinsteady-state.Italsousessomethroughputinformationtoprevent
oscillations,enablingstablestreamingatlowerbuffercapacities.
Other ABR algorithms are hybrid using both throughput and buffer level information.
ELASTIC[6]designsafeedbackcontrolsystemtokeepthebufferlevelclosetoapredefinedset-
point. However, it can be slow to react to some throughput changes. MPC [30] presents another
utilityframeworkandusesamodelpredictivecontrolalgorithmtooptimizeutilitywithinafinite
horizon. MPC uses the buffer level by allowing the algorithm to be more or less aggressive. One
drawbackofMPCisthattheoptimizationprocessrequiressignificantcomputation,whichhasto
beprecomputedofflineanddeliveredtothevideoplayer.ABMA+[2]startswiththegoalofmini-
mizingrebufferprobability.SimilartoMPC,itreliesoncomplexestimationcalculations,whichare
precomputedoffline.Theofflinecomputationsmaketheimplementationmorecomplexforboth
MPCandABMA+.
Therearealsorecentmachine-learningalgorithmforABR.C2SP[25]involveslearningaHidden
Markov Model for throughput prediction. It performs ABR in three stages: an offline prediction
enginethatdoesmodeltrainingandclusteringmodellearning,anonlinethroughputprediction
stage, and a bitrate selection stage. Pensieve [18] trains a neural-network to choose the bitrate
basedonthevideodescriptionandrecentdownloadmetrics.Notethat[2,18,25,30]requirepre-
computedtables,introducingadditionalcomplexityfordeploymentinproductionsystems.
Regardingevaluationtools,MACI[24]providesanemulationenvironmentthatallowsautomatic
loadingandevaluationofcompleteplayerssuchasdash.js.MACIandSabreservecomplementary
rolesinABRalgorithmdevelopment.MACIisacompleteenvironmentthatplaysthevideos,while
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:23
Sabre is a simulation environment that can more quickly test ABR algorithm for wide range of
videosandnetworktraceswithoutactuallyplayingthevideos.
8 CONCLUSION
WedesignedandimplementedSabre,anopen-sourcepubliclyavailabletoolthatcanbeusedby
researcherstorunaccuratesimulationsofABRalgorithmsusingaplayerarchitecturesimilarto
dash.js. We used Sabre to design and test BOLA-E and DYNAMIC, two algorithms that enhance
thebuffer-basedABRalgorithmBOLA.WealsodevelopedaFAST SWITCHINGalgorithmthatcan
replace segments that have already been downloaded with higher-bitrate (thus higher-quality)
segments. The new algorithms provide higher QoE to the user in terms of higher bitrate, fewer
rebuffers, and lesser bitrate oscillations. In addition, these algorithms react faster to user events
suchasstartupandseek,andrespondmorequicklytonetworkeventssuchasimprovementsin
throughput. Further, they perform well for live streams that require low latency, a challenging
problemforABRalgorithms,sincetheclientbufferneedstobekeptverysmall.Overall,thealgo-
rithmspresentedinourarticleofferssuperiorvideoQoEandresponsivenessforreal-lifeadaptive
videostreaming.AllthreealgorithmspresentedinthisarticlearenowpartoftheofficialDASH
referenceplayerdash.jsandarebeingusedbyvideoprovidersinproductionenvironments.For
videoproviderswantingtochooseBOLA-EversusDYNAMICintheproductionplayer,wealsocom-
pared them head-to-head. BOLA-E is slightly better than DYNAMIC when the network bandwidth
hashighervariability,asituationthatisalsoverychallengingfortheTHROUGHPUTalgorithm.How-
ever,DYNAMICisslightlybetterforsmallbuffercapacities,asituationthatcanbechallengingfor
allbuffer-basedalgorithmsincludingBOLA-E.WhileDYNAMICiscurrentlythedefaultchoice,we
foundbothalgorithmsperformedsimilarlywellintheQoEandresponsivenessmetrics.
APPENDIXES
A ABRALGORITHMSINDASH.JS
Thealgorithmsdescribedinthisarticleareimplementedindash.jsthatisthereferenceplayer
of the MPEG-DASH standard that is maintained by DASH Industry Forum (DASH-IF). DASH-
IF is a consortium that includes most major participants in the video streaming industry and
currently has 60+ members. Our code is part of the dash.js project repository that can be
found at https://github.com/Dash-Industry-Forum/dash.js. Extensive documentation is available
athttps://github.com/Dash-Industry-Forum/dash.js/wiki,andAPIdocumentationisalsoavailable.
Thecurrentversionis3.0.0releasedonJune28,2019.
The dash.js player is written in JavaScript and runs inside a web browser. Video rendering
is delegated to the Media Source Extensions (MSE) as implemented by the browser. The player
functionality7 is handled by a number of modules internally known as controllers. We describe
thesecontrollersastheyinteractwithouralgorithms.
Figure 18 shows a simplified overview of the player architecture. A streaming session starts
whentheplayerloadsamanifestfile,whichdescribesthevideo,knownastheMediaPresentation
Description(MPD).TheDashAdapterparsestheMPDtoobtaininformationsuchasvideolength,
segmentlength,encodedbitrates,andpossiblelive-streamingdetails.
OuralgorithmsareincorporatedintheScheduleControllerandabrControllerasdescribed
below.TheScheduleControllermanagesthehigh-leveltaskofsegmentdownload.Todownload
asegment,theScheduleControllerqueriestheabrControllertochooseabitrate,theninstructs
7Wewillnotdescribeanumberofdash.jsfeaturessuchasDRMsupportandsubtitles;whilethesefeaturesarecrucial
forcommercialstreaming,theirdetailsarebeyondthescopeofthisarticle.
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:24 K.Spiterietal.
Fig.18. Thesimplifieddash.jsplayerarchitecture. Fig.19. TheSabrearchitecture.
OurworkisincorporatedintheScheduleandABR
controllers.
theFragmentLoader8 todownloadthevideosegmentatthatbitrate.Oncethesegmentisdown-
loaded,theBufferControllerreceivesitandsendsthebytestotheMSEbuffer.AftertheMSE
bufferhasbeenupdated,theScheduleControllercanrestarttheprocessforthenextsegment.
Thisprocessmightneedtobescheduledinthefutureforanumberreasons.Forexample,thenext
segmentmightnotyetbeavailableinalivestream,orthebufferlevelmighthavereachedthebuffer
capacity.TheScheduleControlleristhemodulewhereweimplementedtheFAST SWITCHINGal-
gorithmdescribedinSection6.Itcanbefoundinthesourcetreeatsrc/streaming/controllers/
ScheduleController.js.
TheabrControllermanagesacollectionofABRrules,whichcanbefoundinthesourcetree
at src/streaming/rules/abr. Figure 20 shows how the controller uses the rules to choose a
bitrate.ThecontrollermaintainsacollectionofABRrules,thefirstthreeofwhichweredesigned
andimplementedbyusasdescribedinthearticle.
(1) ThroughputRule: Select bitrate based on the THROUGHPUT algorithms described in Sec-
tion5.
(2) BolaRule:SelectbitratebasedontheBOLA-EalgorithmdescribedinSection4.
(3) InsufficientBufferRule:Limitbitratebasedontheinsufficientbufferruledescribedin
Section4.
(4) SwitchHistoryRule:Additionalheuristictodetectandavoidanyextremebitrateoscil-
lationsallowedbytheABRalgorithms.
(5) DroppedFramesRule:Additionalheuristictoavoidusingbitratesthatexceedthedevice
computationalresources.
8Indash.jssegmentsaresometimesreferredtoasfragments.
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:25
Fig.20. TheabrControllerinthecurrentdash.jsplayerprovidesthevideoproviderachoiceofthethree
ABRalgorithmsdescribedinthisarticle.
WemodifiedtheabrControllertoofferthevideoproviderthechoiceofusingDYNAMIC,which
isturnedonbydefault,BOLA,9 orTHROUGHPUT.AsshowninFigure20,whenDYNAMICischosen,
eitherTHROUGHPUTorBOLAisselectedaccordingtothecriteriadescribedinSection5.Whenthe
9ThealgorithmdescribedasBOLA-EinSection4islabeledassimplyBOLAintheactualproductionimplementationof
dash.js.
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:26 K.Spiterietal.
videoprovideroptionallychooseseitherTHROUGHPUTorBOLA,onlythechosenalgorithmisexe-
cutedasshowninthefigure.
UsingourABRalgorithmsindash.js.Anexampleplayerimplementationbasedondash.js
can be found at http://reference.dashif.org/dash.js/. The implementation provides options to
choosebetweenthedifferentABRalgorithmsdescribedinthisarticle.Developerscanbuildtheir
ownvideoplayersbasedondash.jsasdescribedontheprojectrepositoryfrontpage.Thedocu-
mentationindicatesthedevelopmentdependenciesrequiredandalsoprovidesaquick-startguide
to setting up a basic player. The API documentation also shows how the ABR algorithm can be
changedusingasimpleJavaScriptcommand.
B SIMULATINGABRALGORITHMSINSABRE
Sabre is an open-source simulation environment for ABR algorithms licensed under the Sim-
plified BSD License. It is a Python tool that facilitates initial development and quick evaluation
of algorithms in an environment similar to real production players, without requiring the al-
gorithm researchers to learn the often complex implementation details of a production player.
Sabre takes a video description, network trace, and an ABR algorithm as inputs and gives a
collection of QoE metrics as output. The software and documentation are available at https://
github.com/UMass-LIDS/sabre.
Figure19showsanoverviewoftheSabrearchitecture.Thevideoadaptercanreadasimplified
manifestforthevideothatisbeingsimulated.Wesimulatethedownloadofvideosegmentsusing
anetworkmodelthatcanemulatenetworkconditionsfromatracefile.Pythonmodulesforthe
ABRalgorithmandforthesegmentreplacementalgorithminsidetheschedulecontrollercanbe
providedasinputstoSabre,allowingnewalgorithmstobeevaluated.
Sabre’sarchitectureissimilartothatofdash.js,ascanbeseenfromthesimilaritiesbetween
Figures 18 and 19. This helps algorithms developed within the Sabre environment to be easily
implementableindash.js.However,othervideoplayers,suchasGoogle’sShaka Playerandthe
HLSplayerhls.js,arefunctionallysimilartodash.js,allowingSabretobeusedasaneffective
toolforsimulatingotherplayersaswell.
B.1 UsingSabreforVideoPlayerSimulations
Sabrecanbeusedeitherthroughthecommandlineorprogrammatically.Theinputsandoutputs
ofSabrearedescribedbelow.
B.1.1 VideoManifest. TheinputvideospecificationisgivenasafileintheJavaScriptObject
Notation(JSON)format.Anexampleisshownbelow.
{
"segment_duration_ms": 3000,
"bitrates_kbps": [ 1000, 2000, 4000 ],
"segment_sizes_bits": [
[ 3000000, 6000000, 12000000 ],
[ 3177800, 6311760, 12310936 ],
[ 2932704, 5854096, 11732072 ],
[ 2667248, 5652216, 11217520 ],
[ 3222248, 6181928, 12739472 ]
]
}
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:27
Thefilecontainsthreefields:thesegmentduration,thelistofbitrates,andthesizeofeachvideo
segment available. In the example, each video segment is 3s long, and the video is encoded at
three bitrates: 1,000, 2,000, and 4,000kbps. The video is 15s long, and there are five segments
available at each bitrate. Note that the segments sizes for a particular bitrate might be differ-
ent because of VBR. The video manifests used in this article are provided in the source tree at
example/tomm19/{bbb,bbb4k}.json.
B.1.2 ABR Algorithm. The ABR algorithms that are described in this article are provided as
Pythonclassesinthemainmodulesrc/sabre.py.TheusercanprovideanewABRalgorithmas
input by creating a new Python module. Detailed documentation of the interface is available at
https://github.com/UMass-LIDS/sabre/wiki.Anexampleofasimpleuser-definedABRmoduleis
providedbelow.
import sabre
class CustomAbr(sabre.Abr):
def get_quality_delay(self, segment_index):
| manifest =       | self.session.manifest           |              |
| ---------------- | ------------------------------- | ------------ |
| bitrates =       | manifest.bitrates               |              |
| throughput       | = self.session.get_throughput() |              |
| quality = 0      |                                 |              |
| while (quality   | + 1 < len(bitrates)             | and          |
| bitrates[quality | + 1] <=                         | throughput): |
| quality +=       | 1                               |              |
| return (quality, | 0)                              |              |
B.1.3 SegmentReplacementAlgorithm. TheFAST SWITCHINGalgorithmdescribedinthisarticle
is provided as a Python class in the main module src/sabre.py. A new replacementalgorithm
canbeprovidedbytheuserasaninputbycreatinganewPythonmodule.Detaileddocumentation
oftheinterfaceisavailableathttps://github.com/UMass-LIDS/sabre/wiki.Anexampleofasimple
user-definedreplacementmoduleisprovidedbelow.
import sabre
class CustomReplacement(sabre.Replacement):
| def check_replace(self,                     | quality):             |               |
| ------------------------------------------- | --------------------- | ------------- |
| buffer = self.session.get_buffer_contents() |                       |               |
| for i in range(2,                           | len(buffer)):         |               |
| if buffer[i]                                | < quality:            |               |
| #                                           | return -ve index from | end of buffer |
return i - len(buffer)
| # if we arrive | here, no switching | occurs |
| -------------- | ------------------ | ------ |
return None
B.1.4 NetworkTrace. TheinputnetworktraceisgivenasafileintheJSONformat.Anexample
isshownbelow.
[
{"duration_ms": 30000, "bandwidth_kbps": 5000, "latency_ms": 75},
{"duration_ms": 30000, "bandwidth_kbps": 3000, "latency_ms": 150},
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

67:28 K.Spiterietal.
{"duration_ms": 30000, "bandwidth_kbps": 1500, "latency_ms": 200},
{"duration_ms": 30000, "bandwidth_kbps": 3000, "latency_ms": 150}
]
Thefilecontainsalistoffourrecordsrepresentingdifferenttimeperiodsandthenetworkstate
in each of those periods. The first period lasts 30s, and while in this state the network allows a
throughputof5,000kbps,witharound-triplatencyof75ms.Whenthefourperiodscometoanend
aftertwominutes,Sabrerestartsatthetop.Thenetworktracesusedinthisarticleareprovided
inthesourcetreeatexample/tomm19/{3Glogs,4Glogs,sd_fs,hd_fs}/.
B.1.5 Outputs. While Sabre runs a session for the provided inputs, it collects a set of QoE
metrics.Anexampleoutputisshownbelow.
| total played    | bitrate: 1765337 |      |
| --------------- | ---------------- | ---- |
| time average    | played bitrate:  | 2956 |
| total play      | time: 1791       |      |
| total rebuffer: | 0                |      |
| rebuffer        | ratio: 0         |      |
| time average    | rebuffer: 0      |      |
| total rebuffer  | events: 0        |      |
| time average    | rebuffer events: | 0    |
| total bitrate   | change: 341760   |      |
| time average    | bitrate change:  | 572  |
| reaction        | time: 3.252272   |      |
Sabrecanalsoprovideadetailedhistoryofalldownloads(successfulorabandoned)andwhich
segmentswereplayedback.
B.2 ASabreScriptExample
Togeneratetheplotsforthisarticle,weusedanautomatedscriptthatcanbefoundinthesource
tree at example/tomm19/generate.py. Documentation about the script can be found at https:
//github.com/UMass-LIDS/sabre/wiki/TOMM-19-Plots.
ACKNOWLEDGMENTS
Theauthorsthanktheanonymousreviewersfortheirvaluablecommentsandhelpfulsuggestions.
REFERENCES
[1] Adobe.2013.HTTPDynamicStreamingSpecificationVersion3.0FINAL.Retrievedfromhttps://www.adobe.com/
devnet/hds.html.
[2] AndrzejBeben,P.Wiśniewski,J.MongayBatalla,andPiotrKrawiec.2016.ABMA+:Lightweightandefficiental-
gorithmforHTTPadaptivestreaming.InProceedingsofthe7thInternationalConferenceonMultimediaSystems.
ACM,2.
[3] Cisco.2019.CiscoVisualNetworkingIndex:ForecastandTrends,2017–2022.Retrievedfromhttps://www.cisco.com/
c/en/us/solutions/collateral/service-provider/visual-networking-index-vni/white-paper-c11-741490.html.
[4] FederalCommunicationsCommision.2016.RawData—MeasuringBroadbandAmerica2016.Retrievedfromhttps://
www.fcc.gov/reports-research/reports/measuring-broadband-america/raw-data-measuring-broadband-america-
2016.
[5] Dailymotion. 2017. hls.js, from Dailymotion to Beyond. Retrieved from https://medium.com/dailymotion/
hls-js-from-dailymotion-to-beyond-384c0b2eeaa6.
[6] LucaDeCicco,VitoCaldaralo,VittorioPalmisano,andSaverioMascolo.2013.Elastic:Aclient-sidecontrollerfor
dynamicadaptivestreamingoverhttp(dash).InProceedingsofthe20thInternationalPacketVideoWorkshop(PV’13).
IEEE,1–8.
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.

FromTheorytoPractice:ImprovingBitrateAdaptationintheDASHReferencePlayer 67:29
[7] FlorinDobrian,VyasSekar,AsadAwan,IonStoica,DilipJoseph,AdityaGanjam,JibinZhan,andHuiZhang.2011.
Understandingtheimpactofvideoqualityonuserengagement.InACMSIGCOMMComputerCommunicationReview,
vol.41.ACM,362–373.
[8] DASH Industry Forum. 2016. September 13, 2016 dash.js Meeting Minutes. Retrieved from https://github.com/
Dash-Industry-Forum/dash.js/wiki/Meeting-Minutes.
[9] DASHIndustryForum.2019.DASHReferenceClient3.0.0.Retrievedfromhttps://reference.dashif.org/dash.js/v3.0.
0/samples/dash-if-reference-player/index.html.
[10] DASH Industry Forum. accessed 2019. dash.js Meeting Minutes. Retrieved from https://github.com/
Dash-Industry-Forum/dash.js/wiki/Meeting-Minutes.
[11] BlenderFoundation.2008.BigBuckBunnyMovie.Retrievedfromhttps://peach.blender.org/.
[12] Google.2015.ShakaPlayer.Retrievedfromhttps://opensource.google.com/projects/shaka-player.
[13] Te-YuanHuang,RameshJohari,NickMcKeown,MatthewTrunnell,andMarkWatson.2015.Abuffer-basedapproach
torateadaptation:Evidencefromalargevideostreamingservice.ACMSIGCOMMComput.Commun.Rev.44,4(2015),
187–198.
[14] JunchenJiang,VyasSekar,andHuiZhang.2012.Improvingfairness,efficiency,andstabilityinhttp-basedadaptive
videostreamingwithfestive.InProceedingsofthe8thInternationalConferenceonEmergingNetworkingExperiments
andTechnologies.ACM,97–108.
[15] S.ShunmugaKrishnanandRameshK.Sitaraman.2013.Videostreamqualityimpactsviewerbehavior:Inferring
causalityusingquasi-experimentaldesigns.IEEE/ACMTrans.Netw.21,6(2013),2001–2014.
[16] ZhiLi,XiaoqingZhu,JoshuaGahm,RongPan,HaoHu,AliC.Begen,andDavidOran.2014.Probeandadapt:Rate
adaptationforHTTPvideostreamingatscale.IEEEJ.Select.AreasCommun.32,4(2014),719–733.
[17] BruceM.MaggsandRameshK.Sitaraman.2015.Algorithmicnuggetsincontentdelivery.ACMSIGCOMMComput.
Commun.Rev.45,3(2015),52–66.
[18] HongziMao,RaviNetravali,andMohammadAlizadeh.2017.Neuraladaptivevideostreamingwithpensieve.Pro-
ceedingsoftheACMAnnualACMConferenceoftheSpecialInterestGrouponDataCommunication(SIGCOMM’17).
[19] R.PantosandW.May.2017.HTTPLiveStreaming.RFC8216.RFCEditor.
[20] HaakonRiiser,PaulVigmostad,CarstenGriwodz,andPålHalvorsen.2013.Commutepathbandwidthtracesfrom3G
networks:Analysisandapplications.InProceedingsofthe4thACMMultimediaSystemsConference.ACM,114–118.
[21] KevinSpiteri,RameshSitaraman,andDanielSparacio.2018.Fromtheorytopractice:Improvingbitrateadaptation
intheDASHreferenceplayer.InProceedingsofthe9thACMMultimediaSystemsConference.ACM,124–137.
[22] KevinSpiteri,RahulUrgaonkar,andRameshK.Sitaraman.2016.BOLA:Near-optimalbitrateadaptationforonline
videos.InProceedingsofthe35thAnnualIEEEInternationalConferenceonComputerCommunications(IEEEINFO-
COM’16).IEEE,1–9.
[23] ThomasStockhammer.2011.DynamicadaptivestreamingoverHTTP—Standardsanddesignprinciples.InProceed-
ingsofthe2ndAnnualACMConferenceonMultimediaSystems.ACM,133–144.
[24] DennyStohr,AlexanderFrömmgen,AmrRizk,MichaelZink,RalfSteinmetz,andWolfgangEffelsberg.2017.Where
arethesweetspots?AsystematicapproachtoreproducibleDASHPlayercomparisons.InProceedingsoftheACMon
MultimediaConference.ACM.
[25] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,FuyuanLin,NanshuWang,TaoLiu,andBrunoSinopoli.2016.CS2P:
Improvingvideobitrateselectionandadaptationwithdata-driventhroughputprediction.InProceedingsoftheAnnual
ACMConferenceoftheSpecialInterestGrouponDataCommunication(SIGCOMM’16).
[26] Wowza Media Systems. accessed 2019. Low Latency Streaming. Retrieved from https://www.wowza.com/
low-latency.
[27] WowzaMediaSystems.accessed2019.WhatisLowLatency,andWhoNeedsIt?Retrievedfromhttps://www.wowza.
com/blog/what-is-low-latency-and-who-needs-it.
[28] J.vanderHooft,S.Petrangeli,T.Wauters,R.Huysegems,P.R.Alface,T.Bostoen,andF.DeTurck.2016.HTTP/2-
basedadaptivestreamingofHEVCvideoover4G/LTEnetworks.IEEECommun.Lett.20,11(2016),2177–2180.
[29] CongWang,AmrRizk,andMichaelZink.2016.Squad:Aspectrum-basedqualityadaptationfordynamicadaptive
streamingoverHTTP.InProceedingsofthe7thInternationalConferenceonMultimediaSystems.ACM.
[30] XiaoqiYin,AbhishekJindal,VyasSekar,andBrunoSinopoli.2015.Acontrol-theoreticapproachfordynamicadaptive
videostreamingoverHTTP.ACMSIGCOMMComput.Commun.Rev.45,4(2015),325–338.
[31] AlexZambelli.2009.IISsmoothstreamingtechnicaloverview.Technicalreport,MicrosoftCorporation.
ReceivedNovember2018;revisedMarch2019;acceptedMay2019
ACMTrans.MultimediaComput.Commun.Appl.,Vol.15,No.2s,Article67.Publicationdate:July2019.