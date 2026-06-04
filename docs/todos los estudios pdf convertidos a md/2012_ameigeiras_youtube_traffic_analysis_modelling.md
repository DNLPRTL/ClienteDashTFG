TRANSACTIONSONEMERGINGTELECOMMUNICATIONSTECHNOLOGIES
Trans.EmergingTel.Tech.2012;23:360–377
PublishedonlineinWileyOnlineLibrary(wileyonlinelibrary.com).DOI:10.1002/ett.2546
RESEARCHARTICLE
Analysis and modelling of YouTube traffic
PabloAmeigeiras,JuanJ.Ramos-Munoz,JorgeNavarro-OrtizandJ.M.Lopez-Soler*
ResearchCenteronInformationandCommunicationsTechnologies,UniversityofGranada,Granada,Spain
ABSTRACT
YouTube currently accounts for a significant percentage of the Internet’s global traffic. Hence, understanding the
characteristicsoftheYouTubetrafficgenerationpatterncanprovideasignificantadvantageinpredictinguservideoquality
andinenhancingnetworkdesign.Inthispaper,wepresentacharacterisationofthetrafficgeneratedbyYouTubewhen
accessedfromaregularPC.Onthebasisofthischaracterisation,aYouTubeservertrafficgenerationmodelisproposed,
which,forexample,canbeeasilyimplementedinsimulationtools.Thederivedcharacterisationandmodelarebasedon
experimentalevaluationsoftrafficgeneratedbytheapplicationlayerofYouTubeservers.AYouTubeservercommences
thedownloadwithaninitialburstandlaterthrottlesdownthegenerationrate.Iftheavailablebandwidthisreduced(e.g.
inthepresenceofnetworkcongestion),theserverbehavesasifthedataexcessthatcannotbetransmittedbecauseofthe
reducedbandwidthwereaccumulatedataserver’sbuffer,whichislaterdrainedifthebandwidthavailabilityisrecovered.
Aswewillshow,thevideoclipencodingrateplaysarelevantroleindeterminingthetrafficgenerationrate,andtherefore,
acumulativedensityfunctionforthemostviewedvideoclipswillbepresented.Theproposedtrafficgenerationmodel
was implemented in a YouTube emulation server, and the generated synthetic traffic traces were compared with down-
loadsfromtheoriginalYouTubeserver.Theresultsshowthattherelativeerrorbetweendownloadsfromtheemulation
serverandtheoriginalserverdoesnotexceed6%forthe90%oftheconsideredvideos.Copyright©2012JohnWiley&
Sons,Ltd.
KEYWORDS
YouTube;YouTubetrafficgeneration;progressivedownload;YouTubedatarate;YouTubeapplicationflowcontrol;progressive
downloadtrafficgeneration
*Correspondence
J.M.Lopez-Soler,DepartmentofSignalTheory,TelematicsandCommunications,E.T.S.I.InformáticayTelecomunicación,
C/PeriodistaDanielSaucedoArandas/n,18071Granada,Spain.
E-mail:juanma@ugr.es
Received11November2011;Revised26April2012;Accepted26April2012
1. INTRODUCTION YouTubeemploystheMP4containerforhigh-definition
(HD)clipsandusestheFlashVideo(FLV)asthedefault
In recent years, the Internet has experienced enormous formatforthemajorityofnon-HDclips[4].Whereasusers
increasesintrafficfromsocialnetworkingmediadataand may upload their content in a variety of media formats,
video streaming on-demand web-based services because YouTubeadaptsthemtotheaforementionedformatsbefore
oftheincreasinginterestinuser-generatedcontent.Inter- posting [5]. YouTube employs the progressive download
net videos from sites such as YouTube, Hulu and Netflix technique that enables video playback before the con-
grewtorepresentabout40%oftheconsumerInternettraf- tent download is completely finished [5]. It also uses the
fic in 2010 [1], whereas the percentage of the Internet’s HTTP/TCP platform, which further distinguishes it from
trafficfrompeer-to-peer serviceshasdeclined inthepast traditionalmediastreaming.
fewyears[1].Amongallaudioandvideosites,YouTube The present paper aims at two main objectives: (1) to
has become the most dominant, being rated as the third shed light on the YouTube service from the viewpoint of
most visited Internet site (according to [2]); additionally, theprogressivedownloadtrafficgenerationcarriedoutby
continuingagrowingtrend,videotraffichasreached52% YouTube servers accessed from a regular PC; the ratio-
ofthetotaltrafficinmobilenetworksattheendof2011[3]. naleforitisbecausethealgorithmsandparametersruling
Therefore,theanalysisandcharacterisationofitstrafficis thetrafficgenerationarenotpubliclyavailable;and(2)to
ofmajorimportance. propose a YouTube server traffic generation model. As a
360 Copyright©2012JohnWiley&Sons,Ltd.

P.Ameigeirasetal.
result, one major benefit is that YouTube traffic sources The video clip download process is initiated by the
canbeeasilyimplementedinnetworksimulationtoolsand end-userrequestingtheYouTubewebpageofthedesired
experimentaltestbedstoevaluatetheserviceperformance video clip. When the web browser receives the YouTube
anditsend-userqualitydegradationimpact,forexample, webpage,theembeddedplayerinitiatestherequiredsig-
ascarriedoutin[6]. nalling (see Section 2.1) with the media server (selected
Inthiswork,wefocusonFLV-basedvideoclipsbecause from a farm of servers) to indicate the video that is to
the default download from regular PCs use an FLV con- beplayed.Then,theplayerstartsprogressivelydownload-
tainerformorethan92%ofthevideosclips,asitwillbe ing the video data (at a receiving data rate in the TCP
showninSection3.3.Furthermore,usersstickwithdefault layer Rr/, which is stored in a buffer (as described in
playerconfigurationswithnegligiblevoluntarychangeof Section 2.2), and later played with a playback rate equal
videoresolutions[7]. tothevideoclipencodingrateVr.Thevideoclipdataare
Our study includes a complete characterisation of the encapsulatedinanHTTPresponse,andthen,thedatafeed
progressivedownloadtechniqueusedbyYouTubeservers. aTCPstack(atatrafficgenerationrateintheapplication
Theresultswillshowthattheservercommencesadown- layerGr/withaproprietaryalgorithmbythemediaserver.
load by transferring an initial burst of 40 s of video data Finally,thedataaresentbytheTCPstack(atatransmis-
at the Internet’s maximum available bandwidth and later sion data rate in the TCP layer Tr/ to the client over the
appliesathrottlingalgorithmthatimposesadatarateequal Internet(withanavailablebandwidthB/.
to1.25timesthevideoclipencodingrate.Forthesephases,
YouTube applies a minimum size of the initial burst and
aminimumtransmissiondatarateof250kbpsduringthe 2.1. Signalling
throttlingphase.
Theexperimentalresultswillalsoshowthatiftheavail- On YouTube, each video has a unique identifier
ablebandwidthisreduced(e.g.inthepresenceofnetwork (video_id) and can be accessed via a uniform resource
congestion), the server behaves as if the data excess that locator (URL) at the YouTube site as well as an
cannotbetransmittedbecauseofthelimitedInternetband- embedded object in other Hypertext Markup Language
widthwereaccumulatedataserverbufferof2MB,which (HTML) pages. In the first case, the accessing URL is
is later drained as soon as the bandwidth availability is http://www.youtube.com/watch?v=<video_id>.Inthesec-
recovered.Itwasalsoidentifiedthatthevideoclipencod- ond case, the video is accessed as an embeddable object
ingrateplaysakeyroleindeterminingthedownloaddata byusingtheURLhttp://www.youtube.com/v/<video_id>.
rate.Therefore,thecumulativedensityfunction(CDF)for In both cases, the HTML code contains a customisable
alargenumberofrandomlychosenvideoclipsispresented Adobe Flash video player [8] provided by YouTube that
andlaterfittedbyananalyticalfunction. isdownloadedafterthewebbrowserparsesthepage.
On the basis of all of the conducted experiments, we The player can be fed with configuration parameters
propose a YouTube server traffic generation model. This (such as the video clip identifier, video format and other
model was validated by implementing it in a YouTube parametersexplainedinthesucceedingparagraphs).When
emulationserverandbycomparingthegeneratedsynthetic the video clip is embedded in a YouTube web page, the
traffic traces with downloads from the original YouTube player setup is encoded as JavaScript variables of the
server.Weclaimthatintheworstcase,90%ofthevideo HTML page. On the contrary, when the video is embed-
clipsgeneratedbyourmodelhavearelativeerrorthatdoes ded in any other web page, the player must obtain the
notexceed6%. proper parameters by issuing an HTTP request to the
The rest of the article is organised as follows: URL http://www.youtube.com/get_video_info?video_id=
Section 2 provides an overview of YouTube server and <video_id>toobtaintheparameterslist.Theplayermay
player operation; Section 3 provides the experimental choose to change the configuration parameters (e.g. if it
frameworkandadescriptionofthecollectedsetsoftraces; runsinfullscreenmode),butwewillconcentrate onthe
Section4presentstheanalysisoftheexperimentalresults regularcasewhentheparametersaremaintained.
ofthemaincharacteristicsofYouTubetrafficgeneration; Afterthevideoplayerhasbeenconfiguredwiththesetup
Section5providesthepseudo-codeoftheYouTubeserver parameters, it issues the HTTP request to the streaming
trafficgenerationmodelandpresentsitsexperimentalval- server,specifiedasparametersintheHTMLcode.Then,a
idation;finally,Sections6and7presenttherelatedwork progressivedownloadisperformedfromthatserver(called
andmainconclusions,respectively. themediaserverhereafter).
We have observed that the video player only issues a
single HTTP request to initiate the download and that
2. YOUTUBE OPERATION the video stream is downloaded as an HTTP response
OVERVIEW with no further client to server signalling. A new HTTP
requestisrequiredonlyiftheusersetsthepositionforthe
This section describes the operation of the YouTube ser- videoplayback.
vice. Figure 1 summarises the different functionalities of The HTTP request is sent to the URL http://<media_
thisservice,includingboththeserverandtheclient. server>.youtube.com/videoplayback of the streaming
Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd. 361
DOI:10.1002/ett
21613915,
2012,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/ett.2546
by
University
Of
Granada,
Wiley
Online
Library
on
[13/05/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 21613915, 2012, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ett.2546 by University Of Granada, Wiley Online Library on [13/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
P.Ameigeirasetal.
Figure1.OverviewoftheoperationoftheYouTubeservice.
media server along with configuration parameters. These tagspecifiestheaudiocodec(SoundFormat),samplingrate
(SoundRate) (SoundSize).
setup parameters, which control the server behaviour, and size of each sample The
are specified as query variables of the service URL. video tag includes the codec type (CodecID and Video-
Although to the authors’ knowledge, the meaning and Data).Thisinformationisessentialtodecode,renderand
syntax of the server parameters are not publicly docu- synchronisetheaudioandvideomediaaswellastosetup
mented, we have identified some of the arguments that the streaming server downloading parameters. The FLV
govern the download operation. They are summarised file includes an onMetaData tag, which can be accessed
| inTableI.        |                 |                 | fromanActionScriptprogrammeanddescribesthevideo |
| ---------------- | --------------- | --------------- | ----------------------------------------------- |
| For the majority | of non-HD video | clips, the HTTP | properties(seeTableII).                         |
response of the media server encapsulates the requested Thisinformationcanbeaccessedeasily,andthus,itis
video and the corresponding audio formatted in an FLV reasonable to believe that the media servers may use it
file[9].TheFLVfileincludestagsthatencodethecharac- tocalculate,forinstance,thetrafficgenerationrateinthe
| teristicsoftheencapsulatedmedia.Forinstance,theaudio |     |     | applicationlayer. |
| ---------------------------------------------------- | --- | --- | ----------------- |
TableI. Videorequestparametersthatcontrolprogressivedownloadperformance.
| Parameter |                                                              |     | Description |
| --------- | ------------------------------------------------------------ | --- | ----------- |
| sparams   | Thelistoftheparametersincludedintherequest,separatedbycommas |     |             |
| id        | Auniquevideoidentifiertag                                    |     |             |
algorithm Thealgorithmthatthemediaservershouldusetostreamthevideo;itisfixedtothrottle-factor
factor Speedfactor,expressedasafactorofthevideoencodingrate;itsvalueisfixedto1.25
burst Thelengthofvideothattheserverwillsendfortheinitialbufferingmeasuredinseconds;itisfixedto40s
| begin | Playbackstarttimeexpressedinmilliseconds |     |     |
| ----- | ---------------------------------------- | --- | --- |
itag Videoformatcode,equivalenttofmt(undocumentedURLparameter).FLV-basedvideoclipshaveitagsequalto
5 (low quality, 240p), 34 (normal quality, 360p) and 35 (high (non-HD) quality, 480p). See [10] for more
informationaboutthisparameter.
362 Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd.
DOI:10.1002/ett

 21613915, 2012, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ett.2546 by University Of Granada, Wiley Online Library on [13/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
P.Ameigeirasetal.
|     |     | TableII. FlashVideoparametersoftheonMetaDatatag. |     |
| --- | --- | ------------------------------------------------ | --- |
Parameter Description
|     | Duration |           | Totaldurationofthefilemeasuredinseconds        |
| --- | -------- | --------- | ---------------------------------------------- |
|     | Byte     | length    | Totalsizeofthefilemeasuredinbytes              |
|     | Total    | data rate | Jointdatabitrateinkilobitspersecond            |
|     | Video    | data rate | Videobitrateinkilobitspersecond                |
|     | Audio    | data rate | Audiobitrateinkilobitspersecond                |
|     | Frame    | rate      | Framespersecondofthemedia                      |
|     | Width,   | Height    | Widthandheightofthevideoframesmeasuredinpixels |
2.2. Playeroperation this situation occurs, the player will enter the buffering
stateuntilthereareenoughdatatocontinue,atwhichtime
AsmentionedinSection2.1,theYouTubevideoplayeris itwillentertheplayingstate.Thesestatetransitionsmay
an Adobe Flash application (in Shockwave Flash (SWF) take place several times during short periods, thus caus-
format)thatisloadedfromtheHTMLpageandobtainsits ingintermittentandconsecutivepauses.Inaddition,ifthe
parametersfromeitherJavaScriptvariablesoftheHTML player is stopped or configured not to directly play the
page or through an HTTP request. As in other streaming video when the web page is loaded, it enters the cued
clients,itstoresthevideodatainaplay-outbufferthatmit- state(i.e.thevideoiscuedandreadytoplay).Beforethe
igatesinstantaneousdegradationofthenetworkconditions playercanentertheplayingstate,acertainamountofdata
thatcouldaffecttheend-user’sperceivedvideoquality,for must be stored in the play-out buffer both at the begin-
example,causingaplaybackinterruption.Thesedegrada- ning (an initial buffering) and after a playback interrup-
tionscouldincludefluctuationsintheavailablebandwidth tion (a rebuffering event). See [12] for more information
andintheend-to-enddelay,aswellaspacketlosses.The abouttheamountofdatastoredduringarebufferingevent
playerstatesandthebufferingstrategyareexplainednext. inYouTube.
2.3. Playerstates
3. EXPERIMENTAL FRAMEWORK
| The YouTube | video player | has several states | [11] that |
| ----------- | ------------ | ------------------ | --------- |
dependonthecurrentactionbeingperformed:unstarted, In this section, we describe the experimental framework
ended, playing, paused, buffering and cued. These states used to collect traces of data traffic generated by the
arerepresentedinFigure2. YouTube media servers. The framework is composed
When the SWF player is first loaded, it enters the of a PC connected to a campus network (University
unstarted state. Then, the player starts downloading the of Granada), which in turn is connected to the Inter-
FLV file, changing its state to buffering. Once the player net through the national Academic and Research Net-
hasenoughdatainitsbuffer,theplaybackstarts(changeto work (RedIRIS [13]). During pilot tests, it has been
playingstate).Duringvideoplay-out,theusermaypause verified that neither the CPU or memory of the PC
thevideo,whichcausestheplayertogotothepausedstate. nor the network connection impeded the normal play-
Assuming that there are no congestion events, the video back of the video clips. The framework includes three
willcontinuesmoothly,endingwithoutproblemsandthe software tools installed in the PC: the Wireshark proto-
playerwillhaveenteredtheendedstate. col analyZer [14], a playback monitor and a clip sur-
However, network degradations may pause the video veyor; the last two were specifically developed for the
| playback | because of a lack | of sufficient buffered | data. If performedexperiments. |
| -------- | ----------------- | ---------------------- | ------------------------------ |
Figure2.StatediagramoftheYouTubevideoplayer.
Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd. 363
DOI:10.1002/ett

 21613915, 2012, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ett.2546 by University Of Granada, Wiley Online Library on [13/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
P.Ameigeirasetal.
3.1. Playbackmonitortool and27/02/2012tovalidatethetrafficmodelderivedfrom
|     |     |     |     |     |     |     | trace sets | T1 and | T2. All FLV-based |     | video formats | (i.e. |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ----------------- | --- | ------------- | ----- |
A playback monitor tool has been built with the objec- itagsequalto5,34and35)areconsidered.
| tiveofanalysingtheservertrafficgeneration. |     |     |     |     | Thetoolis |     |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
basedonaJavaServletandincludesawebapplicationthat (cid:2) Trace set T1: a set of 95 video clip downloads
embedstheYouTubeplayer.Thetoolconsistsoftwoparts: obtainedwiththeplaybackmonitortool.Thissethas
(1)amonitoringwebpageinwhichtheYouTubeplayeris been collected to understand the main traffic gen-
embedded and controlled using the YouTube player API eration characteristics of the YouTube server: the
[11]viaJavaScriptand(2)aJavaServletthatsequentially initial burst (Section 4.2), the throttling algorithm
readsthelistofvideostomonitorfromaconfigurationfile, (Section 4.3) and the chunk size (Section 4.4). The
launchesthewebbrowserwithourmonitoringwebpage, video clips have been downloaded with the default
requests the listed video clips and later gathers the data quality (89% with itag D34 and 11% with itag
generatedbytheplayer’sAPI. D 5), with encoding rates from 140 to 918 kbps
For every clip download, the YouTube player API (average 510 kbps) and durations from 561 to
provides—marked with a timestamp—the state of the 659 s (average 605 s). To minimise the effect of
player,theplaybacktimeandthenumberofbytesreceived network congestion, this trace set was collected
in the player buffer. This information is dumped periodi- at night. Their identifiers (VideoIDs) are available
| callyevery100ms.Moreover,thetransitionsbetweenthe |     |     |     |     |     |     | at[17]. |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
player’sstatesarealsorecordedasynchronously.Attheend (cid:2) Trace set T2: a set of 95 video clip downloads (the
ofthedownload,thedataaregatheredbytheServletand samesetofvideoclipsasinT1)butaddingbandwidth
storedinaseparatefileforpost-processing. limitations.Thissethasbeencollectedtounderstand
The launcher Servlet is configured to intentionally thecharacteristicsoftheYouTubeserverinthepres-
reduce the available bandwidth of the PC’s network con- enceofbandwidthlimitations(Section4.5).Thisset
nectionbyusingSoftPerfectBandwidthManagerLitefor has been obtained with the playback monitor tool:
Windows [15] to introduce controlled bandwidth limita- foreveryclip,twodownloadsareperformed,reduc-
tionsduringtheclipdownload. ing the available bandwidth to 50 kbps over time
|     |     |     |     |     |     |     | intervals | of     | 15 and 120       | s, respectively. | To                 | minimise |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---------------- | ---------------- | ------------------ | -------- |
|     |     |     |     |     |     |     | the       | effect | of other sources | of               | network congestion |          |
3.2. Clipsurveyortool
onthistraceset,thesemeasurementswerecollected
atnight.
| To characterise |     | the encoding | rates | of the | YouTube | video |               |         |             |           |       |          |
| --------------- | --- | ------------ | ----- | ------ | ------- | ----- | ------------- | ------- | ----------- | --------- | ----- | -------- |
|                 |     |              |       |        |         |       | (cid:2) Trace | set T3: | a set of 32 | 070 video | clips | randomly |
clips,wehavealsodevelopedaclipsurveyortoolthatcol-
|     |     |     |     |     |     |     | collected | using | the random | prefix | sampling | method |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ---------- | ------ | -------- | ------ |
lectsthelistofthemostviewedvideosforadateorrangeof
|     |     |     |     |     |     |     | presented | in  | [18] that provides |     | an unbiased | collec- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------------ | --- | ----------- | ------- |
datesanddownloadstheFLVfileheaderforeachvideoclip
|     |     |     |     |     |     |     | tion | of YouTube | video | identifiers | (videoID | parame- |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | ----- | ----------- | -------- | ------- |
withthepurposeofextractingitsmainparameters,suchas
|     |     |     |     |     |     |     | ter). | Using | this sampling | method, | 12 777 | videoIDs |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ------------- | ------- | ------ | -------- |
theencodingrate.
|     |     |     |     |     |     |     | and | their | available formats | (itag | parameter) | were |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------------- | ----- | ---------- | ---- |
BymeansoftheYouTubeDataAPI[11],thetoolgath-
obtainedbymeansofGoogleDataAPIqueries[19].
| ers a list | of video | clips. | To obtain | the FLV | file header | of  |     |     |     |     |     |     |
| ---------- | -------- | ------ | --------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Thedefaultformatswere34(FLVformat),18(MP4
| each clip,  | the clip | surveyortool | automatically |            | launches | a   |         |     |                |     |        |          |
| ----------- | -------- | ------------ | ------------- | ---------- | -------- | --- | ------- | --- | -------------- | --- | ------ | -------- |
|             |          |              |               |            |          |     | format) | and | 5 (FLV format) | for | 92.5%, | 7.3% and |
| web browser | (namely  | Firefox)     | with          | the proper | URL      | and |         |     |                |     |        |          |
0.2%oftheconsideredvideoidentifiers,respectively.
| stops the | download | after | 30 s so | that the | initial | part of |     |     |     |     |     |     |
| --------- | -------- | ----- | ------- | -------- | ------- | ------- | --- | --- | --- | --- | --- | --- |
ConcentratingontheavailableFLVformatsofthese
| the clip     | is downloaded | but        | the rest  | disregarded. | The        | tool |       |               |            |          |              |           |
| ------------ | ------------- | ---------- | --------- | ------------ | ---------- | ---- | ----- | ------------- | ---------- | -------- | ------------ | --------- |
|              |               |            |           |              |            |      | video | identifiers,  | YouTube    | provided | 12 713,      | 11 772    |
| FLVTool2     | [16]          | is used to | extract   | the FLV’s    | onMetaData |      |       |               |            |          |              |           |
|              |               |            |           |              |            |      | and   | 7585 video    | clips with | itags    | equal to     | 5, 34 and |
| information, | which         | contains   | the video | encoding     | data       | rate |       |               |            |          |              |           |
|              |               |            |           |              |            |      | 35,   | respectively, | yielding   | the      | total set of | 32 070    |
(Section2.1).
|     |     |     |     |     |     |     | video | clips. | It shall be | noticed | that none | of these |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ----------- | ------- | --------- | -------- |
videoIDhaditag6,whichwasanFLV-basedformat,
3.3. Collectedtraces but it is currently inactive. The main information of
thesevideoclipswasextractedfromthemetadataof
We only consider FLV files for clip characterisation theFLVavailablecontainers.Thesemetadatainclude
becauseitisthemostusedfileformatforvideoresolutions the audio stream and video stream encoding rates,
(morethan92%). the encoding rate of the video clip, the video clip
Two sets of data traffic traces (sets T1 and T2) have duration, the resolution (width and height) and the
beencollectedduringtheweeksbetween05/12/2010and framerateandthebytelength.The12713videoclips
07/12/2010toanalysethebehaviouroftheYouTubevideo with itag D5 (240p) had encoding rates from 38 to
servers.Thesetracesetsonlyincludethedownloadofthe 2489 kbps (average 301 kbps) and durations from 1
videoclipsintheirdefaultFLVfileformat. to11346s(average234s).The11772videoclips
Twoadditionalsetsofdatatraffictraces(setsT3andT4) with itag D34 (360p) had encoding rates from 29
havebeencollectedduringtheweeksbetween26/01/2012 to2333kbps(average527kbps)anddurationsfrom
364 Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd.
DOI:10.1002/ett

 21613915, 2012, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ett.2546 by University Of Granada, Wiley Online Library on [13/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
P.Ameigeirasetal.
1 to 9131 s (average 242 s). The 7585 video clips 4. ANALYSIS OF THE
withitagD35(480p)hadencodingratesfrom33to EXPERIMENTAL RESULTS
|     | 3230 kbps | (average 840 | kbps) and | durations from | 1   |     |     |     |     |     |
| --- | --------- | ------------ | --------- | -------------- | --- | --- | --- | --- | --- | --- |
to11 346s (average 234 s).Thesetraces have been Thissectionpresentstheexperimentalresultsobtainedto
collected with the clip surveyor tool and have been evaluate the traffic generation of the application layer of
|     | usedtocharacterisethevideoclipencodingrates(see |                  |     |                    | theYouTubeserver. |                                |     |     |     |     |
| --- | ----------------------------------------------- | ---------------- | --- | ------------------ | ----------------- | ------------------------------ | --- | --- | --- | --- |
|     | Section 4.1).                                   | More information |     | about these traces | is                |                                |     |     |     |     |
|     | availableat[20].                                |                  |     |                    | 4.1.              | Characterisationofthevideoclip |     |     |     |     |
(cid:2) Trace set T4: a set of 600 video clips has been col- encodingratesanddurations
lectedforvalidationpurposes.Thissetincludes200
videoclipsforeachoftheconsideredformats(itags As it will be described in the following subsections, the
5,34and35)usingthesamesamplingmethodasfor traffic generation rate of the media server depends on
tracesetT3.Foreachvideoclip,atracefromthereal the video clip encoding rate. Hence, we require a char-
YouTubeserverandanothertracefromacustomised acterisation of the video clip encoding rates to be able
YouTubeemulationserverhavebeenobtained.Allthe to create a model of the traffic that YouTube media
|     | tracesfromtherealYouTubeserverweredownloaded |     |     |     | serversgenerate. |     |     |     |     |     |
| --- | -------------------------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
over the campus network (University of Granada). Tostatisticallycharacterisethevarietyofencodingrates,
Additionally,theywerecollectedatnighttominimise we extracted the FLV parameters of the onMetaData tag
the effect of other sources of network congestion. from the video clips in trace set T3 and derived the his-
TheYouTubeemulationserverisdirectlyconnected togramoftheencodingrates.AsdescribedinSection3.3,
through a Local Area Network to our PC. The 200 weconcentratedontheFLV-basedvideoformats(i.e.itags
|     | videoclipswithitagD5hadencodingratesfrom62 |     |     |     | equalto5,34and35). |     |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
to 638 kbps (average 284 kbps) and durations from Because the audio and video codecs used can provide
120 to 5001 s (average 426 s). The 200 video clips different compression levels depending on the character-
withitagD34hadencodingratesfrom91to939kbps istics of the video content, YouTube clips present a wide
(average506kbps)anddurationsfrom121to5239s variety of bit rates. The encoding rates of the audio and
(average 399 s). The 200 video clips with itag D35 video streams have been collected, and their correspond-
had encoding rates from 113 to 1371 kbps (average inghistogramsareshowninFigure3.Withregardtothe
790 kbps) and durations from 120 to 4538 s (aver- audio stream, the encoding rates of video clips with itag
age 390 s). More information about these traces is equal to 5 do not exceed 64 kbps, whereas video clips
availableat[21]. with itags equal to 34 and 35 reach up to approximately
| 0.4  |          |     |     | 0.35      |     |     | 0.4  |           |     |     |
| ---- | -------- | --- | --- | --------- | --- | --- | ---- | --------- | --- | --- |
|      | itag = 5 |     |     | itag = 34 |     |     |      | itag = 35 |     |     |
| 0.35 |          |     |     | 0.3       |     |     | 0.35 |           |     |     |
| 0.3  |          |     |     |           |     |     | 0.3  |           |     |     |
0.25
| margotsiH 0.25 |     |     |     | margotsiH |     |     | margotsiH 0.25 |     |     |     |
| -------------- | --- | --- | --- | --------- | --- | --- | -------------- | --- | --- | --- |
0.2
| 0.2 |     |     |     |     |     |     | 0.2 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.15
| 0.15 |     |     |     |     |     |     | 0.15 |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
0.1
| 0.1 |     |     |     |     |     |     | 0.1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.05
| 0.05 |     |     |     |     |     |     | 0.05 |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
| 0    |     |     |     | 0   |     |     | 0    |     |     |     |
0 10 20 30 40 50 60 70 40 60 80 100 120 140 40 60 80 100 120 140
Audio Stream Encoding Rate (kbps) Audio Stream Encoding Rate (kbps) Audio Stream Encoding Rate (kbps)
| 0.45 |     |     |          | 0.14 |     |           | 0.1  |     |     |           |
| ---- | --- | --- | -------- | ---- | --- | --------- | ---- | --- | --- | --------- |
|      |     |     | itag = 5 |      |     | itag = 34 |      |     |     | itag = 35 |
| 0.4  |     |     |          |      |     |           | 0.09 |     |     |           |
0.12
0.08
0.35
|     |     |     |     | 0.1 |     |     | 0.07 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
0.3
| margotsiH |     |     |     | margotsiH |     |     | margotsiH 0.06 |     |     |     |
| --------- | --- | --- | --- | --------- | --- | --- | -------------- | --- | --- | --- |
| 0.25      |     |     |     | 0.08      |     |     |                |     |     |     |
0.05
| 0.2 |     |     |     | 0.06 |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
0.04
0.15
|      |     |     |     | 0.04 |     |     | 0.03 |     |     |     |
| ---- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
| 0.1  |     |     |     |      |     |     | 0.02 |     |     |     |
| 0.05 |     |     |     | 0.02 |     |     | 0.01 |     |     |     |
0
0 0 100 200 300 400 500 600 700 0 0 200 400 600 800 100 0 200 400 600 800 1000 1200
Video Stream Encoding Rate (kbps) Video Stream Encoding Rate (kbps) Video Stream Encoding Rate (kbps)
|     |     | a)  |     |     | b)  |     |     |     | c)  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure3.HistogramsofthevideostreamencodingratesofYouTubeclips:(a)itagD5,(b)itagD34and(c)itagD35.
Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd. 365
DOI:10.1002/ett

 21613915, 2012, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ett.2546 by University Of Granada, Wiley Online Library on [13/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
P.Ameigeirasetal.
| 128 kbps. | With regard | to  | the video stream, | the | encoding |     |     | 5   |     |
| --------- | ----------- | --- | ----------------- | --- | -------- | --- | --- | --- | --- |
P a xi
rates strongly differ with the video format. For the itags x;itag;i
iD0
|          |           |         |              |       |        |     | F .itag;x/D |     | (1)   |
| -------- | --------- | ------- | ------------ | ----- | ------ | --- | ----------- | --- | ----- |
| equal to | 5, 34 and | 35, 99% | of the video | clips | have a |     | X           | 4   |       |
|          |           |         |              |       |        |     |             | P   | x‘jC1 |
videostreamencodingratebelow500,810and1300kbps, 1C b x;itag;j
| respectively. |     |     |     |     |     |     |     | jD0 |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Forthepurposeofstatisticalcharacterisation,theCDF
|              |            |          |         |           |        | where | x is the corresponding | measurement, | that is, the |
| ------------ | ---------- | -------- | ------- | --------- | ------ | ----- | ---------------------- | ------------ | ------------ |
| of the total | video clip | encoding | rate Vr | (i.e. the | sum of |       |                        |              |              |
the audio and video streams) and the CDF of the video video clip encoding rate vr or the video clip duration
|                                                     |                                     |                 |           |          |          | d, itag  | is 5, 34 or 35, and               | the corresponding | coefficients |
| --------------------------------------------------- | ----------------------------------- | --------------- | --------- | -------- | -------- | -------- | --------------------------------- | ----------------- | ------------ |
| clipdurationd                                       | havebeencomputedandarerepresentedin |                 |           |          |          |          |                                   |                   |              |
|                                                     |                                     |                 |           |          |          | (a       | andb x;itag;j)areshowninTableIII. |                   |              |
| Figure 4.                                           | The obtained                        | CDFs            | have been | fitted   | with the | x;itag;i |                                   |                   |              |
| objective                                           | of providing                        | analytical      | functions | that     | can be   |          |                                   |                   |              |
| implementedinsimulationtools.Thederivedfittingfunc- |                                     |                 |           |          |          | 4.2.     | Initialburst                      |                   |              |
| tions, F                                            | and F                               | , are presented | in        | Equation | (1) and  |          |                                   |                   |              |
| V                                                   | D                                   |                 |           |          |          |          |                                   |                   |              |
graphicallydepictedinFigure4.Pleasenotethattheval- In this subsection, we investigate the operation of the
ues obtained from the fitting functions shall be bounded YouTube server during the initial seconds of a progres-
between 0 and 1, so the expressions for F and F sivedownload. Onthebasisofthisinformationprovided
V D
are valid if vr is lower than 650 930 and 2200 kbps by the Playback Monitor Tool, we depict the progres-
for itags 5, 34 and 35, respectively, and d is lower sive download of two FLV video clips, which belong to
than5000s. trace set T1, as an example. Figure 5 (a) plots the time
| FDC |     |     |     |     |     | FDC |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CDF (itag = 5)
F (itag = 5)
v
CDF (itag = 34)
F (itag = 34)
v
|     |                                 |     |     | CDF (itag = 35) |     |     |              |     | CDF |
| --- | ------------------------------- | --- | --- | --------------- | --- | --- | ------------ | --- | --- |
|     |                                 |     |     | F (itag = 35)   |     |     |              |     | F   |
|     |                                 |     |     | v               |     |     |              |     | D   |
|     | Video Clip Encoding Rate (kbps) |     |     |                 |     |     | Duration (s) |     |     |
|     |                                 |     | a)  |                 |     |     |              | b)  |     |
Figure 4.Cumulative density functions (CDFs) of (a) the video clip encoding rates, (b) their durations and their corresponding
curvefitting.
TableIII. Coefficientsforthecurvefittingofthecumulativedensityfunctionsofthevideoclipencoding
ratesandtheirdurations.
|     |              |     |                        |     | xDv r (encodingrate)   |     |                        | xDd(duration)          |     |
| --- | ------------ | --- | ---------------------- | --- | ---------------------- | --- | ---------------------- | ---------------------- | --- |
|     | Coefficients |     | itagD5                 |     | itagD34                |     | itagD35                | allitags               |     |
|     | a            |     | 6.624(cid:3)10(cid:2)3 |     | 2.764(cid:3)10(cid:2)3 |     | 5.109(cid:3)10(cid:2)3 | 5.813(cid:3)10(cid:2)2 |     |
x;itag;0
|     |     |     | (cid:4)5.530(cid:3)10(cid:2)4 |     | (cid:4)9.136(cid:3)10(cid:2)5 |     | (cid:4)1.470(cid:3)10(cid:2)4 | 2.747(cid:3)10(cid:2)3 |     |
| --- | --- | --- | ----------------------------- | --- | ----------------------------- | --- | ----------------------------- | ---------------------- | --- |
a x;itag;1
|     | a x;itag;2 |     | 9.850(cid:3)10(cid:2)6        |     | 9.675(cid:3)10(cid:2)7         |     | 1.057(cid:3)10(cid:2)6        | 2.082(cid:3)10(cid:2)5 |     |
| --- | ---------- | --- | ----------------------------- | --- | ------------------------------ | --- | ----------------------------- | ---------------------- | --- |
|     | a x;itag;3 |     | (cid:4)5.013(cid:3)10(cid:2)8 |     | 1.818(cid:3)10(cid:2)9         |     | (cid:4)1.422(cid:3)10(cid:2)9 | 0                      |     |
|     | a          |     | 7.926(cid:3)10(cid:2)11       |     | (cid:4)7.457(cid:3)10(cid:2)12 |     | 5.517(cid:3)10(cid:2)13       | 0                      |     |
x;itag;4
|     | a   |     | 0   |     | 4.935(cid:3)10(cid:2)15 |     | 0   | 0   |     |
| --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
x;itag;5
|     | b   |     | (cid:4)8.908(cid:3)10(cid:2)3 |     | (cid:4)3.628(cid:3)10(cid:2)3 |     | (cid:4)2.607(cid:3)10(cid:2)3 | 2.318(cid:3)10(cid:2)3 |     |
| --- | --- | --- | ----------------------------- | --- | ----------------------------- | --- | ----------------------------- | ---------------------- | --- |
x;itag;0
|     | b   |     | 3.579(cid:3)10(cid:2)5 |     | 5.834(cid:3)10(cid:2)6 |     | 3.423(cid:3)10(cid:2)6 | 2.088(cid:3)10(cid:2)5 |     |
| --- | --- | --- | ---------------------- | --- | ---------------------- | --- | ---------------------- | ---------------------- | --- |
x;itag;1
|     | b   |     | (cid:4)8.515(cid:3)10(cid:2)8 |     | (cid:4)1.431(cid:3)10(cid:2)9 |     | (cid:4)2.527(cid:3)10(cid:2)9 | 0   |     |
| --- | --- | --- | ----------------------------- | --- | ----------------------------- | --- | ----------------------------- | --- | --- |
x;itag;2
|     | b   |     | 9.670(cid:3)10(cid:2)11 |     | (cid:4)6.398(cid:3)10(cid:2)12 |     | 8.037(cid:3)10(cid:2)13 | 0   |     |
| --- | --- | --- | ----------------------- | --- | ------------------------------ | --- | ----------------------- | --- | --- |
x;itag;3
|     | b   |     | 0   |     | 4.797(cid:3)10(cid:2)15 |     | (cid:4)2.273(cid:3)10(cid:2)17 | 0   |     |
| --- | --- | --- | --- | --- | ----------------------- | --- | ------------------------------ | --- | --- |
x;itag;4
366 Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd.
DOI:10.1002/ett

 21613915, 2012, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ett.2546 by University Of Granada, Wiley Online Library on [13/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
P.Ameigeirasetal.
60
Endof Download
|                                |            Received KBytes at Player |     |                           | 16              |     |     |
| ------------------------------ | ------------------------------------ | --- | ------------------------- | --------------- | --- | --- |
| INITIALBURST                   |            (Bin size = 10ms)         |     |                           | (133s,16.56 MB) |     |     |
| )setyBK( ataD suoenatnatsnI 50 |                                      |     | )setyBM( ataD detalumuccA | 14              |     |     |
12
| 40  |     |     |     | ThrottlingPhase |     |     |
| --- | --- | --- | --- | --------------- | --- | --- |
Endof Playback
10
(201.5s,16.56MB)
30
8
THROTTLING
6
| 20  |     |     |     |     | Endof InitialBurst |               |
| --- | --- | --- | --- | --- | ------------------ | ------------- |
|     |     |     |     | 4   |                    | (5.5s,3.27MB) |
10
|     |            |       |        | 2   | Startof Playback | Received at Player      |
| --- | ---------- | ----- | ------ | --- | ---------------- | ----------------------- |
|     |            |       |        |     | (1.5s,0 MB)      | Reproduced by Player    |
| 0   |            |       |        | 0   |                  |                         |
| 0 1 | 2 3 4      | 5 6 7 | 8 9 10 | 0   | 20 40 60 80      | 100 120 140 160 180 200 |
|     | Time (sec) |       |        |     | Time (sec)       |                         |
|     |            | a)    |        |     |                  | b)                      |
Figure5.Examplesoftimeevolutionofthe(a)instantaneousand(b)accumulatedreceiveddataattheplayerbuffer.
evolutionoftheinstantaneousamountofdatareceivedby fluctuations of the network bandwidth hindered the iden-
theplayeratthebeginningofthedownload.Additionally, tification of the slope change. To mitigate this effect, the
Figure5(b)depictsthetimeevolutionoftheaccumulated accumulateddatahavebeenfilteredwitha500-mssimple
amountofdatareceivedintheplayer’sbufferandtheaccu- movingaverage(a400-msperiodhasalsobeenusedand
mulated amount of data reproduced by the player during producednearlyidenticalresults).Aslopeapproximation
theentire download. Thenumber ofbytes reproduced by sequence is computed as the difference between consec-
theplayerwasestimatedonthebasisoftheplaybacktime utive samples of the filtered series. Then, the maximum
informationandthevideoclipencodingrate. slopeaftertheinitialburst(i.e.duringthethrottlingphase)
As shown in Figure 5, the video clip download com- iscomputedbyconsideringonlythelast20softhetrace.
mences with a significant burst of data. After this initial Theobservedendoftheinitialburstismeasuredasthe
burst,thereceivingdatarateoftheclient’splayeriscon- lastinstantofthetracewhentwoconsecutivesamplesof
siderably reduced. This effect can be clearly observed in the slope approximation sequence surpass the maximum
Figure5(a),whereitcanbeseenthatduringtheinitialfew slopeofthethrottlingphase.TableIVdepictstheCDFof
seconds,theamountofdatareceivedattheplayerissig- theamountofdata(measuredinsecondsofvideodata,i.e.
nificantandlaterreduced;itcanalsobeclearlyobserved bydividingtheamountofdatabythevideoclipencoding
inFigure5(b)bythechangeintheslopeoftheaccumu- rate)downloadeduntiltheobservedendoftheinitialburst
lateddatareceivedattheplayerafteraninitialfewseconds. foralldownloadsoftracesetT1.Theresultsshowthatthe
Graphicalrepresentationsofotherdownloadexamplesof majority of the measured sizes amount to approximately
tracesetT1arenotincludedhere,buttheyalsoexhibitthe 40sofvideodata.Fortheremainingdownloads,theempir-
rapiddownloadofaninitialburstofdataduringthebegin- icalmeasurementsoftheirinitialburstsslightlydifferfrom
ningofthedownload.Theauthorsin[7,22]and[23]also 40s,whichiscausedbyshortfluctuationsinthenetwork’s
observedthattheYouTubeserversendsthevideoasfastas available bandwidth that affect the empirical estimation.
possibleforaninitialbufferingperiodbeforesettlinginto However, during the validation process, we detected that
aconstantsendingrate. for the videos with encoding rates lower than 200 kbps,
To extend the previous analysis to a large set of video theamountofdownloaded dataduringtheinitialburstis
clip downloads, all downloads of trace set T1 have been approximatelyequalto40smultipliedby200kbps.
post-processed in search of an initial burst. This initial FromTableIV,weconcludethatinthecaseofYouTube,
burst is identified in each trace by determining the slope thereexistsaninitialburstwithasizeequivalentto40sof
change in the accumulated data received by the player video content, that is, a total amount of data equal to 40
between the initial burst and the subsequent phase (here- multipliedbythevideoclipencodingrateassumingamin-
after referred to as throttling phase). The instantaneous imum encoding rate of 200 kbps. It should be noted that
| TableIV.                 | Cumulativedensityfunctionoftheinitialburstsizemeasuredinsecondsofvideodata. |         |          |           |                |          |
| ------------------------ | --------------------------------------------------------------------------- | ------- | -------- | --------- | -------------- | -------- |
| Sizeoftheinitialburst(s) |                                                                             | 37 38   | 39 40    | 41 42     | 43 44          | 45 46 47 |
| Cumulativeprobability(%) |                                                                             | 1.2 1.2 | 3.6 69.9 | 89.2 91.6 | 94.0 97.6 97.6 | 98.8 100 |
Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd. 367
DOI:10.1002/ett

 21613915, 2012, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ett.2546 by University Of Granada, Wiley Online Library on [13/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
P.Ameigeirasetal.
thesetupparameterburstsenttotheHTTPrequestbythe 8(cid:3)s(cid:4)40(cid:3)Vr
|                                         |        |             |       |        |         |     | t   | Dt ib C |     |     |     | (2) |
| --------------------------------------- | ------ | ----------- | ----- | ------ | ------- | --- | --- | ------- | --- | --- | --- | --- |
| YouTubeclientissetto40s(seeSection2.1). |        |             |       |        |         |     | d   |         | Tr  |     |     |     |
| The operation                           | of the | application | layer | of the | YouTube |     |     |         |     |     |     |     |
wheret ib isavariablethatrepresentsthetimerequiredto
| server at | the beginning | of the   | download | presented | in         |          |             |        |          |           |          |     |
| --------- | ------------- | -------- | -------- | --------- | ---------- | -------- | ----------- | ------ | -------- | --------- | -------- | --- |
|           |               |          |          |           |            | download | the initial | burst, | s is the | file size | measured | in  |
| Figure 5  | resembles the | Advanced | Fast     | Start     | of Windows |          |             |        |          |           |          |     |
bytes,Vr isthevideoclipencodingratemeasuredinbps
MediaServices[24],whichsendsthefirstfewsecondsof
andTr isthetransmissiondataratemeasuredinbps.Let
dataatthemaximumavailablebandwidthoftheInternet.
Theobjective ofthisinitial burstistoinject a significant usfurtherassumethatTr D1:25(cid:3)Vr duringthethrottling
phase.Then,
amountofdataintheplayer’sbuffer.Thisstrategyaimsto
improvethequalityperceivedbytheend-usersbeyondthat
|     |     |     |     |     |     |     | 8(cid:3)s(cid:4)40(cid:3)Vr |     |     | 1   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
o f t r a di t io n a l str ea m i ng w i th n o i n i t i al b u rs t, in w hichthe t Dt C Dt C .d(cid:4)40/ (3)
|                          |                       |            |              |             |      | d                       | ib 1:25(cid:3)Vr |               | ib        | 1:25   |            |        |
| ------------------------ | --------------------- | ---------- | ------------ | ----------- | ---- | ----------------------- | ---------------- | ------------- | --------- | ------ | ---------- | ------ |
| p la y e r a w           | a i ts a lo n ge r in | iti a lb u | ff e r i n g | d e la y [2 | 5] . |                         |                  |               |           |        |            |        |
|                          |                       |            |              |             |      | where d                 | represents       | the duration  |           | of the | video clip | mea-   |
|                          |                       |            |              |             |      | sured in seconds        |                  | (see duration | parameter |        | available  | in the |
| 4.3. Throttlingalgorithm |                       |            |              |             |      | onMetaDatataginTableI). |                  |               |           |        |            |        |
Foreachvideoclip,Figure6depictsthetotaldownload
| We continue | our discussion   | of  | the experimental |     | analysis     |             |                 |      |           |          |        |        |
| ----------- | ---------------- | --- | ---------------- | --- | ------------ | ----------- | --------------- | ---- | --------- | -------- | ------ | ------ |
|             |                  |     |                  |     |              | time versus | the video       | clip | duration. | Figure   | 6 also | repre- |
| by focusing | on the operation | of  | the YouTube      |     | server after |             |                 |      |           |          |        |        |
|             |                  |     |                  |     |              | sents the   | linear equation | (3), | although  | assuming |        | t D 0. |
ib
theinitialsecondsofaprogressivedownload.Asshownin Fromthefigure,itcanbeseenthatthetotaldownloadtime
Figure5(b),aftertheinitialburst,theslopeoftheaccumu- closely approximates the represented linear equation for
latedreceiveddataattheplayerwasreducedbecauseofa
|     |     |     |     |     |     | video clips | longer | than 40 | s and | that a small | increase | is  |
| --- | --- | --- | --- | --- | --- | ----------- | ------ | ------- | ----- | ------------ | -------- | --- |
decreaseinthereceivingdatarate.Letusfurtheranalyse
|               |          |        |             |      |           | observed | because | of the variable |     | t ib > 0. | Again, | during |
| ------------- | -------- | ------ | ----------- | ---- | --------- | -------- | ------- | --------------- | --- | --------- | ------ | ------ |
| this download | example. | Figure | 5 (b) shows | that | after the |          |         |                 |     |           |        |        |
thevalidationprocess,wedetectedthatforthevideoswith
initialburst,theslopeoftheamountofdatareceivedinthe encodingrateslowerthan200kbps,thetransmissiondata
player’sbufferwithrespecttotime(i.e.thereceivingdata rateduring thethrottlingphase isapproximately equal to
| rate) remains | approximately | constant |     | until the | download |     |     |     |     |     |     |     |
| ------------- | ------------- | -------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
250kbps(i.e.1.25multipliedby200kbps).
| is completed. | This suggests | that | the | application | layer in |            |          |        |              |     |      |           |
| ------------- | ------------- | ---- | --- | ----------- | -------- | ---------- | -------- | ------ | ------------ | --- | ---- | --------- |
|               |               |      |     |             |          | From these | results, | it can | be concluded |     | that | after the |
theserverthrottlesdownthetrafficgenerationrate,thereby
initialburst,themediaserverthrottlesdownthetrafficgen-
establishingaconstantlimitontherateatwhichthedata eration rate, thereby avoiding transferring the data at the
are fed to the TCP stack during this phase. This throt- maximumavailablebandwidth.Theserversendsinforma-
tlingeffectincreasesthetotaltimerequiredtocompletethe
|     |     |     |     |     |     | tion at a | constant | bit rate, | and a throttling |     | algorithm | (see |
| --- | --- | --- | --- | --- | --- | --------- | -------- | --------- | ---------------- | --- | --------- | ---- |
filedownload.
|       |                    |      |          |     |            | parameteralgorithm=throttle-factor |     |     |     | inTableI)isapplied |     |     |
| ----- | ------------------ | ---- | -------- | --- | ---------- | ---------------------------------- | --- | --- | --- | ------------------ | --- | --- |
| Based | on the accumulated | data | received | by  | the player |                                    |     |     |     |                    |     |     |
thatshapesthetrafficgenerationrateaccordingtoathrottle
andassuminganapproximatelyconstanttransmissiondata
factormultipliedbythevideoclipencodingrateassuming
rate during the throttling phase, it is possible to make aminimumencodingrateof200kbps.Theso-calledthrot-
a simple estimation of the transmission data rate on tlefactor(seesetupparameterfactorinTableI)isequalto
| the basis | of Figure 5 (b): | Tr  | D (16.56–3.27 |     | MB)/(133– |     |     |     |     |     |     |     |
| --------- | ---------------- | --- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
1.25.Theseresultsareinagreementwith[7,22]and[23].
| 5.5 s)(cid:2)875                        | kbps, where        | Tr is      | the transmission |              | data rate. |                 |        |           |             |      |          |       |
| --------------------------------------- | ------------------ | ---------- | ---------------- | ------------ | ---------- | --------------- | ------ | --------- | ----------- | ---- | -------- | ----- |
|                                         |                    |            |                  |              |            | This throttling |        | procedure | is also     | used | in other | plat- |
| Additionally,thevideoclipencodingrateVr |                    |            |                  |              | D696kbps   |                 |        |           |             |      |          |       |
|                                         |                    |            |                  |              |            | forms such      | as the | Internet  | Information |      | Services | Media |
| is obtained                             | from the FLV’s     | onMetaData |                  | information  | (see       |                 |        |           |             |      |          |       |
| Section                                 | 2.1). Note that    | Vr could   | also             | be estimated | on         |                 |        |           |             |      |          |       |
| the basis                               | of the accumulated |            | data             | reproduced   | by the     |                 |        |           |             |      |          |       |
250
| player from | Figure 5 (b) | as Vr | D .16:56 | MB//(201.5– |     |     | download time |     |     |     |     |     |
| ----------- | ------------ | ----- | -------- | ----------- | --- | --- | ------------- | --- | --- | --- | --- | --- |
t=(d-40)/1.25
| 1.5 s)(cid:2)695 | kbps. Thus, | it is | interesting | to  | observe that |     |     |     |     |     |     |     |
| ---------------- | ----------- | ----- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
)sdnoces( emit daolnwoD
200
| duringthethrottlingphase,theratioTr=Vr |                  |        |             | D   | 1:256that   |     |     |     |     |     |     |     |
| -------------------------------------- | ---------------- | ------ | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| indicates                              | that during this | phase, | the YouTube |     | server pro- |     |     |     |     |     |     |     |
gressivelydownloadsthevideoclipfileatapaceapprox-
150
| imately 25% | faster than              | it is | reproduced | by             | the player. |     |     |     |     |     |     |     |
| ----------- | ------------------------ | ----- | ---------- | -------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| Again, a    | graphical representation |       | of         | other examples | of          |     |     |     |     |     |     |     |
100
downloadsoftracesetT1alsopresentsathrottlingphase
andasimilarfactorTr=Vr.
Toverifytheapplicationofthethrottlingperformedby
50
theYouTubeserver,allvideoclipdownloadsoftraceset
T1werealsopost-processedtoobtainthemeasureddown-
0
load times. Let t d denote the total time to download a 0 50 100 150 200 250 300 350
video clip measured in seconds. Then, assuming that the Duration time (seconds)
transmissiondatarateisapproximatelyconstantduringthe
throttlingphase,t canbeexpressedas Figure6.Samplesofvideoclipdurationanddownloadtime.
d
368 Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd.
DOI:10.1002/ett

P.Ameigeirasetal.
Services delivery platform. It saves bandwidth of media ToverifythischaracteristicoftheYouTubeserver,again
filesthatmightnotbeplayedtotheend[26].Additionally, all video clip downloads of trace set T1 were also post-
it prevents congestion both at the server and the network processed.Inthiscase,weusetheWireSharkinformation
becausethedatatransferisnotperformedattheInternet’s tocollectthetimeinstantsatwhichthepacketsarrivedat
maximumavailablebandwidth. theclientcomputer.Post-processingeliminatestheinitial
burstsofeachdownload.Additionally,thepost-processing
groupspacketsintochunkssothattwoconsecutivepack-
ets belong to the same chunk if the difference between
4.4. Chunksize
their arrival times does not exceed a given time thresh-
old.Ifthedifferenceislongerthanthetimethreshold,the
This section analyses another characteristic of the traf-
two consecutive packets are assumed to belong to differ-
fic generated by the YouTube server: during the throt-
ent chunks. Thus, the size of a chunk can be calculated
tling phase, the traffic is generated in chunks of a
simply by aggregating the size of the payloads of all of
specificsize.
itsTCPpackets.Thetimethresholdusedtodecideiftwo
Figure5(a)showsthedatareceivedinstantaneouslyat
consecutivepacketsbelongtothesamechunkisselected
theplayerduringtheinitialsecondsofanexampledown-
to be 200 ms. The selection of this period is based on
load.Thefigureshowsthatduringthethrottlingphase,the
Figure7(b)inwhichthetimebetweentheendoftherecep-
pattern of reception of data alternates between the recep-
tion of a chunk and the beginning of the next does not
tion of data chunks and short periods without packets.
exceed 200 ms, and only 1% of the analysed video clips
To further analyse this characteristic, the instantaneously
haveanencodingratelargerthan1Mbps(roughlysimilar
received data of two additional download examples are
totheoneusedforFigure7(b)).
depictedinFigure7.Thefiguresonlyrepresentashorttime
Fromtheempiricallymeasuredchunksizes,weobserve
spanofthethrottlingphaseduringthedownload.Thevideo
thatthemajority(96.86%)ofthemeasuredchunksizesare
clipencodingratesoftheselectedexamplesare135kbps equal to 64 KB. Marginally, chunk sizes in multiples of
and1.089Mbps,whichareclosetothelowerandtheupper
64KB(e.g.128and192KB)werealsofoundbecauseof
limits of the video clip encoding rates, respectively (see
delayfluctuationsinthenetworkthataffecttheempirical
Section4.1).Thefigureclearlyshowsthatinbothdown-
estimation.Inparticular,just0.97%ofthechunksizeshave
loads,thedataarereceivedinchunkswithanearlyconstant
128KB,whereasnoneoftheothersizesexceedthe0.3%.
period.Furtheranalysisofthesetwoexamplesrevealsthat
Theseresultsareinagreementwith[22]and[23]thatalso
theaggregatepayloadoftheTCPpacketsgroupedineach
foundthatchunksaretypically64KBinsize.
chunk is exactly equal to 64 KB. Moreover, the period
betweenchunksisapproximately64KB/(1.25(cid:3)Vr/,thatis,
64 KB divided by the transmission data rate during the 4.5. Effectsofavailable
throttling phase. This characteristic of the traffic genera- bandwidthreduction
tioncanbeeasilyrecognisedwhenanalyzingashorttime
spanduringthethrottlingphase,asinFigure7.However, One of the most relevant factors that may impact the
itcannotbeidentifiedduringtheinitialburst. performance quality of the YouTube service is the effect
20
18
16
14
12
10
8
6
4
2
0
26 27 28 29 30 31 32 33 34 35
Time (sec)
)setyBK(
ataD
suoenatnatsnI
20
Received KBytesat Player 18
(Bin size = 10ms) 64KB CHUNK
16
14
12
10
8
6
4
2
0
28 28.5 29 29.5 30 30.5 31
2.1 s Time (sec)
)setybK(
ataD
suoenatnatsnI
Received KBytesat Player
64KB CHUNK (Bin size = 10ms)
380 ms
a) b)
Figure7.Anexampleoftimeevolutionoftheinstantaneouslyreceiveddataattheplayerbufferforvideoclipswithencodingrates
of(a)135kbpsand(b)1.089Mbps.
Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd. 369
DOI:10.1002/ett
21613915,
2012,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/ett.2546
by
University
Of
Granada,
Wiley
Online
Library
on
[13/05/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 21613915, 2012, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ett.2546 by University Of Granada, Wiley Online Library on [13/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
P.Ameigeirasetal.
| of network | congestion | because |     | it can potentially |     | cause |     |     |     |     |     |     |
| ---------- | ---------- | ------- | --- | ------------------ | --- | ----- | --- | --- | --- | --- | --- | --- |
Received at Player
| a rebuffering | event, | which | ultimately | degrades |     | the video | 25  |     |     |     |     |     |
| ------------- | ------ | ----- | ---------- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- |
Reproduced by Player
|     |     |     |     |     |     |     | )setyBM( ataD detalumuccA | Stored at Player´s Buffer |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | ------------------------- | --- | --- | --- | --- |
qualityperceivedbytheend-user.Letusassumethatacon-
|                 |              |             |       |               |            |     | THROTTLING |     |     | CONGESTION |     |     |
| --------------- | ------------ | ----------- | ----- | ------------- | ---------- | --- | ---------- | --- | --- | ---------- | --- | --- |
| gestion episode |              | takes place | at a  | given instant | during     | the | 20         |     |     |            |     |     |
| download        | of a YouTube | video       | clip. | Network       | congestion |     |            |     |     |            |     |     |
hasseveralperniciouseffectsonthisflow[27]:
15
| (cid:2) Increase | in      | the probability | of      | discarding | a        | packet at |     |     |     |     |     |     |
| ---------------- | ------- | --------------- | ------- | ---------- | -------- | --------- | --- | --- | --- | --- | --- | --- |
| the              | network | nodes.          | For the | YouTube    | service, | this      | 10  |     |     |     |     |     |
Rebuffering
effectismitigatedbytheretransmissioncapabilityof
| TCP,althoughretransmissionimpliesalongertrans- |        |               |     |        |            |      | 5   |     |     |     |     |     |
| ---------------------------------------------- | ------ | ------------- | --- | ------ | ---------- | ---- | --- | --- | --- | --- | --- | --- |
| mission                                        | delay. | Additionally, |     | packet | discarding | also |     |     |     |     |     |     |
reducesthetransmissiondatarateattheTCPlayer.
0
| Longer                                 | queuing | delay  | at the      | network       | nodes | and,     |     |        |     |            |     |         |
| -------------------------------------- | ------- | ------ | ----------- | ------------- | ----- | -------- | --- | ------ | --- | ---------- | --- | ------- |
| (cid:2)                                |         |        |             |               |       |          | 0   | 50 100 | 150 | 200 250    | 300 | 350 400 |
| therefore,anincreaseinend-to-enddelay. |         |        |             |               |       | However, |     |        |     | Time (sec) |     |         |
| for                                    | YouTube | flows, | this effect | is alleviated |       | by the   |     |        |     |            |     |         |
amount of data stored by the player’s buffer during Figure8.Theeffectofnetworkcongestionontheplayback.
theinitialburst.
| Reduction |     | in the transmission |     | data | rate in | the TCP |     |     |     |     |     |     |
| --------- | --- | ------------------- | --- | ---- | ------- | ------- | --- | --- | --- | --- | --- | --- |
(cid:2)
|        |       |         |        |               |     |           | amount of | data stored | in  | the player’s | buffer | approaches |
| ------ | ----- | ------- | ------ | ------------- | --- | --------- | --------- | ----------- | --- | ------------ | ------ | ---------- |
| layer, | which | in turn | limits | the bandwidth |     | available |           |             |     |              |        |            |
fortheapplication.Ifthenetworkcongestionepisode zero at approximately 215 s, leading to the rebuffering
is long enough, this effect can lead to a rebuffering event.Fromthefigure,itcanalsobeconcludedthatacon-
| event. |     |     |     |     |     |     | gestionepisodeismorelikelytocausearebufferingevent |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
ifitoccursduringtheearlystagesofthedownloadbecause
Ofalloftheeffectsofnetworkcongestion,thepresent therearefewerdatastoredintheplayer’sbuffer.
sectionconcentratesontheinfluenceofthereductioninthe
availablebandwidthcausedbyalongcongestionepisode 4.5.2. Serverresponsetoanetwork
| ontheoperationofthetransmittingandreceivingentities |     |     |     |     |     |     | congestionepisode. |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
oftheYouTubeapplicationlayer.
|          |       |           |               |           |     |       | A network  | congestion   |     | episode may  | not   | only affect the |
| -------- | ----- | --------- | ------------- | --------- | --- | ----- | ---------- | ------------ | --- | ------------ | ----- | --------------- |
| Although | it is | true that | the available | bandwidth |     | drops |            |              |     |              |       |                 |
|          |       |           |               |           |     |       | player and | the playback |     | of the video | clip, | but as it will  |
inthepresenceofnetworkcongestion,itdoesnotdropat be described in this section, it may also affect the traffic
a constant value. However, to conduct controlled experi- generationrateoftheserver’sapplicationlayer.
ments,thebandwidthwillbelimitedtoafixedvalueinthe Toanalysethisresponse,theplaybackmonitortoolpre-
testsdiscussedinthefollowingsubsections. sented in Section 3.1 has been used to download a video
|     |     |     |     |     |     |     | clip in which | the | bandwidth | of the | network | connection |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ------ | ------- | ---------- |
4.5.1. Theinfluenceofnetworkcongestion ofourhostmachinewasintentionallyreducedto50kbps
episodesontheplayback. during a given time interval. Two time intervals are con-
Duringacongestionepisode,thetransmissiondatarate sidered: 15 and 120 s. The selection of these congestion
intheTCPlayeris reduced. Ifthisrateislowerthan the durations is intentionally chosen to manifest the desired
play-outrate,theplayerdrainsdatafromthebuffermore effect. The selected video clip has an encoding rate of
rapidly than it is received from the Internet, and there- 684kbps.Theexperimenthasbeenrepeatedfivetimesfor
fore,theamountofdatastoredintheplayer’sbufferstarts eachtimeinterval.Theresultsobtainedafterprocessingthe
decreasing. An example of this situation is depicted in correspondingtracesarepresentedinFigure9.
Figure8,whereitcanbeseenthatatapproximately150s, InthefivedownloadsrepresentedinFigure9(a),itcan
theplayerstartsreceivingdatamoreslowlybecauseofan beseenthataftertherecoveryphase(attimeinstant58s
episode of network congestion; therefore, the amount of andbeyond),theamountofdatareceivedbytheplayeris
datastoredintheplayer’sbufferbeginstodecrease. the same as if there had been no congestion episode. On
Under this circumstance, two possible cases can be thecontrary,innoneofthefivedownloadsrepresentedin
envisaged:(i)thenetworkcongestionepisodeisshort,and Figure9(b)doestheamountofdatareceivedattheplayer
thebandwidthavailabilityisrecoveredbeforecompletely reachavaluethatwouldsuggestthatnocongestionepisode
| emptying | the player’s | buffer; | in  | this case, | the | rebuffer- | hadoccurred. |     |     |     |     |     |
| -------- | ------------ | ------- | --- | ---------- | --- | --------- | ------------ | --- | --- | --- | --- | --- |
ingeventisavoidedand(ii)thenetworkcongestionlasts InthedownloadexamplesshowninFigure9(a)and(b),
long enough so that the player’s buffer eventually runs theYouTubeserveractsasiftheamountofdatathatcould
out of data; in this case, the play-out is paused, and the notbetransmittedduringthenetworkcongestionepisode
player starts rebuffering the data. Video clip playback is wasstoredinabuffer.Whentheepisodeended,theserver’s
stoppedfortheamountoftimerequiredtoaccumulatesuf- application layer released the data stored in the buffer at
ficient data to resume the play-out. This situation is also the available bandwidth, which explains the rapid down-
represented in Figure 8, where it can be seen that the loadduringtherecoveryphase.FromFigure9(a),itcanbe
370 Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd.
DOI:10.1002/ett

 21613915, 2012, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ett.2546 by University Of Granada, Wiley Online Library on [13/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
P.Ameigeirasetal.
|     | 10  |     |     |     |     |     |     | 22  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Received at Player if No Congestion Had Occurred Received at Player if No Congestion Had Occurred
9.5 Received at Player,Downloads 1-5 20 Received at Player,Downloads 1-5
| )setyBM( ataD detalumuccA |     |     |     |     |     |     | )setyBM( ataD detalumuccA |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- |
|                           | 9   |     |     |     |     |     |                           | 18  |     |     |     |
|                           | 8.5 |     |     |     |     |     |                           | 16  |     |     |     |
S min
|     | 8   |     |     |     |     |     |     | 14  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 7.5 |     |     |     |     |     |     | 12  |     |     |     |
S
|     | 7   |     |     |     |       |       |     | 10    |        | max     |         |
| --- | --- | --- | --- | --- | ----- | ----- | --- | ----- | ------ | ------- | ------- |
|     | 6.5 |     |     |     |       |       |     | 8     |        |         |         |
|     | 6   |     |     |     |       |       |     | 6     |        |         |         |
|     | 30  | 35  | 40  | 45  | 50 55 | 60 65 |     | 40 60 | 80 100 | 120 140 | 160 180 |
Time (sec)
Time (sec)
|     |     |     |     | a)  |     |     |     |     |     | b)  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure9.Fivevideoclipdownloadswithacongestionepisodelasting(a)15and(b)120s.
inferredthatthebufferiscontinuouslyfed(evenduringthe
congestionepisode)attherateindicatedbythethrottling
| algorithm,     |           | which   | explains             | why after | the recovery     | phase,      |     |     |     |     |     |
| -------------- | --------- | ------- | -------------------- | --------- | ---------------- | ----------- | --- | --- | --- | --- | --- |
| the            | amount    | of data | received             | by the    | player is        | the same as |     |     |     |     |     |
| iftherehadbeen |           |         | nocongestionepisode. |           | However,         | inthe       |     |     |     |     |     |
| case           | of Figure | 9       | (b), the amount      |           | of data received | by the      |     |     |     |     |     |
playerdoesnotreachthevaluethatsuggestsnocongestion
| episode | had  | occurred. | This   | might      | be caused | by a limited |     |     |     |     |     |
| ------- | ---- | --------- | ------ | ---------- | --------- | ------------ | --- | --- | --- | --- | --- |
| buffer  | size | such that | if the | congestion | episode   | lasts long   |     |     |     |     |     |
enough,thebufferisfilledup,andthefillingprocedureis
blocked.Asaconsequence,inthecaseofFigure9(b),the
timerequiredtocompletethedownloadofthevideoclipis
observedtohaveincreased.
|       | To verify  | the behaviour |          | described | previously, | the pre-     |     |     |     |     |     |
| ----- | ---------- | ------------- | -------- | --------- | ----------- | ------------ | --- | --- | --- | --- | --- |
| vious | experiment |               | has been | repeated  | for all     | downloads of |     |     |     |     |     |
tracesetT2.Foreveryclip,twodownloadsareperformed,
againreducingthebandwidthofthenetworkconnectionto
|     |     |     |     |     |     |     | Figure | 10.Measured | download | time versus | estimated down- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | -------- | ----------- | --------------- |
50kbpsovertimeintervalsof15and120s,respectively.
loadtimeifnocongestionoccurs.Thedurationsoftheconges-
Foreveryclip,Figure10depictstwometrics:(i)themea-
tionepisodesare15and120s.
suredtimerequiredtocompletethedownloadand(ii)the
| estimated  |     | time required | to         | complete | the download | if no |     |     |     |     |     |
| ---------- | --- | ------------- | ---------- | -------- | ------------ | ----- | --- | --- | --- | --- | --- |
| congestion |     | occurred.     | The latter | metric   | is computed  | from  |     |     |     |     |     |
Equation(3),wheret isobtainedfromtheexperiment. the transmission data rate at the TCP layer is recovered,
ib
The results in Figure 10 clearly confirm the behaviour thenthebufferisdrained.However,whenthebufferisfull,
observed in Figure 9 for all of the videos of trace set the application layer is blocked from sending more data
T2. It can be concluded that the duration of the con- tothe buffer. However, itis unknown how deep and how
gestion episode determines whether or not the YouTube longthetemporarybandwidthreductionmustbetocause
server buffer can fully compensate the effect of the tem- a buffer overflow and, therefore, an increase in the total
| porary | bandwidth |     | reduction | in the | total download | time. |     |     |     |     |     |
| ------ | --------- | --- | --------- | ------ | -------------- | ----- | --- | --- | --- | --- | --- |
downloadtime.
TheseresultssuggestthattheYouTubeserver’sapplication To determine the size of this YouTube server buffer,
layer behaves as a non-greedy source that feeds the TCP we further analyse the traces corresponding to the down-
stackattherateimposedbythethrottlingalgorithm.The loadsoftracesetT2withareducedavailablebandwidthof
TCP layer possibly manages and implements the buffer- 50 kbps that lasts for an interval of 120 s. An estimation
ing.Then,whenanetworkcongestionepisodeoccurs,the
oftheYouTubeserverbufferisperformedforeverydown-
transmissiondatarateattheTCPlayerisreduced,andthe load on the basis of the results depicted in Figure 9 (b).
dataexcessthatcannotbetransmittedbeginstobestored TheestimationiscomputedasBs D Smax(cid:4)S min ,where
inthebuffer.Ifthecongestionepisodeisshortenoughand Bsdenotestheserverbuffersize.Smaxiscomputedduring
Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd. 371
DOI:10.1002/ett

P.Ameigeirasetal.
TableV. CumulativedensityfunctionoftheestimatedsizeoftheYouTubeserverbufferB.
s
B(MB) 1.96 1.98 2.00 2.02 2.04 2.06 2.08 2.10 s
Cumulativeprobability(%) 3.2 10.6 35.1 61.7 88.3 97.9 98.9 100
the congestion episode and represents the maximum dif- the initialization of parameters, the server sends an ini-
ferencebetweentheamountofdatareceivedbytheplayer tial burst of data as its pre-catching strategy. Afterwards,
andtheamountofdatareceivedifnocongestionepisode the filling procedure writes blocks of 64 KB of data into
occurred.S iscomputedafterthecongestionepisodeis theTCPsocketwithaperiodcontrolledbytheparameter
min
over and represents the minimum difference between the sending_rate (which is computed on the basis of throt-
amountofdatareceivedbytheplayerandtheamountof tling factor and the video encoding bit rate). The socket
datareceivedifnocongestionepisodeoccurred.TheCDF is assumed to transmit the data packets at the pace indi-
oftheresultingestimations(Bs)oftracesetT2areshown catedbytheTCPlayer.IftheTCPsocketsendingbuffer
inTableV.Theresultsshowthattheestimationsapproxi- becomesfull,theexecutionoftheprogrammeisblocked,
mateasizeof2MB.Hence,itisassumedthattheYouTube andthealgorithmcannotwritemoredatauntilthebuffer
serverbufferhasamaximumsizeof2MB(orequivalently, startstobedrained.
32chunksofsize64KBeach).
5.1. ValidationoftheproposedYouTube
5. SERVER TRAFFIC trafficgenerationmodel
GENERATION MODEL
Thissectionpresentsthevalidationoftheproposedtraffic
On the basis of the experimental data presented in previ- generationmodel.Forthispurpose,webuiltaserverthat
ous sections, a simple model of the traffic generated by emulates the YouTube server, providing FLV video clip
theYouTubeserverisproposedbymeansofanalgorithm files at the pace specified by the traffic generation model
described in pseudo-code (see Figure 11). The algorithm ofFigure11.Then,weevaluatedtheaccuracyofthesyn-
provides the instants at which the application layer feeds thetic traffic generated by our customised server and the
aTCPblockingsocket.Thesocketistobeopenedwitha onegeneratedbytheoriginalYouTubeserver.
sendingbufferof2MB. The experimental test bed used for this validation was
The algorithm consists of an initialization block and a designedtocollectdatatraffictracesofdownloadsfromthe
filling procedure. At the beginning, the algorithm calcu- originalYouTubeserveraswellasfromourYouTubeemu-
latestheinitializationparameters,whichwillbeusednext. lationserver.Forthefirstcase,wereusedtheframeworkof
Innetworksimulationtools,theencodingrateandthedura- Section3.Forthesecond,theplaybackmonitortool(see
tion can be obtained by sampling the CDF proposed in Section3.1)installedinourPCwasenabledtoaccessthe
Equation (1). From these two parameters, the video clip YouTubeemulationserverthatwaslocatedinanothercom-
sizecanbeestimated.Forthesubsequentphases,YouTube puterwithinthesameLocalAreaNetwork.Theemulation
assumesaminimumencodingrateequalto200kbps.After serverwasimplementedwiththepseudo-codeofFigure11
Figure11.Pseudo-codeofservertrafficgenerationmodel.
372 Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd.
DOI:10.1002/ett
21613915,
2012,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/ett.2546
by
University
Of
Granada,
Wiley
Online
Library
on
[13/05/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 21613915, 2012, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ett.2546 by University Of Granada, Wiley Online Library on [13/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
P.Ameigeirasetal.
inJava,anduponrequestofthewebbrowserofthePlay- whose CDF of the encoding rates matched the CDF of
backMonitorTool,itstartsfeedingtheTCPsocketwiththe the encoding rates of the extensive video clip collection
FLV contents at the pace indicated by the proposed traf- of trace set T3. The distribution of the encoding rates of
ficmodel.FordownloadsfromtheoriginalYouTubeand the selected video clips in trace set T4 is compared with
theemulatedserverS,theavailablebandwidthofthePC’s the ones in trace set T3 in the quantile–quantile plots of
networkconnectionwaslimitedto5Mbps.Withoutacom- Figure 12 for each video format. Moreover, for each for-
monlimit,theconnectiontotheemulatedserverthrough mat, a two-sample Kolmogorov–Smirnov test failed to
theLocalAreaNetworkwasexpectedtoprovideamuch
|     |     |     |     |     | reject the | null hypothesis | that the | encoding rates of the |
| --- | --- | --- | --- | --- | ---------- | --------------- | -------- | --------------------- |
higheravailablebandwidththantheconnectionthroughthe video clips in trace sets T4 and T3 are from the same
InternettotheoriginalYouTubeserver.Thiswouldcausea continuousdistributionatasignificancelevelof5%.
biasinthetimerequiredtodownloadtheinitialburstorto Foreveryvideoclipandserver,threecaseswereanal-
recoverafterabandwidthlimitationperiod,whichwould ysed:(i)noadditionalbandwidthlimitation;(ii)a50-kbps
impedethecomparisonbetweenthedownloadtracesfrom additional bandwidth limitation lasting 15 s; and (c) a
theoriginalYouTubeserverandfromtheemulatedone. 50-kbps additional bandwidth limitation lasting 120 s.
For the validation, we aimed at using a representative Again,thesebandwidthlimitationswereperformedusing
sample of 200 video clips for each FLV-based video for- SoftPerfect Bandwidth Manager Lite for Windows [15].
mat (i.e. itags equal to 5, 34 and 35) in trace set T4. For For every download, the playback monitor tool provided
each format, we selected (using the random prefix sam- the amount of accumulated data received by the player’s
| pling method                                  | presented | in [18]) | a set of 200 video | clips    | bufferasafunctionoftime.                      |     |         |             |
| --------------------------------------------- | --------- | -------- | ------------------ | -------- | --------------------------------------------- | --- | ------- | ----------- |
| 3T ni soediV fo )spbk(selitnauQ etaR gnidocnE |           |          |                    |          | 3T ni soediV fo )spbk(selitnauQ etaR gnidocnE |     |         |             |
| 500                                           |           |          |                    |          | 1000                                          |     |         |             |
| 450                                           |           |          |                    |          | 900                                           |     |         |             |
| 400                                           |           |          |                    |          | 800                                           |     |         |             |
| 350                                           |           |          |                    |          | 700                                           |     |         |             |
| 300                                           |           |          |                    |          | 600                                           |     |         |             |
| 250                                           |           |          |                    |          | 500                                           |     |         |             |
| 200                                           |           |          |                    |          | 400                                           |     |         |             |
| 150                                           |           |          |                    |          | 300                                           |     |         |             |
| 100                                           |           |          |                    |          | 200                                           |     |         |             |
| 50                                            |           |          | +                  | itag = 5 | 100                                           |     |         | + itag = 34 |
| 0                                             |           |          |                    |          | 0                                             |     |         |             |
| 0                                             | 100       | 200      | 300 400            | 500      | 0                                             | 200 | 400 600 | 800 1000    |
Encoding Rate Quantiles(kbps) of Videos in T4 Encoding Rate Quantiles(kbps) of Videos in T4
|     |     | a)  |     |     |     |     | b)  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
3T ni soediV fo )spbk(selitnauQ etaR gnidocnE
1400
1200
1000
800
600
400
|     |     |     | 200 |     |     | + itag = 35 |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
0
|     |     |     | 0 200 | 400 | 600 800 1000 | 1200 | 1400 |     |
| --- | --- | --- | ----- | --- | ------------ | ---- | ---- | --- |
Encoding Rate Quantiles(kbps) of Videos in T4
c)
Figure12.Encodingratesquantile–quantileplotsofvideoclipsintracesetsT3andT4,(a)itagD5,(b)itagD34and(c)itagD35.
Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd. 373
DOI:10.1002/ett

 21613915, 2012, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/ett.2546 by University Of Granada, Wiley Online Library on [13/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
P.Ameigeirasetal.
ThedownloadtracesfromtheoriginalYouTubeandthe sequences AŒn] and AOŒn(cid:2). Finally, for every video clip
emulatedservershavebeencomparedforeveryvideoclip and considered case, the 90th percentile of the discrete-
andconsideredcase.Forthecomparison,theinstantaneous time sequence "Œn] has been computed and denoted as
relativeerroroftheaccumulatedamountofdatahasbeen "O. Figure 13 represents the CDF of "O for the three
| computedateverysamplinginstantnas: |     |     |     |     |     | consideredcases. |      |                  |       |            |
| ---------------------------------- | --- | --- | --- | --- | --- | ---------------- | ---- | ---------------- | ----- | ---------- |
|                                    |     |     |     |     |     | The results      | show | that in the case | of no | additional |
jAOŒn(cid:2)(cid:4)AŒn(cid:2)j bandwidth limitation, 90% of the video clips have a rel-
"Œn(cid:2)D (4) ative error "O that does not exceed 4.5%. In the cases
AŒn(cid:2)
|     |     |     |     |     |     | with bandwidth | limitation, | 90% of | the video clips | have |
| --- | --- | --- | --- | --- | --- | -------------- | ----------- | ------ | --------------- | ---- |
where "Œn] denotes the instantaneous relative error, AŒn] a relative error "O that does not exceed 6%. Most of the
represents the amount of accumulated data received by observed error is an artefact of the technique used in
the player’s buffer in the case of the download from the our test bed to deal with the variable available band-
originalserverandAOŒn(cid:2)representstheamountofaccumu- width at the Internet. Bandwidth fluctuations at the
lated data from the emulated server. It should be noted Internetcannotbefullyeliminatedbythebandwidthlimi-
from Section 3.1 that our playback monitor tool dumps tationsintroducedtoourPC’snetworkconnection,which
thecollecteddataevery100ms,whichthereforefixesthe directlyaffecttherelativeerroroftheaccumulatedamount
| period between | consecutive | samples | of the | discrete-time |     | ofdata. |     |     |           |     |
| -------------- | ----------- | ------- | ------ | ------------- | --- | ------- | --- | --- | --------- | --- |
| 1              |             |         |        |               |     | 1       |     |     |           |     |
| 0.9            |             |         |        |               |     | 0.9     |     |     |           |     |
| 0.8            |             |         |        |               |     | 0.8     |     |     |           |     |
| 0.7            |             |         |        |               |     | 0.7     |     |     |           |     |
| 0.6            |             |         |        |               |     | 0.6     |     |     |           |     |
| FDC            |             |         |        |               | FDC |         |     |     |           |     |
| 0.5            |             |         |        |               |     | 0.5     |     |     |           |     |
| 0.4            |             |         |        |               |     | 0.4     |     |     |           |     |
| 0.3            |             |         |        |               |     | 0.3     |     |     |           |     |
|                |             |         |        | itag = 34     |     |         |     |     | itag = 34 |     |
| 0.2            |             |         |        |               |     | 0.2     |     |     |           |     |
|                |             |         |        | itag = 35     |     |         |     |     | itag = 35 |     |
| 0.1            |             |         |        |               |     | 0.1     |     |     |           |     |
|                |             |         |        | itag = 5      |     |         |     |     | itag = 5  |     |
| 0              |             |         |        |               |     | 0       |     |     |           |     |
| 0              | 2           | 4       | 6      | 8             | 10  | 0       | 2   | 4 6 | 8         | 10  |
^ε (%)
^ ε (%)
b)
a)
1
0.9
0.8
0.7
0.6
FDC
0.5
0.4
0.3
|     |     |     | 0.2 |     |     |     | itag = 34 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
itag = 35
0.1
itag = 5
0
|     |     |     | 0   | 2   | 4   | 6   | 8   | 10  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
^ε (%)
c)
Figure13.Cumulativedensityfunction(CDF)oftherelativeerror"ObetweendownloadsfromtheoriginalYouTubeserverandfrom
theemulatedoneforthefollowingcases:(a)noadditionalbandwidthlimitation,(b)a50-kbpsadditionalbandwidthlimitationlasting
15sand(c)a50-kbpsadditionalbandwidthlimitationlasting120s.
374 Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd.
DOI:10.1002/ett

P.Ameigeirasetal.
6. RELATED WORK schemesthatgeneratesuserrequeststhatcontainvideoid,
clientIP,requesttimeandcontentsize.Additionally,Rao
Theimpactofnewandexistingservicesontrafficvolume et al. also proposed a mathematical model of the aggre-
in current and future backbone networks has been stud- gatevideostreaming.However,tothebestofourknowl-
ied in [28]. In this respect, YouTube is the leading video edge,ourworkisthefirsttopresentandvalidateamodel
downloadsite,beingratedasthethirdmostvisitedInternet that provides for each video clip the instants and blocks
site[2]. ofdataatwhichtheYouTube applicationlayergenerates
Various studies have been performed to characterise thetraffic.
YouTube traffic, each of which has focused on different
aspects.Works[5,29,30]analysedrelevantcharacteristics
ofYouTube videos suchas theirpopularity, duration, file 7. CONCLUSIONS
size,bitrateandsocialnetworkcharacteristics.
Fromadifferentperspective,theworkin[31]presented This paper characterises the YouTube service from the
the characteristics of YouTube traffic over a campus net- viewpoint of traffic generation in the server’s application
work,providingstatisticsregardingthevideorequestrate layer,whichisveryvaluableforpredictingthevideoqual-
over time, the number of requests per client, the session ityperceivedbyend-usersandenhancingnetworkdesign.
durationandfilesize,andtheauthorsfurtheranalysedthe The characterisation is based on combined information
implicationsoncachingmethods. frombothYouTube’sofficialdocumentationandthecon-
In[32],thecharacterisationwasperformedfromadig- ducted experiments. The focus has been on FLV-based
ital subscriber line provider perspective, indicating that videoclipsbecause,asithasbeenshowninSection3.3,the
theYouTubetrafficcharacteristicsdiffersignificantlyfrom defaultdownloadfromregularPCsuseanFLVcontainer
thoseofotherWebtrafficandthatYouTubeserversapplya formorethan92%ofthevideosclips.
dataratelimitationofabout1.25Mbps.Similarly,thework The presented results have shown that YouTube’s pro-
in [33] investigated the characteristics of network traffic gressive download commences by transferring an initial
flows of video-sharing services from a network provider burst of 40 s of data at the Internet’s maximum avail-
standpoint. ablebandwidthandlaterappliesathrottlingalgorithmthat
In addition to our work, other studies have focused imposesadatarateequalto1.25(i.e.thethrottlingfactor)
on the traffic characteristics of YouTube video streaming timesthevideoclipencodingrate.Ourresultshaveshown
servers. Alcock and Nelson [22] found some of its basic thatYouTubeappliesaminimumtransmissiondatarateof
properties.Inparticular,theyillustratedthatitisastandard 250kbpsduringthethrottlingphaseandaminimumsizeof
practice for YouTube servers to send consistently sized theinitialburst(equivalentto40smultipliedby200kbps).
blocksof64-KBdataatareducedratetolimittheamount Moreover,ithasalsobeenshownthataftertheinitialburst,
ofdatathatissenttotheclient.Theyalsodescribedthat thedataaresentinchunksof64KB.
duringtheinitialburstphase,theamountofdatasentbythe The YouTube media serverreacts to a reduction inthe
YouTube server is related to the transmission rate during transmissiondatarateintheTCPlayerasifthedataexcess
thethrottlingphase. thatcannotbetransmittedwereaccumulatedattheserver
Rao et al. [23] made an extensive description of the buffer, which is later drained if the bandwidth availabil-
streamingstrategyofYouTubeandNetflix.ForYouTube, ity is recovered. The TCP layer possibly manages and
they measured the traffic characteristics for the cases of implementsthisserverbuffer.Ifthecongestionepisodeis
access via PCs and mobile devices and additionally con- longenough,theserverbufferisfilled,andtheapplication
sideredseveralcontainers(Flash,HTML5andFlashHD). layerisblockedfromsendingmoredatatothebuffer.This
TheirmeasurementresultsforthecaseofFLV-filedown- causes the time required to complete the download of a
loads accessed via PC also exhibited an initial burst and videocliptoincreaseeveniflaterthebandwidthavailabil-
shorton–offperiodswithathrottlingfactor. ityisfullyrecovered.Theexperimentsconductedhavealso
Finamore et al. [7] also compared the traffic genera- indicatedthatthesizeoftheserverbufferisapproximately
tionwhenaccessingYouTubeviaPCsandmobiledevices. 2.0MB.
Theydescribedthatmobiledevicescannotbuffertheentire Becauseoftherelevanceofthevideoclipencodingrate
video,sotheplayerprogressivelyrequestsportionsaccord- indeterminingthedownloaddatarate,aCDFoftheencod-
ingtotheevolutionoftheplayback.Ourinvestigationof ingratesforFLV-filebasedvideoclipshasbeencomputed.
YouTubetraffichasalsofoundthecharacteristicspresented It has been shown that for the itag equal to 34 (which is
by Rao [23] and Alcock [22], although our results have the default format for 92% of the video clips), the video
shownthatYouTubeappliesaminimumtransmissiondata clipencodingraterangesfrom100kbpstoapproximately
rate during the throttling phase and a minimum size of 1 Mbps. This implies that during the throttling phase,
the initial burst. Unlike previous works, we have carried traffic is generated at a rate that ranges from 250 kbps
outtheanalysisforthecaseofreductionoftheavailable to approximately 1.25 Mbps. The obtained CDF of the
bandwidthinthenetwork. encoding rates has been fitted by an analytical function.
RegardingthemodellingofYouTubetraffic,Zinketal. Additionally, the CDF of the video clip duration is also
[31] proposed a model for evaluating proxy caching presentedandfittedbyananalyticalfunction.
Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd. 375
DOI:10.1002/ett
21613915,
2012,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/ett.2546
by
University
Of
Granada,
Wiley
Online
Library
on
[13/05/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

P.Ameigeirasetal.
On the basis of all of the conducted experiments, a 6. Matera F, Matteotti F, Pasquali P, Rea L, Tarantino
YouTube server traffic generation model has been for- A, Baroncini V, Del Prete G, Gaudino G. Compari-
mulated, which can be easily implemented in network sonbetweenobjective andsubjectivemeasurementsof
simulation tools to evaluate service performance and
quality of serviceover anOptical Wide Areanetwork.
end-userquality.
European Transactions on Telecommunications 2008;
Forvalidationpurposes,wehavebuiltaserverthatemu-
19(3):233–245.DOI:10.1002/ett.1189.
lates the YouTube server, providing FLV video clip files
7. Finamore A, Mellia M, Munafo M, Rao SG. YouTube
at the pace specified by the proposed traffic generation
everywhere: impact of device and infrastructure syn-
model.Wehavecomparedtheaccumulatedamountofdata
received by the player when using our customised server ergies on user experience, In Proceedings of the 11th
and when using the original YouTube server. The results Annual Internet Measurement Conference (IMC ’11),
haveshownthat,for90%oftheconsideredvideos,therela- Berlin,Germany,November2011;345–360.
tiveerrordoesnotexceed4.5%inthecaseofnoadditional 8. Adobe Systems Incorporated. Adobe Flash Player.
bandwidth limitation and 6% in the cases of additional [cited 2012 April 25]. Available from: http://www.
bandwidthlimitations. adobe.com/.
Finally,forfuturework,weareinterestedinthecharac-
9. Adobe Systems Incorporated. Video file format
terisationoftheYouTubetrafficinthecaseofnetworkcon-
specification version 10.1. [cited 2012 April 25].
gestionepisodeswithpacketlossesandvariablebandwidth
Available from: http://download.macromedia.com/f4v/
limitations.
video_file_format_spec_v10_1.pdf.
10. YouTube-DL documentation. [cited 2012 April 25].
Available from: http://rg3.github.com/youtube-dl/docu-
ACKNOWLEDGEMENTS
mentation.html.
11. Youtube Corporation. YouTube APIs and tools.
This work was supported by the Ministerio de Ciencia
[cited 2012 April 25]. Available from: http://code.
e Innovación of Spain under research project TIN2010-
google.com/intl/en-US/apis/youtube/overview.html.
20323. The authors would like to thank the anonymous
reviewersfortheirvaluablecomments.Theauthorswould 12. Staehle B, Hirth M, Pries R, Wamser F, Staehle D.
alsoliketothankProfessorJoseCarlosSegura-Lunaand YoMo:aYoutubeapplicationcomfortmonitoringtool.
JoseA.Zamora-Cobofortheirveryvaluablecollaboration. Technical Report 467, University of Würzburg, March
2010.
13. Red Iris. Red Iris Weathermap. [cited 2012
April 25]. Available from: http://www.rediris.es/
REFERENCES
conectividad/weathermap/.
1. Cisco Corporation. Cisco Visual Networking Index: 14. Wireshark Corporation. Wireshark network protocol
forecast and methodology, 2010-2015. White paper. analyzer. [cited 2012 April 25]. Available from:
[cited2012April25].Availablefrom:http://www.cisco. http://www.wireshark.org/.
com/en/US/solutions/xcollateral/ns341/ns525/ns537/ns 15. Softperfect Research. SoftPerfect bandwidth manager
705/ns827/white_paper_c11-481360_ns827_Network- lite version for Windows. [cited 2012 April 27].
ing_Solutions_White_Paper.html. Available from: http://www.softperfect.com/products/
2. Alexa Corporation. The top 500 sites on the web. bandwidth/.
[cited 2012 April 25]. Available from: http://www. 16. Inlet Media Corporation. FLVTool2–flash video and
alexa.com/topsites. metadatamanipulation.[cited2012April25].Available
3. Cisco Corporation. Cisco Visual Networking Index: from:http://www.inlet-media.de/flvtool2/.
global mobile data traffic forecast update, 2011-2016. 17. Characterization of trace sets T1 and T2. [cited
White paper. [cited 2012 April 25]. Available from: 2012 April 25]. Available from: http://dtstc.ugr.es/
http://www.cisco.com/en/US/solutions/collateral/ns341/ tl/downloads/set_t1_t2.csv.
ns525/ns537/ns705/ns827/white_paper_c11-520862.pdf. 18. Zhou J, Li Y, Adhikari VK, Zhang Z. Count-
4. Garapati N. Quality estimation of YouTube video ing YouTube videos via random prefix sampling,
service, Master Thesis, Blekinge Institute of Technol- In Proceedings of the 2011 Internet Measurement
ogy,Sweden,Feb.2010. Conference (IMC’11), Berlin, Germany, 2011, DOI:
5. Gill P, Arlitt M, Li Z, Mahanti A. YouTube traffic 10.1145/2068816.2068851.
characterization:aviewfromtheedge,InProceedings 19. Google Data API Protocol – API query parameters.
of the 7th ACM SIGCOMM Conference on Internet [cited 2012 April 25]. Available from: http://code.
Measurement, San Diego, 2007, DOI: 10.1145/ google.xcom/apis/youtube/2.0/developers_guide_proto-
1298306.1298310. col_api_query_parameters.html.
376 Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd.
DOI:10.1002/ett
21613915,
2012,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/ett.2546
by
University
Of
Granada,
Wiley
Online
Library
on
[13/05/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the applicable
Creative
Commons
License

P.Ameigeirasetal.
20. Characterization of trace set T3. [cited 2012 April 28. Palkopoulou E, Merkle C, Schupke DA, Gruber CG,
25]. Available from: http://dtstc.ugr.es/tl/downloads/ Kirstädter A. Traffic models for future backbone net-
format_set_t3.xlsx and http://dtstc.ugr.es/tl/downloads/ works – a service-oriented approach. European Trans-
metadata_set_t3.xlsx. actions on Telecommunications 2011; 22(4): 137–150.
21. Characterization of trace set T4. [cited 2012 April DOI:10.1002/ett.1464.
25]. Available from: http://dtstc.ugr.es/tl/downloads/ 29. Cheng X, Dale C, Liu J. Understanding the char-
format_set_t4.xlsxandhttp://dtstc.ugr.es/tl/downloads/ acteristics of Internet short video sharing: YouTube
metadata_set_t4.xlsx. as a case study. Technical Report arXiv:0707.3670v1
22. Alcock S, Nelson R. Application flow control in [cs.NI],CornellUniversity,arXive-prints,2007.
Youtube video streams. ACM SIGCOMM Com- 30. Cha M, Kwak H, Rodriguez P, Ahn Y, Moon S.
puter Communication Review 2011; 41(2). DOI: I tube, you tube, everybody tubes: analyzing the
10.1145/1971162.1971166. world’s largest user generated content video system,
23. Rao A, Lim Y, Barakat C, Legout A, Towsley D, In Proceedings of the 7th ACM SIGCOMM Confer-
Dabbous,W.Networkcharacteristicsofvideostreaming enceonInternetMeasurement,SanDiego,2007,DOI:
traffic,InProceedingsofthe7thInternationalConfer- 10.1145/1298306.1298309.
ence on emerging Networking EXperiments and Tech- 31. Zink M, Suh K, Gu Y, Kurose J. Characteristics
nologies (CoNEXT), Tokyo, Japan, December 2011. of YouTube network traffic at a campus net-
http://dl.acm.org/citation.cfm?doid=2079296.2079321. work – measurements, models, and implications.
24. Microsoft Corporation. Windows Media Services Computer Networks 2008; 53: 501–514. DOI:
features and benefits. [cited 2012 February 27]. 10.1016/j.comnet.2008.09.022.
Available from: http://www.microsoft.com/windows/ 32. PlissonneauL,En-NajjaryT,Urvoy-KellerG.Revisit-
windowsmedia/forpros/serve/features.aspx. ingwebtrafficfromaDSLproviderperspective:thecase
25. Varsa V, Curcio I. Transparent end-to-end packet ofYouTube,InProceedingsofthe19thITCSpecialist
switched streaming service (PSS); RTP usage model Seminar 2008 on Network Usage and Traffic (ITC SS
(release9).3GPPTR26.937V9.0.0,2009. 19),Berlin,Germany,2008.
26. Microsoft Corporation. IIS Media Services. 33. Mori T, Kawahara R, Hasegawa H, Shimogawa S.
[cited 2012 February 27]. Available from: http:// Characterizing traffic flows originating from large-
technet.microsoft.com/en-us/library/ee729229(WS.10). scale video sharing services. In Proceedings of Traffic
aspx.June10,2010. Monitoring and Analysis: Second International Work-
27. Welzl M. Network Congestion Control: Managing shop(TMA2010).Springer:Zurich,Switzerland,2010;
Internet Traffic. John Wiley & Sons: The Atrium, 17–31.
Southern Gate, Chichester, West Sussex PO19 8SQ,
England,2005.
Trans.EmergingTel.Tech.23:360–377(2012)©2012JohnWiley&Sons,Ltd. 377
DOI:10.1002/ett
21613915,
2012,
4,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/ett.2546
by
University
Of
Granada,
Wiley
Online
Library
on
[13/05/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License