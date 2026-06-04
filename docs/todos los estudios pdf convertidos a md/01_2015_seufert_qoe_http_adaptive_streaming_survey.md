IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015 469
A Survey on Quality of Experience of
HTTP Adaptive Streaming
MichaelSeufert,SebastianEgger,MartinSlanina,ThomasZinner,TobiasHoßfeld,andPhuocTran-Gia
Abstract—Changing network conditions pose severe problems Index Terms—HTTP adaptive streaming, variable video qual-
to video streaming in the Internet. HTTP adaptive streaming ity,dynamicstreaming,qualityofexperience.
(HAS)isatechnologyemployedbynumerousvideoservicesthat
relieves these issues by adapting the video to the current net-
I. INTRODUCTION
workconditions.Itenablesserviceproviderstoimproveresource
utilization and Quality of Experience (QoE) by incorporating NOWADAYS, video is the most dominant application in
information from different layers in order to deliver and adapt
theInternet.Accordingtoarecentstudyandforecast[1],
avideoinitsbestpossiblequality.Thereby,itallowstakinginto
global Internet video traffic accounted for 15 PB per month
accountenduserdevicecapabilities,availablevideoqualitylevels,
current network conditions, and current server load. For end in 2012, which is 57% of all consumer traffic. By 2017, it is
users, the major benefits of HAS compared to classical HTTP expectedtoreach52PBpermonth,whichwillthenbe69%of
videostreamingarereduced interruptionsofthevideoplayback theentireconsumerInternettraffic.Twothirdsofallthattraffic
and higher bandwidth utilization, which both generally result in will then be delivered by content delivery networks (CDN)
ahigherQoE.Adaptationispossiblebychangingtheframerate,
like YouTube, which is already today one of the most popular
resolution, or quantization of the video, which can be done with
Internetapplications.
various adaptation strategies and related client- and server-side
actions. The technical development of HAS, existing open stan- For a long period of time, YouTube has been employing
dardized solutions, but also proprietary solutions are reviewed a server-based streaming, but recently it introduced HTTP
inthispaperasfundamentaltoderivetheQoEinfluencefactors adaptive streaming (HAS) [2] as its default delivery/playout
that emerge as a result of adaptation. The main contribution is
method.HASrequiresthevideotobeavailableinmultiplebit
acomprehensivesurveyofQoErelatedworksfromhumancom-
rates, i.e., in different quality levels/representations, and split
puterinteractionandnetworkingdomains,whicharestructured
according to the QoE impact of video adaptation. To be more intosmallsegmentseachcontainingafewsecondsofplaytime.
precise, subjective studies that cover QoE aspects of adaptation Theclientmeasuresthecurrentbandwidthand/orbufferstatus
dimensionsandstrategiesarerevisited.Asaresult,QoEinfluence andrequeststhenextpartofthevideoinanappropriatebitrate,
factorsofHASandcorrespondingQoEmodelsareidentified,but
suchthatstalling(i.e.,theinterruptionofplaybackduetoempty
also open issues and conflicting results are discussed. Further-
playoutbuffers)isavoidedandtheavailablebandwidthisbest
more, technical influence factors, which are often ignored in the
context of HAS, affect perceptual QoE influence factors and are possiblyutilized.
consequentlyanalyzed.Thissurveygivesthereaderanoverviewof This trend can not only be observed with YouTube, which
thecurrentstateoftheartandrecentdevelopments.Atthesame is a prominent example, but nowadays an increasing number
time,ittargetsnetworkingresearcherswhodevelopnewsolutions
ofvideoapplicationsemployHAS,asithasseveralmoreben-
forHTTPvideostreamingorassessvideostreamingfromauser
efits compared to classical streaming. First, offering multiple
centricpointofview.Therefore,thispaperisamajorsteptoward
trulyimprovingHAS. bit rates of video enables video service providers to adapt
the delivered video to the users’ demands. As an example, a
high bit rate video, which is desired by home users typically
enjoying high speed Internet access and big display screens,
Manuscript received February 17, 2014; revised July 28, 2014; accepted is not suitable for mobile users with a small display device
August 31, 2014. Date of publication September 30, 2014; date of current andslowerdataaccess.Second,differentservicelevelsand/or
version March 13, 2015. This work was supported by the COST Action
pricingschemescanbeofferedtocustomers.Forexample,the
IC1003 Qualinet, by the Deutsche Forschungsgemeinschaft (DFG) under
GrantsHO4770/2-1andTR257/38-1(DFGprojectOekoNet),intheframework customers could select themselves which bit rate level, i.e.,
of the EU ICT Project SmartenIT (FP7-2012-ICT-317846), and by Brno whichqualityleveltheywanttoconsume.Moreover,adaptive
UniversityofTechnologyunderProjectCZ.1.07/2.3.00/30.0005.
streaming allows for flexible service models, such that a user
M. Seufert, T. Zinner, and P. Tran-Gia are with the Institute of Com-
puter Science, University of Würzburg, 97074 Würzburg, Germany (e-mail: can increase or decrease the video quality during playback if
seufert@informatik.uni-wuerzburg.de; zinner@informatik.uni-wuerzburg.de; desired, and can be charged at the end of a viewing session
trangia@informatik.uni-wuerzburg.de).
exactly taking into account the consumed service levels [3].
S. Egger was with FTW Telecommunications Research Center, Vienna,
Austria.HeisnowwiththeDepartmentofInnovationSystems,Technology Finallyandmostimportant,thecurrentvideobitrate,andhence
Experience,AITAustrianInstituteofTechnologyGmbH,1220Vienna,Austria thedemandeddeliverybandwidth,canbeadapteddynamically
(e-mail:sebastian.egger@aic.ac.at).
to changing network and server/CDN conditions. If the video
M.SlaninaiswiththeDepartmentofRadioElectronics,BrnoUniversityof
Technology,61600Brno,CzechRepublic(e-mail:slaninam@feec.vutbr.cz). is available in only one bit rate and the conditions change,
T.HoßfeldwaswiththeUniversityofWürzburg.HeisnowwiththeChair eitherthebitrateissmallerthantheavailablebandwidthwhich
ofModelingofAdaptiveSystems,UniversityofDuisburg-Essen,45127Essen,
leads to a smooth playback but spares resources which could
Germany(e-mail:tobias.hossfeld@uni-due.de).
DigitalObjectIdentifier10.1109/COMST.2014.2360940 be utilized for a better video quality, or the video bit rate is
1553-877X©2014IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttp://www.ieee.org/publications_standards/publications/rights/index.htmlformoreinformation.

470 IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015
Fig.1. Structureofthearticle.StartingfromtheQualityofExperienceofHTTPvideostreaming,technicalpossibilitiesofadaptationandtheresultinginfluence
onQualityofExperienceareinthefocusofthiswork.
higherthantheavailablebandwidthwhichleadstodelaysand strategy and parameters. The dimensions of adaptation which
eventually stalling, which degrades the Quality of Experience can be utilized for HAS are outlined in Section V. As end
(QoE) severely (e.g., [4] and [5]). Thus, adaptive streaming usersperceivethequalityadaptationwhenusingaHASservice,
mightimprovetheQoEofvideostreaming. SectionVIsurveystheinfluenceofeachdimensiononQoEand
HAS is an evolving technology which is also of interest for describespossibletrade-offs.SectionVIIpresentsuserexperi-
theresearchcommunity.Theopenquestionsaremanifoldand ence related impairments in a shared network and respective
coverboththeplanningphaseandtheoperationalphase. countermeasures. Finally, Section VIII maps the key findings
PlanningPhase: to different stakeholder perspectives discussing the lessons
learned,challenges,andfuturework,andSectionIXconcludes.
(cid:129) How (i.e., with which parameters) to convert a source
videotogiventargetbitrates?
(cid:129) Which dimensions (image quality, spatial, temporal) to
II. QUALITYOFEXPERIENCEINFLUENCEFACTORSOF
adapt?
HTTPVIDEOSTREAMING
OperationalPhase
HTTP video streaming (video on demand streaming) is a
(cid:129) When(i.e.,underwhichcircumstances)toadapt?
combinationofdownloadandconcurrentplayback.Ittransmits
(cid:129) Whichqualityrepresentationtorequest?
the video data to the client via HTTP where it is stored in an
Moreover, the performance of existing implementations or application buffer. After a sufficient amount of data has been
proposed algorithms has to be evaluated and improvements downloaded (i.e., the video file download does not need to be
have to be identified. This is especially important as today’s complete yet), the client can start to play out the video from
mechanismsdonottakeintoaccounttheresultingQoEofend the buffer. As the video is transmitted over TCP, the client
users.However,QoEisthemostimportantperformancemetric receives an undisturbed copy of the video file. However, there
as video services are expected to maximize the satisfaction of are a number of real world scenarios in which the properties
theirusers. (most importantly instantaneous throughput and latency) of
Intheresearchcommunity,somesurveysexist,whichrelate a communication link serving a certain multimedia service
to HAS, but mainly focus on visual quality (e.g., [6]–[9]) or are fluctuating. Such changes can typically appear when com-
streaming technology (e.g., [10]–[14]). However, no survey municating through a best effort network (e.g., the Internet)
of the relationship of HAS and subjectively perceived quality where the networking infrastructure is not under control of an
has been done. Such QoE aspects of adaptation have already operator from end to end, and thus, its performance cannot
been investigated in subjective end user studies in different be guaranteed. Another example is reception of multimedia
disciplines and communities. This work surveys these studies, contentthroughamobilechannel,wherethechannelconditions
identifies influence factors and QoE models, and discusses arechangingovertimeduetofading,interferences,andnoise.
challenges toward new HAS mechanisms. Therefore, this ar- Thesenetworkissues(e.g.,packetloss,insufficientbandwidth,
ticle follows the structure as depicted in Fig. 1: In Section II, delay, and jitter) will decrease the throughput and introduce
the main influence factors of QoE of HTTP video streaming, delays at the application layer. As a consequence, the playout
i.e., initial delay and stalling, are outlined. As changing video buffer fills more slowly or even depletes. If the buffer is
qualitylevels(i.e.,adaptation)introducesnewimpactsonQoE, empty, the playback of the video has to be interrupted until
theremainderoftheworkwillfocusonadaptation.SectionIII enoughdataforplaybackcontinuationhasbeenreceived.These
presents the approach of HTTP adaptive streaming and de- interruptionsarereferredtoasstallingorrebuffering.
scribes the current state of the art. Section IV describes the In telecommunication networks, the Quality of Service
influences on QoE which arise from the employed adaptation (QoS) is expressed objectively by network parameters like

| SEUFERTetal.:SURVEYONQUALITYOFEXPERIENCEOFHAS |              |     |         |          |        |     |          |     |     |     | 471 |
| --------------------------------------------- | ------------ | --- | ------- | -------- | ------ | --- | -------- | --- | --- | --- | --- |
| packet                                        | loss, delay, | or  | jitter. | However, | a good | QoS | does not |     |     |     |     |
guaranteethatallcustomersexperiencetheservicetobegood.
Thus,QualityofExperience(QoE)—aconceptofsubjectively
| perceived | quality—was |     | introduced | [15]. | It  | takes | into account |     |     |     |     |
| --------- | ----------- | --- | ---------- | ----- | --- | ----- | ------------ | --- | --- | --- | --- |
howcustomersperceivetheoverallvalueofaservice,andthus,
| relies on | subjective | criteria. |      | For HTTP | video | streaming,   | [4],    |     |     |     |     |
| --------- | ---------- | --------- | ---- | -------- | ----- | ------------ | ------- | --- | --- | --- | --- |
| [16] show | in their   | results   | that | initial  | delay | and stalling | are the |     |     |     |     |
keyinfluencefactorsofQoE.However,changingthetransmit-
| ted video | quality | as  | employed | by  | HTTP | adaptive | streaming |     |     |     |     |
| --------- | ------- | --- | -------- | --- | ---- | -------- | --------- | --- | --- | --- | --- |
introducesanewperceptualdimension.Therefore,inthispaper
| we will | present | detailed | results | on the | influence | of  | adaptation |     |     |     |     |
| ------- | ------- | -------- | ------- | ------ | --------- | --- | ---------- | --- | --- | --- | --- |
onsubjectivelyperceivedvideoquality.
Ingeneral,theQoEinfluencefactorscanbecategorizedinto
technicalandperceptualinfluencefactorsasdepictedinFig.2.
| The perceptual |        | influence   | factors | are     | directly  | perceived | by the    |     |     |     |     |
| -------------- | ------ | ----------- | ------- | ------- | --------- | --------- | --------- | --- | --- | --- | --- |
| end user       | of the | application |         | and are | dependent | but       | decoupled |     |     |     |     |
fromthetechnicaldevelopment.Forexample,severaltechnical
| reasons    | can introduce |       | initial    | delay, | but the         | end user | only per-  |     |     |     |     |
| ---------- | ------------- | ----- | ---------- | ------ | --------------- | -------- | ---------- | --- | --- | --- | --- |
| ceives the | waiting       | time. | Therefore, |        | it is necessary |          | to analyze |     |     |     |     |
alsothetechnicalinfluencefactors,whichdrivetheperception
oftheendusers.Inthissection,theperceptualinfluencefactors
| of HTTP | video | streaming | will | be described |     | in detail. | In later |     |     |     |     |
| ------- | ----- | --------- | ---- | ------------ | --- | ---------- | -------- | --- | --- | --- | --- |
sections(cf.Fig.1),wewillfocusonHASspecificparameters.
A. InitialDelay
| Initial        | delay        | is always    | present | in           | a multimedia |             | streaming     |     |     |     |     |
| -------------- | ------------ | ------------ | ------- | ------------ | ------------ | ----------- | ------------- | --- | --- | --- | --- |
| service        | as a certain | amount       |         | of data must | be           | transferred | before        |     |     |     |     |
| decoding       | and          | playback     | can     | begin. The   | practical    |             | value of the  |     |     |     |     |
| minimal        | achievable   | initialdelay |         | thus         | depends      | on          | the available |     |     |     |     |
| transmission   | data         | rate         | and     | the encoder  | settings.    |             | Usually, the  |     |     |     |     |
| video playback |              | is delayed   |         | more than    | technically  |             | necessary     |     |     |     |     |
| in order       | to fill      | the playout  |         | buffer       | with a       | bigger      | amount of     |     |     |     |     |
videoplaytimeinthereceiveratfirst.Theplayoutbufferisan
| efficient | tool | used to | tackle | short term | throughput |     | variations. |     |     |     |     |
| --------- | ---- | ------- | ------ | ---------- | ---------- | --- | ----------- | --- | --- | --- | --- |
However,theamountofinitiallybufferedplaytimeneedstobe
tradedoffbetweentheactuallengthofthecorrespondingdelay
(morebufferedplaytime=longerinitialdelay)andtheriskof
bufferdepletion,i.e.,stalling(morebufferedplaytime=higher
robustnesstoshorttermthroughputvariations).
| Reference |           | [17] shows | that         | the        | impact       | of initial | delays      |                  |                      |                  |                |
| --------- | --------- | ---------- | ------------ | ---------- | ------------ | ---------- | ----------- | ---------------- | -------------------- | ---------------- | -------------- |
| strongly  | depends   | on         | the concrete |            | application. | Thus,      | results     |                  |                      |                  |                |
|           |           |            |              |            |              |            |             | Fig. 2. Taxonomy | of HAS QoE influence | factors surveyed | in this paper. |
| obtained  | for other | services   |              | (e.g., web | page         | load       | times [18], |                  |                      |                  |                |
Theseparationofperceptualandtechnicalinfluencefactorsisreflectedinthe
IPTVchannelzappingtime[19],andUMTSconnectionsetup structureofthiswork.
| time [20]) | cannot | easily | be  | transferred | to  | video | streaming. |     |     |     |     |
| ---------- | ------ | ------ | --- | ----------- | --- | ----- | ---------- | --- | --- | --- | --- |
However, those works presume a logarithmic relationship be- confirms for mobile video users that initial delays are con-
tweenwaitingtimesandmeanopinionscore(MOS),whichis sidered less important than other parameters (e.g., technical
ameasureofsubjectivelyperceivedquality(QoE).References qualityofthevideoorstalling)andarelesscriticalforhaving
[17] and [21] find fundamental differences between initial agoodexperience.
delays and stalling.Reference [17] observes that initial delays Thus,theimpactofinitialdelaysonQoEofvideostreamingis
are preferred to stalling by around 90% of users. The impact not severe. Reference [17] shows that initial delays up to 16 s
ofinitialdelayonperceivedqualityissmallanddependsonly reducetheperceivedqualityonlymarginally.Asvideoservice
on its length but not on video clip duration. In contrast to users are used to some delay before the start of the playback,
expectedinitialdelay,whichiswaitingbeforetheserviceandis they usually tolerate it if they intend to watch the video.
wellknownfromeverydayusageofvideoapplications,stalling However, recently [24] and [25] describe a new user behavior
invokes a sudden unexpected interruption within the service. especially for user-generated contents. They report that users
Hence, stalling is processed differently by the human sensory areoftenbrowsingthroughvideos,i.e.,theystartmanyvideos
system, i.e., it is perceived much worse [22]. Reference [23] but watch only the first seconds, in order to search for some

472 IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015
Fig.3. ComparisonofHTTPvideostreamingandHTTPadaptivevideostreaming.Enduserisnotawareofserviceornetworkinfluences,butonlyperceives
initialdelays,stalling,andqualityadaptations.
contentstheyareinterestedin.Inthatcase,initialdelaysshould video encoder, especially for lower values of the quantization
belowtobeacceptedbytheuser,however,theQoErelatedto parameter. The authors of [4] present a model for mapping
videobrowsingiscurrentlynotinvestigatedinresearchyet. regular stalling patterns to MOS. They show that there is an
It follows for video service implementations, like for any exponentialrelationshipbetweenstallingparametersandMOS.
service,thatinitialdelaysshouldbekeptshort,buthereinitial Moreover,theyfindthatuserstolerateatmostonestallingevent
delaysarenotamajorperformanceissue.Althoughshortdelays per clip as long as its duration remains in the order of a few
mightbedesirableforuser-generatedcontentwhenusersoften seconds.Morestallingresultsinhighlydissatisfiedusers.
justwanttopeekintothevideo,evenlongerdelaysuptoseveral Thus, all video streaming services should avoid stalling
seconds will be tolerated, especially if users intend to watch whenever possible, as already little stalling severely degrades
avideo. the perceived quality. Classical HTTP video streaming is
strongly limited and cannot react to fluctuating network con-
ditionsotherthanbytradingoffplayoutbuffersizeandstalling
B. Stalling
duration.Incontrast,HTTPadaptivestreamingismorevariable
Stallingisthestoppingofvideoplaybackbecauseofplayout and is able to align the delivered video stream to the current
bufferunderrun.Ifthethroughputofthevideostreamingappli- networkconditions,therebymitigatingthestallinglimitation.
cation is lower than the video bit rate, the playout buffer will
deplete. Eventually, insufficient data is available in the buffer
C. Adaptation
and the playback of the video cannot continue. The playback
is interrupted until the buffer contains a certain amount of HTTPadaptivestreamingisbasedonclassicalHTTPvideo
video data. Hereagain, theamount ofrebuffered playtimehas streaming but makes it possible to switch the video quality
to be traded off between the length of the interruption (more during the playback in order to adapt to the current network
buffered playtime = longer stalling duration) and the risk of conditions. In Fig. 3, both methods are juxtaposed. To make
a shortly recurring stalling event (more buffered playtime = adaptation possible,thestreamingparadigmmustbechanged,
longerplaybackuntilpotentialnextstallingevent). such that the client, who can measure his current network
In [26], the authors show that an increased duration of conditionsattheedgeofthenetwork,controlswhichdatarateis
stalling decreases the quality. They also find that one long suitableforthecurrentconditions.Ontheserverside,thevideo
stalling event is preferred to frequent short ones. However, issplitintosmallsegmentsandeachofthemisavailableindif-
the position of stalling is not important. This last finding is ferent quality levels/representations (which represent different
refuted in [27], which shows that there is an impact of the bitratelevels).Basedonnetworkmeasurements,theadaptation
position.In[28],theauthorsinvestigatebothstallingandframe algorithmattheclient-siderequeststhenextpartofthevideoin
rate reduction. They show that stalling is worse than frame theappropriatebitratelevelwhichisbestsuitedundercurrent
ratereduction.Furthermore,theyshowthatstallingatirregular networkconditions.
intervals is worse than periodic stalling. In [14], stalling is Reference[29]comparesadaptiveandnon-adaptivestream-
comparedtoquantization.Theauthorspresentarandomneural ingundervehicularmobilityandrevealsthatqualityadaptation
network model to estimate QoE based on both parameters. can effectively reduce stalling by 80% when bandwidth de-
They find in subjective studies that users are more sensitive creases, and is responsible for a better utilization of the avail-
tostallingthantoanincreaseofquantizationparameterinthe ablebandwidthwhenbandwidthincreases.Alsoinnon-mobile

SEUFERTetal.:SURVEYONQUALITYOFEXPERIENCEOFHAS 473
| environments, | HAS      | is useful | because      | it avoids | stalling | to  |     |     |     |
| ------------- | -------- | --------- | ------------ | --------- | -------- | --- | --- | --- | --- |
| the greatest  | possible | extent    | by switching | the       | quality. | The |     |     |     |
provisioning–deliveryhysteresispresentedin[30]confirmsthat
itisbettertocontrolthequalitythantosufferfromuncontrolled
| effects like | stalling. | The | authors compare | video | streaming |     |     |     |     |
| ------------ | --------- | --- | --------------- | ----- | --------- | --- | --- | --- | --- |
impairmentsduetopacketlosstoimpairmentsduetoresolution
reduction.Theymapobjectiveresultstosubjectivelyperceived
qualityandfindthattheimpactoftheuncontrolleddegradation
(i.e.,packetloss)onQoEismuchmoreseverethantheimpact
ofacontrolledbandwidthreductionduetoresolution.
| Thus,            | HAS is   | an improvement | over                  | classical      | HTTP           | video  |     |     |     |
| ---------------- | -------- | -------------- | --------------------- | -------------- | -------------- | ------ | --- | --- | --- |
| streaming        | as it    | aims to        | minimize uncontrolled |                | impairments.   |        |     |     |     |
| However,         | compared | to classical   | HTTP                  | video          | streaming,     | an-    |     |     |     |
| other dimension, |          | i.e., the      | quality adaptation,   |                | was introduced |        |     |     |     |
| (see Fig.        | 3). In   | the context    | of HAS,               | this dimension |                | is not |     |     |     |
| wellresearched.  |          | Therefore,     | we willpresent        | HAS            | indetail       | and    |     |     |     |
reviewsubjectivestudiesfromdifferentfieldsontheinfluences
| of application      | layer     | adaptation   | on QoE      | of end | users          | in the |     |     |     |
| ------------------- | --------- | ------------ | ----------- | ------ | -------------- | ------ | --- | --- | --- |
| following           | sections. | Adaptations  | on other    | layers | (e.g., network |        |     |     |     |
| traffic management, |           | modification | of content, | CDN    | structure)     |        |     |     |     |
arenotinthefocusbecauseenduserseventuallyperceiveonly
| resulting | initial | delays, stalling, | or quality | adaptations |     | when |     |     |     |
| --------- | ------- | ----------------- | ---------- | ----------- | --- | ---- | --- | --- | --- |
using a HAS service. Other impairments beyond video QoE, Fig.4. PrincipleofadaptiveHTTPstreaminginatypicalDASHsystem.The
serverprovidesmediametadataintheMPD,andmediasegmentsindifferent
which are caused by usage of HAS in a shared network, are representations.Theclientrequestsmediasegmentsindesiredrepresentations
presentedinSectionVII. basedonMPDinformationandmeasurementofthroughputandbufferfilllevel.
III. CURRENTHTTPADAPTIVESTREAMINGSOLUTIONS indifferentservices.Currently,theindustryforumgroupsover
60members,amongwhichimportantplayersinthemultimedia
A. DevelopmentandMilestones and networking market can be found [41]. One of the most
AfterthefirstlaunchofanHTTPadaptivestreamingsolution importantoutputsoftheindustryforumisDASH-AVC/264—a
|     |     |     |     |     |     | recommendation | of profiles | and settings serving | as guidelines |
| --- | --- | --- | --- | --- | --- | -------------- | ----------- | -------------------- | ------------- |
byMoveNetworksin2006[31]–[33],HTTPadaptivestream-
ingwascommerciallyrolledoutbythreedominantcompanies forimplementingDASHwithH.264/AVCvideo[42].
| in parallel—as | Microsoft |             | Silverlight Smooth | Streaming |                | (MSS) |     |     |     |
| -------------- | --------- | ----------- | ------------------ | --------- | -------------- | ----- | --- | --- | --- |
| [34] by        | Microsoft | Corporation | (2008),            | HTTP      | Live Streaming |       |     |     |     |
B. TechnologyBehind
| (HLS) [35] | by Apple | Inc. | (2009) and | Adobe HTTP | Dynamic |     |     |     |     |
| ---------- | -------- | ---- | ---------- | ---------- | ------- | --- | --- | --- | --- |
Streaming (HDS) [36], [37] by Adobe Systems Inc. (2010). It has been mentioned in Section III-A that adaptive HTTP
Despite their wide adoption and commercial success, these streaming solutions, provided as standardized or proprietary
solutions are mutually incompatible, although they share a technologies by different companies, share a similar techno-
similartechnologicalbackground(seeSectionIII-B). logical background. An adaptive HTTP streaming solution
ThefirststandardizedapproachtoadaptiveHTTPstreaming architecturecanlookliketheoneshowninFig.4,inwhichthe
was published by 3GPP in TS 26.234 Release 9 [38] in 2009 terminologyusedadherestotheDASHspecification.Although
withtheintendeduseinUniversalMobileTelecommunications other HAS solutions use different terminology and different
System-LongTermEvolution(UMTSLTE)mobilecommuni- data formats (cf. Tables I and II), the principle of operation is
| cation networks. |     | In the context | of [38], | the description |     | of the thesame. |     |     |     |
| ---------------- | --- | -------------- | -------- | --------------- | --- | --------------- | --- | --- | --- |
adaptivestreamingtechniqueisquitegeneral—thefundamental InatypicalHASstreamingsession,atfirst,theclientmakesa
streamingprincipleisprovidedandonlyabriefdescriptionof HTTP request to the server in order to obtain metadata of the
themediaformatisgiven.Theworkof3GPPcontinuedbyim- differentaudioandvideorepresentationsavailable,whichiscon-
proving the adaptive streaming solution in close collaboration tainedintheindexfile.InDASH,theindexfileiscalledMedia
withMPEG[39]and,finally,theDynamicAdaptiveStreaming PresentationDescription(MPD,seeFig.4),whileMSSandHDS
over HTTP (DASH) standard for general use of HAS was usethetermmanifest,andtheindexfileinHLSiscalledplay-
issuedbyMPEGin2012[40].Todate,theDASHspecifications list.Thepurposeofthisindexfileistoprovidealistofrepresen-
are contained in four parts, defining the media presentation tationsavailabletotheclient(e.g.,availableencodingbitrates,
description and segment formats, conformance and reference videoframerates,videoresolutions,etc.)andameanstoformu-
software, implementation guidelines, and segment encryption lateHTTPrequestsforachosenrepresentation.Themostimpor-
andauthentication,respectively. tantconceptinadaptiveHTTPstreamingisthatswitchingamong
Apart from the standardization itself, it is also worth men- different representations can occur at fixed, frequent time
tioning that in connection with DASH, an industry forum has instantsduringtheplayback,asillustratedinFig.5.Toachieve
beenformedinordertoenablesmoothimplementationofDASH this,themediacorrespondingtotherespectiverepresentations

474 IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015
TABLE I
COMPARISONOFDIFFERENTProprietaryHTTPADAPTIVESTREAMINGSOLUTIONS.THEDATADESCRIPTIONFORMATISEITHEREXTENSIBLE
MARKUPLANGUAGE(XML),PLAINTEXTMULTIMEDIAPLAYLIST(M3U8),ORFLASHMEDIAMANIFEST(F4M).
AREADERINTERESTEDINANEXPLANATIONOFTHEVIDEOANDAUDIOCODECSANDREFERENCES
TOTHERESPECTIVENORMATIVEDOCUMENTSISREFERREDTO[43]
TABLE II
COMPARISONOFDIFFERENTStandardHTTPADAPTIVESTREAMINGSOLUTIONS
timebasedontheclient’srequest(e.g.,DASH).Theadaptation
engineintheclientdecideswhichofthemediasegmentsshould
bedownloadedbasedontheiravailability(indicatedbytheindex
|     |     |     |     |     | file), the   | actual | network       | conditions | (measured  |          | or estimated |      |
| --- | --- | --- | --- | --- | ------------ | ------ | ------------- | ---------- | ---------- | -------- | ------------ | ---- |
|     |     |     |     |     | throughput), | and    | media playout |            | conditions | (playout | buffer       | fill |
level).Toallowforsmoothswitchingamongdifferentrepresen-
tations,thesegmentscorrespondingtodifferentrepresentations
mustbeperfectlytime(frame)aligned.
|     |     |     |     |     | The application |     | control | loop is | shown | in the | upper | part of |
| --- | --- | --- | --- | --- | --------------- | --- | ------- | ------- | ----- | ------ | ----- | ------- |
Fig.6.Basedonthemeasurementofrelevantparameters(e.g.,
|     |     |     |     |     | available     | bandwidth      | or receiver |         | buffer fullness—more |          |         | details |
| --- | --- | --- | --- | --- | ------------- | -------------- | ----------- | ------- | -------------------- | -------- | ------- | ------- |
|     |     |     |     |     | are discussed | in             | Section     | III-D), | the client’s         | decision |         | engine  |
|     |     |     |     |     | selects which | representation |             | to      | download             | next.    | In this | work,   |
themainfocusisonthedecisionsofasingleHASinstanceand
theirimpactsonQoE.However,thereisacomplexinterplayof
thecontrolloopwithotherapplicationsandthenetworkwhich
Fig. 5. Video representations available in adaptive HTTP streaming. The canalsoaffectQoE.Therefore,theinteractionsbetweendiffer-
HASserverstoresthevideocontentencodedindifferentrepresentations,each
|     |     |     |     |     | ent HAS | players, | other applications, |     | and | the interactions |     | with |
| --- | --- | --- | --- | --- | ------- | -------- | ------------------- | --- | --- | ---------------- | --- | ---- |
representationischaracterizedbyitsvideobitrate,eventuallyalsoresolution,
frame rate, etc. (not displayed here). The vertical dashed lines represent the theTCPcongestioncontrollooparediscussedinSectionVII.
points at which the client can switch among different representations. The AlthoughthedifferentHASsolutionssharethebasicprinci-
| switch points | are at the boundaries | of neighboring | segments and | are frame |     |     |     |     |     |     |     |     |
| ------------- | --------------------- | -------------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
pleasillustratedinFig.4,theydifferinanumberoftechnical
| aligned in all    | the representations | available. Switching    | is controlled    | by the |             |     |               |     |                 |     |              |     |
| ----------------- | ------------------- | ----------------------- | ---------------- | ------ | ----------- | --- | ------------- | --- | --------------- | --- | ------------ | --- |
|                   |                     |                         |                  |        | parameters. | The | main features | of  | the proprietary |     | and standard |     |
| adaptation engine | (see Fig. 4)        | based on the estimation | of server-client | link   |             |     |               |     |                 |     |              |     |
throughput(redcurve).
HASsolutionsaresummarizedinTablesIandII,respectively.
Inthecontextofthispaper,thefollowingparametersareofhigh
| issplitupintopartsofshortdurations(segmentsorchunks)typ- |     |     |     |     | importance: |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
ically1to15slongandeitherstoredontheserverasonefile Codec: Althoughwecanfindcodecagnostic(MPEGDASH)
per segment (e.g., HLS) or extracted from a single file at run- or variable codec (MSS, HDS) solutions, several systems are

SEUFERTetal.:SURVEYONQUALITYOFEXPERIENCEOFHAS 475
mostimportantdecisionsaredoneregardingthepreparationof
the content, i.e., what representations shall be provided, and
regardingitsdelivery,e.g.,theselectionofthebestCDNserver
foreachrequest.
The behavior of the HAS system needs to obey the re-
quirements of the actual use case. For example, in the context
of a live system, the content is made available at the server
during the viewing and a low overall delay introduced by
the system shall be achieved. This implies that the provided
segmentlengthsshouldbesmallandthesegmentsneedtostart
downloadingassoonastheyappearontheserver.Forvideoon
demandsystems,onthecontrary,alargerreceiverbuffercanbe
used together with longer segments to avoid flickering caused
byfrequentqualityrepresentationchanges.Thefollowingsec-
tionsdiscusstheactionsthesystemoritsdesignercantakeon
Fig.6. ControlloopofHAS.Basedonmeasurementstheclientdecideswhich theserversideandontheclientsideinordertoefficientlyadapt
segmenttodownloadnext.Thecontrolloopinteractswithotherapplications totheactualconditionswhileconsideringcontextrequirements.
(e.g.,otherHASinstances)andthenetwork(e.g.,TCPcongestioncontrolloop)
whichcanalsoaffectQoE.
C. Server-SideActions
tailoredtospecificsupportedcodingalgorithmsforbothvideo
and audio. Currently there is an obvious domination of H.264 On the server side of an HTTP adaptive streaming system,
forvideo,whichissupportedbyallsolutionsinourscope,how- themainconcernisthepreparationofthecontent,i.e.,selection
ever it can be expected that the recently standardized H.265/ of available representations, and optimal encoding. This also
HEVC (High Efficiency Video Coding) [48] will take part of includes proper selection of system parameters, such as the
its share in the coming years. For audio, the codec selection lengthofanencodedsegment(whereselectable).
flexibility is generally higher. The implications of audio and Thelengthofthevideosegmentneedstoobeytwocontradic-
videoencoderselectionandconfigurationarefurtherdiscussed toryrequirements.First,thesegmentsneedtobeshortenough
inSectionIII-C. to allow for fast reaction to changing network conditions. On
Format: The currently dominant formats for media encap- the other hand, the segments need to be long enough to allow
sulation are the MPEG-2 transport stream (M2TS [49]; used highcodingefficiencyofthesourcevideoencoder[54]andto
byHLS,DASH)andISOBaseMediaFileFormat(MP4[50]; keep the amount of overhead low (the impact of segment size
usedbyDASH)oritsderivativereferredtoasfragmentedMP4 onthenecessaryoverheadisquantifiedin[55]).Clearly,these
(fMP4[51],[52];usedbyHDSandMSS). tworequirementsformanoptimizationproblemwhichneedsto
MPEG-2transportstreamscarrythedatainpacketsofafixed beconsideredattheserversideduringcontentpreparation.
184-byte length plus a 4-byte header. Each packet contains In [56], the length of video segments to be offered to the
onlyonetypeofcontent(audio,video,data,orauxiliaryinfor- client is optimized based on the content, so that I-frames and
mation). M2TS is commonly used for streaming, although its representation switches are placed at optimal positions, e.g.,
structureisnotasflexibleasinthecaseofMP4.MP4organizes video cuts. Such an approach led to approximately 10% de-
theaudiovisualdatainso-calledboxesandtreatsdifferenttypes crease of the required bit rate for a given video image quality.
ofdataseparately.Further,thereisahighflexibilityinhandling Thisworkisfollowedby[57],wherevariablesegmentlengths
theauxiliaryinformation(suchascodecsettings),whichcanbe acrossdifferentrepresentationsareconsidered—itisproposed
tailoredtotheneedsoftheapplication.Assuch,MP4hasbeen that for higher bit rates, longer segments are used in order to
successfullyadjustedtocarryprioritizedbitstreamsofscalable improvecodingefficiency.
videooverHAS[53],whichwefurtherconsiderinSectionIII-C. Among the server-side actions is also the selection of com-
SegmentLength: ThesegmentlengthusedinaHASsystem pression algorithms for audiovisual content (in cases where it
specifies the shortest video duration after which a quality (bi- is not fixed by the system specification). A recent comparison
trate)adjustmentcanoccur.Althoughsomesystemskeepthese ofdifferentvideocompressionstandards[58]justifiesthevery
valuesfixed(TableI),thesegmentlengthcanbeleftuptothe widespread use of H.264/AVC (Advanced Video Coding) en-
individualimplementationinmanycases(TableII).Again,we coding [59] for video as shown in Tables I and II, although
will further discuss the implications related to segment length codec flexibility, available in several proprietary and standard
designinSectionIII-C. solutions, is a clear advantage due to the emerging highly
It is clear from the principle of adaptive HTTP streaming efficientHEVC(HighEfficiencyVideoCoding)standard[58].
that the decision engine responsible for selecting appropriate Apart from single-layer codecs like H.264/AVC or HEVC
representationsisrunningontheclientsideandneedstoselect whereonlydifferentrepresentations(i.e.,differentfiles)ofthe
the representation to request based on different criteria. These same video can be switched, multi-layer codecs can be used
criteria can be measurements of downlink throughput, the ac- which enable bitstream switching. Such features were also
tualvideobufferstatus,deviceorscreenproperties,orcontext introducedinAVC(cf.SP/SIsynchronization/switchingframes
information(e.g.,mobility).Ontheserverside,incontrast,the [60])anddatebacktotheMPEG-2standard[61]whichneeded

476 IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015
abigoverheadtoachievescalabilityintimeswhenprocessors variousSVCconfigurationsiswellknown[68],[69]butpapers
werehardlyfastenough. dealingwithDASHandQoEfocusonAVC,andtheintegration
Amodernmulti-layercodecisScalableVideoCoding(SVC) of DASH and SVC is only evaluated using objective metrics
which is an amendment to AVC and offers temporal, spatial, [70]andsimulations[71],[72]sofar.
andimagequalityscalability[62].ThismeansthatSVCallows ThearchitectureofHTTPadaptivestreamingsystemsallows
foradaptationofframerateandcontentresolution,andswitch- for optimization of the server load. In [73], for instance, the
ing between different levels of image quality. It makes use of authorsproposeaschemeforbalancingtheloadamongseveral
difference coding of the video content such that data in lower servers through altering the addresses in the DASH manifest
layers can be used to predict data or samples of higher layers files.
(so called enhancement layer). In order to switch to a higher Itisobviousthatthemainconcernintheserver-sideactions
layer, only the missing difference data have to be transmitted istheselectionofappropriatecodingforthedifferentavailable
andadded.Thus,themajordifferencetoadaptationwithsingle- quality levels. This includes not only the selection of the
layer codecs is that quality can be increased incrementally in compression algorithm and its settings, but also the decision
caseofspareresources.Withsingle-layercodecs,ontheother onadaptationdimensionstobeemployed.Anoverviewofthe
hand,awholenewsegmenthastobedownloaded,andalready availableadaptationdimensionswillfollowinSectionV.
downloadedlowerqualitysegmentshavetobediscarded.
There are two trade-offs that need to be addressed in case
D. Client-SideActions
anSVC-basedHASsolutionisdeployed.Thefirsttrade-offis
theoverheadintroducedbymulti-layercodecs.Thismeans,for On the client side, the most important decisions are which
example,thatanSVCfileofavideoofacertainqualityislarger segments to download, when to start with the download, and
comparedtoanAVCfileofthesamevideoandquality.Fairly howtomanagethereceivervideobuffer.Theadaptationalgo-
low overhead can be achieved in case the scalable encoder rithm(decisionengine)shouldselecttheappropriaterepresen-
is carefully adjusted, and the number of enhancement layers tations in order to maximize the QoE, which can be achieved
is low—e.g., in [63] the authors achieve around 10% bit rate in several different ways. The most common approach is to
overhead in an optimized encoder when quality scalability is estimate the instantaneous channel bandwidth and use it as
appliedonlowresolutionsequenceswith5extractablebitrate decisioncriterion.
levels. The authors also show that the overhead for spatial Thereceivervideobuffersizeisdealtwithin[74],wherethe
scalability largely depends on the spatial scalability ratio, i.e., authors perform an analysis of receiver buffer requirement for
the resolution ratio of the successive layers. SVC is shown to variablebitrateencodedbitstreams.Theyfindthattheoptimal
be very efficient for spatial scalability ratio of 1/2 but rather bufferlengthdependsonthebitstreamcharacteristics(datarate
inefficient for scalability ratio of 3/4 where the overhead is and its variance) as well as network characteristics and, of
between40%and100%.Performanceofqualityscalabilityof course,thedesiredvideoQoErepresentedbyinitialdelayand
SVC has been analyzed in [64], where the results claim that rebufferingprobability.
theoverheadneededfortwoenhancementlayersis10%–30%. A recent work [75] reviews the available bitrate estimation
Thesefindingsareconfirmedby[65]and[66],whereadetailed algorithms and describes the active and passive bitrate mea-
objectiveperformanceanalysisofSVCindifferentlayersetups surement approaches. The passive measurement requires no
isperformed,leadingtoarecommendationofcreatingasepa- additional probe packets to be inserted in the network, which
rateSVCstreamforeachresolution,thususingonlythequality resultsinnoadditionaloverheadattheexpenseoflessaccurate
scalability feature of SVC inpractical HASsystems.Itis also results. The absence of additional overhead is the reason why
shown in [65], [66] that the performance varies largely across passivetoolsaregenerallyusedforavailablebitrateestimation
different SVC encoder implementations. The second trade-off inHAS.Theauthorof[75]classifiesthepassivemeasurement
is the amount of signaling required. The authors of [67] show approaches to cross layer-based, where the protocol stack is
thatSVCcanreducetheriskofstallingbyalwaysdownloading modified to obtain packet properties (e.g., [76]) and model-
the base layer and optionally downloading the enhancement based, which employ throughput modeling (such as [77] for
layers when there is enough available throughput. Such im- wireless LAN networks using TCP or UDP transport proto-
proved flexibility comes at the cost of increased signaling cols). The following paragraphs describe different adaptation
traffic as several HTTP requests are needed per segment. This algorithms generally based on passive measurement of avail-
implies that AVC performs better under high latencies, while ablebitrateorsegmentdownloadtime.
SVC adapts more easily to sudden and temporary bandwidth Depending on the actual use case and scenario, different
fluctuationswhenusingasmallreceiverbuffer. adaptation strategies can be employed to adapt to the varying
By applying a hierarchical coding scheme, SVC allows for available bitrate. In [78] the authors compare several seg-
the selection of a suitable sub-bitstream for the on-the-fly ment request strategies in HAS for live services. The analysis
adaptation of the media bitstream to device capabilities and uses passive measurement of segment arrival times, aiming at
current network conditions. A valid sub-bitstream contains at evaluating the video startup delay, end to end delay, and the
least the AVC-compatible base layer and zero or more en- time available for segment download through the analysis of
hancementlayers.Notethatallenhancementlayersdependon differentinitialdelayadjustment,thetimetostartdownloading
the base layer and/or on the previous enhancement layer(s) of the next segment, and the way to handle missing segments or
the same scalability dimension. The subjective evaluation of theirparts.Itisshownthatdifferentstrategiesexhibitdifferent

SEUFERTetal.:SURVEYONQUALITYOFEXPERIENCEOFHAS 477
behavior, and the adjustment needs to reflect network condi- atesendingbuffercontrol,i.e.,servercomplexityisincreased.
tionsanddesiredQoEprioritiesofthesystem. More details on pipelining performance can be found in [87].
Forliveandvideoondemandservices,[79]and[80]describe Theauthorsof[88]comparetheperformanceofMSS,Netflix,
a decision engine based on Markov Decision Process (MDP) and OMSF (an open source player) clients in terms of the
using the estimated bit rate as input. Reference [81] proposes reaction of the clients to persistent or short-term bandwidth
a rate adaptation algorithm based on smoothed bandwidth changes,thespeedofconvergencetothemaximumsustainable
changesmeasuredthroughsegmentfetchtime,whereasin[82], bitrate and, finally, playback delay, important particularly for
theauthorsproposeanadaptationenginebasedonthedynamics live content playback. The study reveals significant inefficien-
oftheavailablethroughputinthepastandtheactualbufferlevel cies in each of the clients. In [89], the authors compare a
to select the appropriate representation. At the same time, the MSSclientandtheirownDASHclientinWirelessLocalArea
algorithmadjuststherequiredbufferleveltobekeptinthenext Network (WLAN) environment, finding that the DASH client
run. Also in [83], an algorithm for single-layer content (e.g., outperforms the MSS client in terms of average achieved bit
AVC)ofconstantbitrateispresented,whichselectsrepresen- rate, number of fluctuations, rebuffering time, and fairness. In
tationsaccordingtocurrentbandwidth,currentbufferlevel,and [55], the performance of DASH for live streaming is studied.
the average bit rate of each segment. For multi-layer content An analysis of performance with respect to segment size is
(e.g., SVC), [84] describes the Tribler algorithm, which relies provided, quantifying the impact of the HTTP protocol and
on thresholds of downloaded segments, and [85] proposes the segmentsizeontheendtoenddelay.
BIEBalgorithm,whichisalsoanSVC-basedstrategycomput- Theproblemoftheperformancecomparisonin[83]and[88]
ingsegmentthresholdsbasedonsizeratiosbetweenqualitylev- is that the different clients are seen as closed components and
els.Notethatwithmulti-layerstrategiesdifferentqualitylevels the logic inside is unknown. In such cases, the system per-
of the same time slot can be requested independently. Single- formance clearly depends on the actual implementation of the
layerstrategiescanalsorequestdifferentrepresentationsofthe clientandtheadaptationalgorithmused.In[85],aperformance
same time slot, but only one can be used for decoding, and comparisonoftheadaptationalgorithmsdescribedin[82]–[85]
alreadydownloadedotherrepresentationswillbediscarded. is conducted. The traffic patterns used for the evaluation were
Itisimportanttomentionthatthepresentedalgorithmsselect recordedinrealisticwiredandvehicularmobilitysituations.In
among the available representations just based on technical terms of average playback quality and bandwidth utilization,
parameters like bandwidth or bit rate, but do not take the BIEB[85]andTribler[84]canoutperformtheotheralgorithms
expectedqualityperceivedbytheenduserintoaccount. significantly. Both algorithms deliver a high average playback
qualitytotheuser,butTriblerhastoswitchtoadifferentquality
ninetimesmoreoftenthanBIEB.Thealgorithmof[82]shows
E. PerformanceStudies
betterresultsthanBIEBinsomeaspects,asithasalowerqual-
HTTP adaptive streaming uses the TCP transport protocol, ityswitchingfrequencyandabetternetworkefficiencybecause
which,althoughreliable,introduceshigheroverheadanddelays nodataisunnecessarilydownloadedandbandwidthiswasted.
comparedtothesimplerUDP,broadlyusedforvideoservices However, compared to the size of the movie, the segments
earlier.AstherearefundamentaldifferencesbetweenTCPand discarded by BIEB are negligible. In the vehicular scenario,
UDP, studies have been done on justifying the use of TCP for BIEB outperforms the other algorithms, but no performance
video transmission. In [86], for instance, the authors employ results are provided so far for other scenarios. Reference [90]
discrete-time Markov models to describe the performance of enhancestheperformancecomparisonof[85]bycomputingthe
TCP for live and stored media streaming without adaptation. QoE-optimaladaptationstrategyforeachbandwidthcondition
ItisfoundthatTCPgenerallyprovidesgoodstreamingperfor- andshowsthattheBIEBalgorithmisclosesttotheoptimum.
mance when the achievable TCP throughput is roughly twice Also other optimization criteria for algorithm performance
thevideobitrate,i.e.,thereisasignificantsystemoverheadas assessmentlikePSNR[91]orpseudo-subjectivemeasureslike
theexpenseforreliabletransmission. engagement[92],[93]havebeenused.Thesecriteriaareoften
A number of studies have been published aiming at com- assumptions regarding QoE impact, which date from earlier
parison of the existing HAS solutions, both proprietary and studies and have neither been questioned nor verified with
standardized,intermsofperformance.In[83],theauthorscom- respect to their QoE appropriateness [94]. Thus, dedicated
pareMSS,HLS,HDS,andDASHinavehicularenvironment, studies on the impact of adaptation strategies and application
using off-the-shelf client implementations for the proprietary parameters onQoEwillbepresented inthefollowingsection.
systems and their own DASH client. They find that the best These results should be taken into account when designing a
performance, represented by average achieved video bit rate QoE-awareHASalgorithm.
andthenumberofswitchesamongrepresentations,isachieved
by MSS among proprietary solutions and by Pipelined DASH
IV. QOEINFLUENCEOFADAPTATIONSTRATEGY
among all the candidates. The idea behind Pipelined DASH is
ANDAPPLICATIONPARAMETERS
that several segments can be requested at a time in contrast
to standard DASH. Pipelining is beneficial in vehicular and A QoE model for adaptive video streaming, which can be
mobilescenarios,wherepacketlossmightresultinapoorusage used for automated QoE evaluation, is described in [104].
of the available resources in case only one TCP connection is The authors find that adaptation strategy related parameters
established.Thedrawbackisthatpipeliningrequiresappropri- (stalling,representationswitches)havetobetakenintoaccount

478 IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015
TABLE III
EFFECTSOFAPPLICATIONPARAMETERSSETTINGSONADAPTATIONANDONSUBJECTIVELYPERCEIVEDVIDEOQUALITY
and that they have to be considered on a larger time scale mobile devices. With video segment size, there is a trade-
(up to some minutes) than video encoding related parameters off between short segment sizes resulting in many small files,
(resolution,framerate,quantizationparameter,bitrate),which which have to be stored for multiple bit rates of each video.
onlyinfluenceintheorderofafewseconds.In[5],QoEmetrics Larger segment sizes, however, may not be sufficient to adapt
for adaptive streaming, which are defined in 3GPP DASH torapidbandwidthfluctuationsespeciallyinvehicularmobility
specification TS 26.247, are presented. They include HTTP andleadtomorestalling.However,thiseffectcanbebalanced
request/responsetransactions,representationswitchevents,av- by increasing the buffer threshold, i.e., the amount of data
eragethroughput,initialdelay,bufferlevel,playlist,andMPD which is buffered before the video playback starts. Thus, the
information.However,theconductedQoEevaluationconsiders authors state explicitly that it is important to configure the
only stalling as most dominating QoE impairment. Other re- buffer threshold in accordance with the used video segment
sultsregardingtheQoEinfluenceofadaptationparametersare size.Also[95]confirmsbysimulationsthatalongeradaptation
summarizedinTableIIIandwillbepresentedinmoredetailin interval, i.e., longer time between two possible quality adap-
thissection. tations, leads to higher quality levels of the video and fewer
Reference[29]investigateshowplayoutbufferthresholdand quality changes. However, the number of stalling events and
video segment size influence the number of stalling events. the total delay increase. Additionally, [96] reveals an impact
Theyfindthatasmallbufferof6sissufficienttoachieveanear on players’ concurrent behavior, such that large segment sizes
uninterrupted streaming experience under vehicular mobility. allow for a high network utilization but have negative effects
Further increasing the buffer size leads to an increased initial on fairness. These aspects beyond pure video QoE will be
delay and could also be an issue for memory constrained discussedinmoredetailinSectionVII.

SEUFERTetal.:SURVEYONQUALITYOFEXPERIENCEOFHAS 479
Reference[98]showsthattheactiveadaptationofthevideo size in order to deliver a generally acceptable quality. Finally,
bit rate improves or decreases the video quality according to the content plays a significant role in spatial and temporal
theswitchingdirection,butdowngradinghasastrongerimpact adaptation. For image quality reduction, no significant effect
on QoE than increasing the video bit rate. Thus, the authors can be found. The authors conclude that videos with complex
arguethattherecouldbeadegradationcausedbytheswitching spatialdetailsareparticularlyaffectedbyresolutionreduction,
itself. Reference [102] investigates the adaptation of image while videos with complex and global motion require high
quality for layer-encoded videos. They find that the frequency frameratesforsmoothplayback.
ofadaptationshouldbekeptassmallaspossible.Ifavariation In [100], the effects of switching amplitude, switching
cannot be avoided, its amplitude should be kept as small as frequency, and recency effects are investigated. The results
possible. Thus, a stepwise decrease of image quality is rated demonstrate the high impact of the switching amplitude, and
slightly better than one single decrease. Also [101] compares that recency effects (i.e., impact of last quality level and time
smoothtoabruptswitchingofimagequality.Theyconfirmthat after last switch) can be neglected if more than two switches
down-switching is generally considered annoying. Abrupt up- occur. Moreover, it turns out that not the switching frequency
switching,however,mightevenincreaseQoEasusersmightbe but rather the time on each individual layer has a significant
happytonoticethevisualimprovement.Reference[102]finds impactonQoE.Thisconfirmsresultsfrom[99],whichinvesti-
that a higher base (i.e., lowest quality) layer results in higher gatesdynamicallyvaryingvideoqualityonmobiledevices.In
perceivedquality,whichimpliesthatsegmentswhichraisethe thiswork,theauthorsfindthatusersrewardattemptstoimprove
base layer should rather be downloaded instead of improving quality, and thus, they suggest that quality should always be
on higher quality layers. This finding is confirmed by [99] for switchedtoahigherlayer,ifpossible.
mobile devices. Finally, [102] also observes a strong recency To sum up, adaptation is a key influence parameter of
effect, i.e., higher quality in the end of a video clip leads to video streaming services. The reviewed studies suggest an
higher QoE. In [103], the impact of image quality adaptation influence of adaptation amplitudes and times (i.e., frequency,
onSVCvideosisshownforabaselayerandoneenhancement time on each layer), which has to be taken into account by
layer. The authors find that a higher base layer quality allows HAS adaptation strategies. By setting the buffer and segment
for longer impairments to be accepted. The duration of such sizes, video service providers can adjust the adaptation times.
impairments has linear influence on the perceived quality. For As practically relevant switching frequencies (i.e., adaptation
their 12 s video clips the influence of the number of impair- intervals of 2 s or more) are low and have little impact on
ments is only significant between one and two impairments, QoE, adaptation algorithms should try to keep the quality as
whiletheintervalbetweenimpairmentsdoesnotseemtohave high as possible first. Additionally, the perceived quality is
anysignificantinfluence. affecteddifferentlybythedifferentadaptationdimensions(i.e.,
In [105], the authors present an approach which overrides image quality, spatial, or temporal adaptation). Depending on
clientadaptationdecisionsinthenetworkinordertooptimize the content, quality switches will be more or less perceivable.
QoE globally or for a group of users. However, this way of Thus,whenpreparingthestreamingcontent,acontentanalysis
“adaptation”goesbeyondsingleuseroptimizationasdiscussed could allow for improved video segmentation and selection of
within this section. A discussion on network level adapta- the best adaptation dimension(s) and amplitudes. Section V
tion issues and related user experience problems follows in presentsthesedimensionsindetail,andtheirinfluencesonQoE
SectionVII. isoutlinedinSectionVI.
Reference [97] investigates flicker effects for SVC videos,
i.e., rapid alternation of base layer and enhancement layer, in
V. VIDEOADAPTATIONDIMENSIONS
adaptive video streaming to handheld devices. They identify
three effects, namely, the period effect, the amplitude effect, Inordertofollowtherequirementofprovidingvideocontent
andthecontenteffect.Theperiodeffect,i.e.,thefrequencyof at different bit rates for HTTP adaptive streaming, one or
adaptation,manifestsitselfsuchthathighfrequencies(adapta- severaladaptationdimensionscanbeutilized.Inthefollowing
tionintervallessthan1s)areperceivedasmoreannoyingthan paragraphs,wedescribethepossibleadaptationdimensionsand
constant low quality. At low frequencies (adaptation interval providearealworldexampleofthebitratereductionefficiency
larger than 2 s), quality is better than constant low quality, ofeachapproach.Ourrealworldexampleisbasedonencoding
but saturates when decreased further. The amplitude, i.e., the 20secondslongsequenceswithdifferentcontent(sport-200m
difference between quality levels, is the most dominant factor sprint,cartoon-aclipfromtheSintelmovie[106],action-acar
fortheperceptionofflickerasartifactsbecomemoreapparent. chasingscenefromthemovie“KnightandDay”).Wehaveen-
However, image quality adaptation is not detectable for most codedthesequences withH.264/AVCwithvaryingframerate
participants at low amplitudes. Also for temporal adaptation, (from 25 fps down to 2.5 fps), resolution (from 1920 × 1080
changes between frame rates of 15 fps and 30 fps are not de- progressive down to 128 × 72 progressive), and quantization
tectedbyhalfoftheusers.Onlyanincreaseofthequantization parameter (from 30 up to 51). All other encoding parameters
parameter (QP), i.e., reduction of image quality, from 24 QP remained unchanged during the experiment (the x264 codec
above 32 QP, or frame rate reduction below 10 fps brings implementationwasused,highprofile,level4.0,adaptiveGOP
significant flicker effects, which result in low acceptance for lengthupto2seconds).
high frequencies. For spatial adaptation, the authors indicate VideoFrameRatebasedbitrateadaptationreliesondecreas-
thatthechangeofresolutionshouldnotexceedhalftheoriginal ingthetemporalresolutionofavideosequence,i.e.,encoding

480 IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015
Fig.7. Adaptationthroughframeratereduction. Fig.9. Adaptationthroughadjustmentoftransformcoefficientquantization.
|     |     |     |     |     |     |     |     | tion with | poor | visual quality | of  | a sequence). | Fig. | 9 shows | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | -------------- | --- | ------------ | ---- | ------- | --- |
bitratedescendforquantizationparameterincreasingfrom30
upto50.ThesteepdecreaseofbitratearoundQP30isgetting
flatterforQPvaluescloseto50,whichisquitenaturalasthere
|     |     |     |     |     |     |     |     | is a certain | amount | of         | information    | in the    | encoded | bitstream    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ---------- | -------------- | --------- | ------- | ------------ | --- |
|     |     |     |     |     |     |     |     | carrying     | data   | other than | just quantized | transform |         | coefficients |     |
(e.g.,predictionmodesignalization,motionvectorvalues,etc.).
|     |     |     |     |     |     |     |     | It is       | obvious | from Figs. | 7–9           | that the   | curves   | in each   | plot     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ---------- | ------------- | ---------- | -------- | --------- | -------- |
|     |     |     |     |     |     |     |     | are very    | similar | even       | for different | content.   |          | This fact | is a     |
|     |     |     |     |     |     |     |     | consequence | of      | putting    | the relative  | bit        | rates on | the       | ordinate |
|     |     |     |     |     |     |     |     | instead     | of the  | absolute   | values,       | which vary | greatly  | depending |          |
onthespatiotemporalpropertiesofthedifferentcontents.
|     |     |     |     |     |     |     |     | The adaptation |               | dimensions | mentioned |           | in this  | section       | can    |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------- | ---------- | --------- | --------- | -------- | ------------- | ------ |
|     |     |     |     |     |     |     |     | be further     | extended      | as         | described | in [108], | where    | the           | author |
|     |     |     |     |     |     |     |     | proposes       | a three-level | model      | to        | describe  | the user | satisfaction. |        |
Apartfromtranscoding,whichisessentiallythecoreoperation
Fig.8. Adaptationthroughresolutionreduction. forHAScontentpreparation,[108]alsomentionstransmoding,
|     |     |     |     |     |     |     |     | i.e., conversion |     | among | different | modalities—audio, |     | video, | or  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----- | --------- | ----------------- | --- | ------ | --- |
alowernumberofframespersecond.Thetypicalefficiencyof
text,asanalternativeapproachtoadaptation.Anexampleofa
suchanapproachisshowninFig.7.Theoriginalframerateof transmodingimplementationcanbefoundin[109].
| a progressive-scanned |        | video      | sequence | corresponding |          | to      | 100% |     |     |     |     |     |     |     |     |
| --------------------- | ------ | ---------- | -------- | ------------- | -------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| is 25 fps             | in our | real world | example. | In            | order to | achieve | 80%  |     |     |     |     |     |     |     |     |
VI. QOEINFLUENCEOFVIDEOADAPTATIONDIMENSIONS
| of the original | bit | rate, | one needs | to reduce | the | frame | rate to |     |     |     |     |     |     |     |     |
| --------------- | --- | ----- | --------- | --------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
approximately65%.Insuchacase,motioninvideoisnolonger
Inthissection,wereviewrelatedworkwithrespecttoQual-
perceived as smooth and the perceived quality degradation is ity of Experience of HTTP adaptive streaming. Therefore, we
significant[107]. mainlyfocusonstudiesbasedonsubjectiveusertestsasthese
| Resolution | based | bit | rate adaptation | decreases |     | the number |     |           |     |               |     |                 |     |        |      |
| ---------- | ----- | --- | --------------- | --------- | --- | ---------- | --- | --------- | --- | ------------- | --- | --------------- | --- | ------ | ---- |
|            |       |     |                 |           |     |            |     | represent | the | gold standard | for | QoE assessment. |     | Please | note |
of pixels in the horizontal and/or vertical dimension of each thatmostofthesestudiesarenotspecificallydesignedforHAS,
videoframe.Thecorrespondingefficiencyofsuchanapproach but the results are transferred where possible. However, some
| is shown | in Fig. | 8.1 The | steeper descend |     | (compared | to  | Fig. 7) |     |     |     |     |     |     |     |     |
| -------- | ------- | ------- | --------------- | --- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
generalissuesstillremainwhicharenotaddressedbyresearch
of the curves is quite advantageous—even a small decrease of so far, e.g., long video QoE tests in the order of 10 minutes,
frameresolutionleadstoasignificantreductionofrequiredbit
whichisatypicaldurationforuser-generatedcontent.
rate(e.g.,80%oftheoriginalbitratesisachievedbydecreasing Several works (e.g., [118]–[120]) conclude that there is a
theframesizetoapproximately85%inbothdirections). content dependency regarding quantitative effects of adapta-
| Quantization |     | based | bit rate adaptation |     | adjusts | the | lossy |                  |     |             |          |             |     |        |       |
| ------------ | --- | ----- | ------------------- | --- | ------- | --- | ----- | ---------------- | --- | ----------- | -------- | ----------- | --- | ------ | ----- |
|              |     |       |                     |     |         |     |       | tion. Especially |     | spatial and | temporal | information |     | of the | video |
source encoder in order to reach the desired bit rate. In clips determine how the effects of adaptations are perceived.
H.264/AVC,theavailablevaluesofthequantizationparameter
|     |     |     |     |     |     |     |     | Thus, in | this | section no | absolute | results | can be | presented | as  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ---------- | -------- | ------- | ------ | --------- | --- |
(QP) are between 0 (losslesscoding) and 51 (coarse quantiza- they differ for each single video, but the main focus will be
thepresentationofgeneral,qualitativeeffectsofadaptationon
1Resolutionwaschangedinboththeverticalandthehorizontaldimension QoE. Thereby, the different adaptation dimensions and their
inordertokeeptheaspectratiounchanged. respective influence will be outlined first, and links to QoE

| SEUFERTetal.:SURVEYONQUALITYOFEXPERIENCEOFHAS |     |     |     |     |     |     |       |     |     |     |     |     |     |     | 481 |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                               |     |     |     |     |     |     | TABLE | IV  |     |     |     |     |     |     |     |
MAINQOEFINDINGSOFSINGLEDIMENSIONADAPTATION.MOREREFERENCESCANBEFOUNDINTHEDETAILEDDESCRIPTIONINSECTIONVI
models will be provided. A summary of this survey can be coded bit rate and subjective video quality for H.264, stating
found in Table IV, but more details are given in the following that with increasing bit rate the video quality increases but
threesubsections.Afterwards,trade-offsbetweenthedifferent eventually saturates. Thus, a further increase of bit rate does
dimensionswillbehighlighted.Thus,thissectionwillprovide notresultinahigherperceivedquality.
valuable guidelines when selecting the adaptation dimensions ChangingthequantizationparameterofH.264videostreams
andpreparingthecontentforaHASstreamingservice. is in the focus of [14]. The authors find that QoE falls slowly
|     |     |     |     |     |     |     |     | when the  | quantization |           | parameter | starts | to increase, | i.e., | the    |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --------- | --------- | ------ | ------------ | ----- | ------ |
|     |     |     |     |     |     |     |     | video bit | rate         | decreases | and the   | image  | quality      | gets  | worse. |
A. ImageQualityAdaptation
Onlyafterreachingahighquantizationparametertheperceived
| Reference | [112] | finds | that | the perceptual |     | quality | of a de- |     |     |     |     |     |     |     |     |
| --------- | ----- | ----- | ---- | -------------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
qualitydropsfaster.Reference[112]findsthatinordertoreach
codedvideoissignificantlyaffectedbytheencodertype.They
|         |           |      |          |     |         |          |      | a good | or excellent | QoE | the pixel | bit | rate should | be  | around |
| ------- | --------- | ---- | -------- | --- | ------- | -------- | ---- | ------ | ------------ | --- | --------- | --- | ----------- | --- | ------ |
| confirm | work from | 2005 | in which | the | authors | of [121] | show |        |              |     |           |     |             |     |        |
0.1bitsperpixelwhenH.264isused.Ifotherinformationlike
that the video quality produced by the H.264 codec is the framerateorframesizeareunavailable,pixelbitratecanserve
mostsatisfying,ratedhigherthanRealVideo8andH.263.Also
asaroughquantitativegaugeforQoE.
| for low         | bit rates | H.264      | outperforms | H.263  | and    | also       | MPEG-4 |              |           |        |             |           |               |           |         |
| --------------- | --------- | ---------- | ----------- | ------ | ------ | ---------- | ------ | ------------ | --------- | ------ | ----------- | --------- | ------------- | --------- | ------- |
|                 |           |            |             |        |        |            |        | Reference    | [129]     | uses   | linear      | models    | and per-chunk | metrics   |         |
| [122]. However, |           | more       | advanced    | codecs | like   | H.265/HEVC |        |              |           |        |             |           |               |           |         |
|                 |           |            |             |        |        |            |        | to predict   | the       | MOS of | video       | sequences | with          | image     | quality |
| [123]–[125]     | and       | VP9 [126], | [127]       | will   | become | relevant   | for    |              |           |        |             |           |               |           |         |
|                 |           |            |             |        |        |            |        | adaptations. | Reference |        | [111] shows | that      | the           | perceived | quality |
HASinthenextyears. of HTTP video streams with dynamic quantization parameter
| The fact   | that | the encoder | type  | significantly |           | affects | QoE      | is         |     |              |     |          |         |              |     |
| ---------- | ---- | ----------- | ----- | ------------- | --------- | ------- | -------- | ---------- | --- | ------------ | --- | -------- | ------- | ------------ | --- |
|            |      |             |       |               |           |         |          | adaptation | can | be predicted | by  | temporal | pooling | of objective |     |
| also shown | for  | scalable    | video | codecs        | in [120], | which   | investi- |            |     |              |     |          |         |              |     |
per-framemetrics.Theauthorsstatethatasimplemethodlike
gates adaptation with H.264/SVC and wavelet-based scalable the mean of quality levels of a HAS video sequence delivers
| video coding. | Reference |     | [56] proposes |     | an improved |     | approach |     |     |     |     |     |     |     |     |
| ------------- | --------- | --- | ------------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
alreadyverydecentpredictionperformance.
forencodingandsegmentationofvideosforadaptivestreaming Thereviewedworkssuggestthatforvideostreamingingen-
| using H.264, | which | reduces | the | needed | bit rate | by up | to 30% |     |     |     |     |     |     |     |     |
| ------------ | ----- | ------- | --- | ------ | -------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
eralthevideoencoderhasasignificanteffectontheperceived
withoutanylossinquality.Conversely,thismeansthatbyusing
|     |     |     |     |     |     |     |     | quality. | Thus, | the usage | of H.264 | is  | currently | recommended |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --------- | -------- | --- | --------- | ----------- | --- |
their approach, the video can be encoded with a higher image also for HAS. For the highest quality layer, the QP can be
qualityforthesametargetbitrate.
|     |     |     |     |     |     |     |     | adjusted | such that | good | or excellent | video | quality | is reached |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---- | ------------ | ----- | ------- | ---------- | --- |
In [98], the performance of both H.264 and MPEG-4 is with minimal bit rate. When adapting the image quality, an
| investigated | under | different | mobile | network | conditions |     | (WiFi |          |        |          |         |          |            |     |     |
| ------------ | ----- | --------- | ------ | ------- | ---------- | --- | ----- | -------- | ------ | -------- | ------- | -------- | ---------- | --- | --- |
|              |       |           |        |         |            |     |       | increase | of the | QP leads | to only | slightly | decreasing | QoE | in  |
andHSDPA)andvideobitrates.Therefore,theauthorsimple-
|     |     |     |     |     |     |     |     | the beginning. |     | Together | with the | convex | shape | of Fig. | 9, it |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | -------- | ------ | ----- | ------- | ----- |
menttheirownon-the-flyvideocodecchangeoverandbitrate follows that HAS can utilize image quality adaptation by a
switchingalgorithm.WithWiFiconnection,H.264isperceived
smallincreaseofQPinordertosignificantlyreducethebitrate
betterthanMPEG-4especiallyforlowvideobitrates.Incon-
whileintroducingarathersmalldegradationofQoE.However,
trast,withHSDPAconnection,MPEG-4yieldsbetterresultsfor
highQPsleadtopoorvideoqualityandshouldbeavoided.
allbitrates.AchangeofcodecduringplaybackfromH.264to
MPEG-4alwaysdegradestheuserperceivedquality.However,
|     |     |     |     |     |     |     |     | B. SpatialAdaptation |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
achangeintheotherdirectionisperceivedasanimprovement
for low bit rates. Furthermore, the authors find that a bit rate References[114]and[130]findthatspatialresolutionisthe
decrease,i.e.,adecreaseofimagequality,resultsinadecreased key criterion for QoE for small screens. Low resolutions con-
quality, but a bit rate increase is not always better for QoE as tributetoenhancedeyestrainofthesubjects.However,accept-
theswitchitselfmightbeperceivedasanimpairment. abilityofspatialresolutionsisalsotiedtoshottypes(e.g.,long
References[110],[113],and[128]investigatedifferentvideo shot, close-up). Reference [112] finds that, in general, higher
bitratesfordifferentcodecsandshowthatanincreasedvideo MOSisassociatedwithhigherspatialresolution.However,they
bit rate leads to an increased video quality. In particular in showthatforthesamevideobitrate,avideowithhigherspatial
[113], a logistic function describes the relationship between resolution is perceived worse. This is due to a lower pixel bit

482 IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015
rate value (cf. Section VI-A) which causes severe intra-frame complexlinkbetweenunderstandingandperception,i.e.,users
degradationsespeciallyforsequenceswithlargespatiotemporal have difficulty to absorb audio, video, and textual information
activities.In[116],theimpactofresolutiononsubjectivequal- concurrently.Thus,highlydynamicclipsforwhichitisdifficult
ity is investigated by comparing high definition (HDTV) and toassimilateallinformation,suchassportsoractionclips,are
standarddefinitiontelevision(SDTV)sequences.Theyfindthat unaffected by reduced frame rate. On the other hand, a static
QoE increases with increasing resolution for slightly distorted newsclip,whichcanbeunderstoodeasilyasthemostimportant
images.However,largerimagesizebecomesadrawbackwhen information is delivered by audio, suffers from reduced frame
the level of distortion increases as artifacts are more prevalent rate because the lack of lip synchronization is clearly visible.
andvisibleinHDTV.Inthiscase,observerstendtopreferSD Also [132] reconfirms the findings that a reduction of frame
asthisreducesthevisualimpactofthedistortions. rate has only little impact on high motion videos. Reference
In [115], a model for mapping resolution to MOS is pre- [133]confirmsthesefindingsinastudyonMPEG1subjective
sented. The considered resolutions range from SD to SQCIF. quality which additionally takes into account packet loss, and
TheauthorsshowthatMOSisalinearfunctionofthelogarithm states that the MOS is good if the frame rate is more than
oftheresolution,spatialinformation,andtemporalinformation. about 10 frames per second (fps). More recently, [134] states
Moreover, they find that temporal information is more impor- that the threshold of subjective acceptability is around 15 fps.
tantthanspatialinformationfortheirmodel. Reference [135] finds that the optimal frame rate for a given
As the display capability limits the displayed resolution, bit rate depends on the type of motion in a sequence. They
HAS should first adjust the delivered spatial resolution to the findthatvideoswithjerkymotionbenefitfromincreasedimage
enduser’sdeviceinordertoavoidtransmissionofunnecessary quality at lower frame rates. Clips with smoother (i.e., less
data. A linear relation of resolution reduction and bit rate jerky)motionaregenerallyinsensitivetochangesinframerate.
savings(seeFig.8)canbeobserved.Theimpactofadaptation Reference [28] finds that only for very low frame rates the
by resolution reduction depends mainly on the content and quality decreases as the impairment duration increases. For
the device, but in general, resolution reduction leads to a medium or high frame rates the quality is similar whether the
lower image quality, and thus, to a lower QoE. However, in frameratereductionoccursduringtheentirevideoorduringa
combination with image quality adaptation, spatial adaptation shortpartofthevideo.Thus,theystatethatthereisnoquality
can even be beneficial for HAS. In particular, decreasing the gainbyre-increasingframerateafteratemporarydrop.
image size when image quality is poor can help in order to In [115], a model for mapping frame rate to MOS is given.
obfuscateartifacts. MOScanbeexpressedasalinearfunctionofthelogarithmof
frame rate and spatial information. Adding temporal informa-
tiondoesnotimprovethemodelperformance.
C. TemporalAdaptation
The presented studies show that, in general, a lower frame
In [117], the effect of frame dropping on perceived video rate leads to lower QoE. However, the impact of temporal
quality is investigated and a model for predicting QoE is pro- adaptationdependsheavilyonthevideocontent.Consequently,
posed.Itisshownthatframedroppinghasanegativeimpacton HAScantakeadvantageofframerateadaptationespeciallyfor
QoEandthequalityimpairmentdependsonmotionandcontent highmotioncontentwheresmallframeratereductionsareless
ofthesequence.Moreover,theauthorsfindthatperiodicframe visible. Drawbacks for HAS are that the frame rate cannot be
dropping, i.e., decrease of frame rate, is less annoying than reduced too much until the video quality is perceived as bad,
an irregular discarding of frames. Note that stalling, i.e., a andthebitratesavingsintherelevantrangearesmallcompared
playout interruption by delaying or skipping the playout of totheotherdimensions(cf.Fig.7).
several consecutive frames, can also be considered a temporal
adaptation. However, the QoE impact of stalling is already
D. Trade-OffsBetweenDifferentAdaptationDimensions
discussed in Section II-B, and HAS primarily tries to avoid
stalling. Therefore, this section focuses on the reduction of The three dimensions presented not only allow for single
frame rate as a means of temporal quality adaptation, which dimension adaptation but also for combined quality changes
hasalessnegativeimpactonQoEthanstalling[28]. in multiple dimensions. Several studies consider trade-offs
Reference [131] investigates the influence of frame rate on between different adaptations and are be presented in this
theacceptanceofvideoclipsofdifferenttemporalnature(e.g., section.TableVsummarizesthemainfindingsandlinkstothe
still image, fast motion) and different importance of auditory correspondingworks.
and visual components (e.g., music video, sport highlights). Reference [94] claims that there exists an encoding which
The authors show that reducing the frame rate generally has maximizestheuser-perceivedqualityforagiventargetbitrate
a negative influence on the users’ acceptance of the video which can be extended to an optimal adaptation trajectory for
clips. However, low temporal videos, i.e., videos with little a whole video stream. In their work, the authors focus on the
motion, are affected more by lower frame rates than high adaptationofMPEG-4videostreamswithinatwo-dimensional
temporal videos. This finding is confirmed by [118] which adaptation space defined by frame rate and spatial resolution.
investigates different frame rates for dynamic content. They They show that a two-dimensional adaptation, which reduces
show that reducing the frame rate generally leads to a lower both resolution and frame rate, outperforms adaptation in one
usersatisfaction,butitdoesnotproportionallyreducetheusers’ dimension. Comparing clips of similar average bit rates, it is
understanding and perception of the video. Instead they find a shown that reduction of frame rate is perceived worse than

SEUFERTetal.:SURVEYONQUALITYOFEXPERIENCEOFHAS 483
TABLE V
TRADE-OFFSBETWEENDIFFERENTADAPTATIONDIMENSIONS.A(cid:2)BMEANSTHATDIMENSIONAISMOREIMPORTANTTHANDIMENSIONB,I.E.,
ADEGRADATIONOFAISWORSETHANADEGRADATIONOFB.FOREXAMPLE,STALLINGWASSHOWNTOBEAWORSEDEGRADATION
THANADAPTATION(STALLING(cid:2)ADAPTATION).NOTETHATSOMERESULTSFROMTHESURVEYEDWORKSARECONTRADICTORY
ANDMIGHTDEPENDONTHEVIDEOTYPE.INTHESECASES,INFORMATIONONTHEVIDEOTYPESAND
REFERENCESTOTHESTUDIESCANBEFOUNDINTHESECONDCOLUMN.MOREDETAILS
ONTHETRADE-OFFSAREPRESENTEDINSECTIONVI-D
reduction of resolution. In [119], the authors research optimal framerateshouldbedecreased.Athighbitrates,framerateis
combinations of image quality and frame rate for given bit moreimportantandpixelbitrateshouldbedecreasedtoachieve
rates. They find that until image quality improves to an ac- a high perceived quality. Reference [112] maximizes the QoE
ceptablelevel,itshouldbeenhancedfirst.Onceitisimproved by selecting an optimal combination of frame rate and frame
adequately, temporal quality should be improved. Especially sizeunderlimitedbandwidth,i.e.,videobitrate.Theyfindthat,
spatially complex videos require a high image quality first, in general, resolution should be kept low. For videos with a
while videos with high camera motion require a higher frame high frame difference and variance, also frame rate should be
rate at a lower bit rate. Also in [138], for a given bit rate low (which implies a high pixel bit rate). Instead, frame rate
trade-offsbetweenframerateandimagequalityarepresented. should be high for content with low temporal activity in order
A trend is found that for decreasing video bit rate also the toachieveahighQoE.
optimal frame rate decreases. The authors show that for dif- ThemajorfindingsforHAScanbesummarizedasfollows.
ferentvideobitratesthereexistswitchingpointswhichdefine First, an adaptation in multiple dimensions is perceived as
multiplebitrateregionsrequiringadifferentoptimalframerate better than a single dimension adaptation. Second, for most
foradaptation.Reference[136]investigatestrade-offsbetween content types image quality is considered the most important
frame rate and quantization for soccer clips. The authors find dimension.Thus,reducingimagequalitytoomuchwillleadto
that participants were more sensitive to reductions in frame bad QoE. This effect can be mitigated by reducing the image
qualitythantoreducedframerate.Especiallyforsmallscreen size at the same time to make artifacts less visible. Third,
devices, a higher quantization parameter removes important a high frame rate is important especially for content where
information about the players and the ball. In contrast, a low jerkiness is easily visible (e.g., low motion content). Finally,
frame rate of 6 fps is accepted 80% of the time although resolutionadaptation,whichiscloselyrelatedtoimagequality
motion is not perceived as being smooth. The experimental adaptation,istheleastimportantdimensioninmostcases.Note
results obtained by [139] show that image quality is valued that the impact of upscaling, which is a prevalent reaction of
higher by test users (which were able to choose which dis- video players to reduced resolution and was inherent in the
tortion step they preferred) than temporal resolution of the reviewedstudies,dependsonthespecificplayerandcouldnot
content for low bit rate videos. Reference [137] confirms that beassessedinoursurvey.
for fast foreground motion like soccer reducing frame rate is
preferred to reducing frame quality. However, for fast camera
VII. QOEDEGRADATIONSINASHAREDNETWORK
or background motion a high frame rate is better because dis-
turbing jerkiness can be detected more easily which results in Withinthissectionwediscusschallengesthatarisefromthe
lowerQoE. interplaybetweenHASplayerinstancesandotherapplications
In[132],trade-offsbetweenresolutionandframequalityare that share the network. We thereby concentrate on effects that
investigated.Theyfindthatasmallresolution(withoutupscal- impairQoEofnetworkedapplicationsbeyondvideoplayback.
ing)andhighimagequalityispreferredtoalargeresolutionand Thisdiscussionincludesseveralnetworkrelatedissuesthatarise
lowframequalityforagivenbitrate.Reference[120]compares from the particular behavior of video adaptation algorithms
different combinations of resolution, frame rate, and pixel bit established in HAS clients, and their interplay with network
rate, which result in similar average video bit rates. They find level optimization algorithms. Within Section III-B, this inter-
that at low bit rates a larger resolution is preferred, and thus, play between application level control loop and network level

484 IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015
controlloophasalreadybeenintroducedanddepictedinFig.6. bit rates, and a large number of quality switching events for
Typically such an interplay can introduce numerous different thesecondclient,respectively.Asimilarfindingisreportedin
issues, especially as more network level control loops beyond [96]wherealargernumberofHASclientinstancesalsoresults
TCP can be involved, e.g., in wireless networks. However, inincreasingqualityoscillationsforalloftheseinstances.The
we not only address those issues that affect QoE relevant problemofthedelayrequiredtoconvergetothefinalbitrateis
dimensions of HAS client instances, as discussed in previous also associated to a high number of quality adaptation events.
sections,butalsopossibleQoEimpactsonotherapplicationson This impacts especially short viewing sessions like 2–3 min
thenetwork.Ouraiminthissectionistoidentifytheaforemen- clips where the client will not reach the maximum available
tioned issues and the resulting impairments on an application bitrateduetotheabovedescribedbehavior(cf.[140]).
level,hencewedonotgointoprotocolornetworkleveldetails Anotherchallengeassociatedwiththebehaviorofcompeting
in terms of a detailed root cause analysis for these problems. playersisfairnessbetweendifferentHASclients.Ifoneplayer
Therefore, this section is very selective in terms of network on network bottleneck grasps a large share of the bandwidth
issues and hence incomplete. A more thorough discussion of before the other players join the stream it will be privileged
network related HAS problems can be found in [88] and [91]. throughoutitswholestreamingsessionwhiletheotherplayers
The problems described here reach beyond pure video based onthenetworkcompetefortheremainingbandwidthasshown
quality,astheyalsotackleavailabilityandstabilityofthesingle in [88], [140]. With a rising number of competing clients the
network connection the respective HAS client is utilizing, as unfairnessincreases[96].Theauthorsin[88]haveshownthat
wellastheutilizednetworkinfrastructureatlarge.Wefirstdis- this behavior is not based on TCP’s well known unfairness
cuss issues between concurrent network entities (HAS clients, toward connections of different round trip times, but rather a
other networked applications), and second describe actionable resultofthecompetingHASclientinstances.
measuresthataimtocountertheseissues. In addition to the abovementioned problems, network uti-
lization within the bottleneck network is also impacted by
competing HAS client instances. Results in [142] identify
A. InteractionsBetweenNetworkEntities
conservativestrategiesinthestream-switchinglogicaswellas
For the discussion of interactions between network entities in the buffer controller as a major source of network under-
and resulting issues, we distinguish two types of network utilization for multiple client instances. This is in line with
entities: HAS client instances and other applications utilizing resultsdescribedin[141]and[143]thatreportnetworkunder-
the same network. After this distinction, the following inter- utilization as a result of video quality oscillation due to com-
actions are discussed: Between different HAS clients, other petingplayerinstances.
applicationsonHASclientinstances,andHASclientinstances Altogether, these three problems of stability, fairness, and
on other applications. In addition, HAS client instances may bandwidth utilization do in turn influence QoE of HAS from
alsointerferewiththeTCPprotocolasdiscussedattheendof anenduserperspective.First,frequentqualityoscillationsdue
thissubsection. to instability have already been shown to degrade QoE (cf.
1) Interactions Between HAS Players: If several adaptive SectionIV).Andsecond,lowvideoqualitylevelsasaresultof
players share a network connection, the following questions unfairbehaviororlownetworkutilizationdodecreaseresulting
havebeenidentified(cf.[88])tobeofparticularinterest: videoQoE(cf.SectionVI).
(cid:129) Cantheplayerssharetheavailablebandwidthinastablema- 2) InteractionsBetweenOtherApplicationsandHASPlay-
nner,withoutexperiencingoscillatorybitratetransitions? ers: The impact of other applications on the quality of HAS
(cid:129) Cantheysharetheavailablebandwidthinafairmanner? clients has not been widely addressed yet. Investigations in
(cid:129) Is bandwidth utilization influenced by competing HAS this area discuss basic effects of parallel file downloads or
clientinstances? browsing on the HAS control loop. Segments are downloaded
One major issue for competing HAS players within a net- sequentially with iterative decisions which segment quality to
workisstability(intermsofqualitylevels)andthefrequency downloadnext.Conservativedecisions,aswellastheadditional
of switching events. Several studies reveal that more frequent delayintroducedbythecontrolloopmayresultinareduceduti-
quality switching is invoked when more than one instance of lizationofthenetworkresources,andthus,alessthanpossible
HAS clients compete for bottleneck bandwidth [88], [140], video quality [85]. This effect is amplified in case of parallel
[141]. Depending on the amount of available bandwidth and downloads. Depending on the specific implementation of the
the time the different players join the stream the reaction is HAScontrolalgorithm,particularlyonitsaggressiveness,less
different.In[88],theauthorsshowthatinatwoplayersetupthe thanthefairshareoftheresourcesisused[144].Hence,parallel
clientjoiningthestreamfirstgrabsthehighestavailablevideo downloads account for more network resources resulting in a
bandwidth the network supports. Following, the second client worsethannecessaryqualityofthevideostream.
joiningstartswithalowvideobandwidthandtriestoincrease Other applications with different traffic patterns like web
its video bandwidth subsequently. However, the throughput browsing, gaming, or voice and video conferencing have not
needed for the higher video bandwidth cannot be provided by been investigated in this context. Hence, to foster a better
the network as the first client utilizes this bandwidth already. understanding of the impact of multiple applications on the
Hence, the buffer level of the second client depletes, and the HAScontrolloop,additionalresearchisrequired.
video adaptation algorithm switches to a lower video bit rate. 3) Interaction Between HAS Players and Other Applica-
This leads to a permanent oscillation between different video tions: BeyondtheabovediscussedinfluenceofdifferentHAS

SEUFERTetal.:SURVEYONQUALITYOFEXPERIENCEOFHAS 485
clients amongst each other, there is also the problem of their tation set and related properties, such as segment sizes (cf.
influence on other applications using the network connection. Section III-C), which can influence fairness and network uti-
One of the main problems arising is the interaction between lization, and b) solutions that either actively select the chunk
aggressiveHASclients,whichperiodicallyrequestssmallfiles levelsthataredeliveredtotheplayerorinterfereonTCPlevel.
(videosegments)overHTTP.ThiscausesTCPtooverestimate Within this section, we concentrate on the latter approaches
thebandwidthdelayproductofthetransmissionlineandresults and cross-reference to Section III-C for adaptation set related
in a buffer bloat effect as shown in [145] and [146], which in countermeasures.
turn leads to queuing delays reaching up to one second and Intermsofactiveselectionofchunklevelsontheserverside,
being over 500 ms for about 50% of the time. Having a one [151] propose an algorithm that maximizes global perceptual
wayqueuingdelayclosetoonesecondseverelydegradesQoE qualityintermsofvideobitratewithrespecttothebandwidth
of cloud services [147], [148] and real-time communications constraintsforallclientsonthenetwork.Toachievethat,they
services,suchasVoIP[149]andvideotelephony[150].Hence, connect bitrate or quality level information with bandwidth
it is almost impossible to use the bottleneck link for anything availabilityandthendecidewhichchunklevelsareofferedfor
else but video transmission or large file downloads as shown a certain client instance. Thereby, they improve stability and
in [146]. This is particularly concerning as [145] showed that networkutilization.Theapproachproposedby[152]identifies
activequeuemanagement(AQM)techniques,awidelybelieved quality oscillations based on the client requests. When oscil-
solution to this problem, do not manage to eliminate large lationsaredetected,therelatedserversidealgorithmlimitsthe
queuingdelays. maximum chunk level available to the client in order to stabi-
4) InteractionsBetweenHASPlayersandTCP: Theprevi- lizethestreamqualitylevel.Similartotheaforementionedap-
ous sections highlighted the interaction between HAS clients proach,thisresultsinimprovedstabilityandnetworkutilization.
andbetweenHASclientsandotherapplications.Besidesthat, In contrast, the authors in [153] propose to place an upper
the HAS control loop on application layer may also interfere bound on the TCP congestion window on the server side in
with the TCP control loop resulting in performance issues ordertocontroltheburstinessofadaptivevideotraffic.Asare-
without any other application. A TCP data transfer can be sult,packetlossesandroundtriptimedelaysarereduced,which
segmented into three phases [143]. In the initial burst phase, positivelyaffectsnotonlyHASbutalsootherapplicationsthat
thecongestionwindowisfilledquicklyresultinginaggressive sharethenetworkbottleneck.
probingtoestimatethecurrentcongestionlevel.Oncethewin- Overall,themeasuresdiscussedwithinthissectiondotackle
dowisfull,thesenderwaitsforacknowledgmentpackets.Inthe issues arising from interactions between different HAS in-
secondphase,theACKclockingphase,thecongestionwindow stancesaswellasinteractionsbetweenHASinstancesandother
increases slowly and most of the packets are transmitted upon applications.
receiving an ACK packet. TCP mechanisms like fast recovery 2) Network Based Approaches: Purely network based ap-
and fast retransmission are fully working. In the third phase, proaches that overcome the previously mentioned limitations
the trailing ACK phase, the sender waits for the final ACKs, are sporadically discussed in literature. In [154], the authors
andfastretransmissionscannotbeusedtonotifythesenderon propose a flexible redirection of HAS flows using Software-
corruptedorlostpackets. DefinedNetworking(SDN)tooptimizethevideoplayoutqual-
Theperformanceofthedatatransmissionispronetopacket ity. Reference [155] proposes to use Differentiated Services
lossesinthefirstphase.Duetotheaggressivepacketprobing, (DiffServ) to guarantee the video delivery. TCP rate shaping
multiplepacketlossesmayoccurresultinginadelayeddelivery on a per flow level is introduced in [156] as one possibility to
of packets to the HAS client, and thus, a too conservative explicitlyallocateresourcestospecificvideoflows,andthus,to
decisionwhichqualitytopick.Inphasethree,additionaldelays enhancetheQoEfortheinvolvedclients.
maybeinduced.Sincefastretransmissionmaynotbeused,the To conclude, the existing work mainly aims at optimizing
packet timeout has to expire before a packet is retransmitted the video quality for HAS clients and the investigation of
resultinginlessthroughputinthisphase. interactions with other HAS clients and applications is not
Due to the start-and-stop nature of HAS induced by the addressedindetailyet.
client-based control loop, more time is spent either in phase 1 3) Proxy and Client Based Approaches: A purely client
or phase 3. Control delays may further result in an imprecise based solution is described in [157]. The proposed client so-
knowledge of the current congestion level in the network, a lution does not request chunk levels (equivalent to a certain
higher experienced packet loss, and thus, a lower throughput video bitrate) based on an available throughput estimation on
thantheoreticallypossible. the client side. Instead, the client buffer evolution over time
is calculated and chunk levels are requested based on the
relation of the current buffer level to a reference buffer level.
B. Countermeasures
Performanceresultsshowthatstabilityandnetworkutilization
In the preceding paragraphs, problems due to entities com- are increased compared to commercial HAS client implemen-
peting for a bottleneck link have been identified. Within this tationsthatutilizethroughputestimationfordeterminingchunk
section,wediscusshowsuchproblemscanbecounteractedin levelsrequested.
differentnetworklocations. In contrast, the solution of [105] introduces a proxy server
1) Server Based Approaches: On the server side, one can thatmonitorsrequestedqualitylevelsofallclientflowspassing
distinguish: a) Solutions related to properties of the adap- through. This monitoring allows the proxy to identify the

486 IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015
fairness distribution over the connected clients. In case clients anddelivertheservice.Thus,wewillconsidertheperspectives
with unfair shares of network throughput usage are identified, of these stakeholders, and present their goals and remaining
theproxylimitsavailablechunklevelstotheleveloftheother challenges with respect to the QoE of HTTP adaptive video
| clientsandtherebyachievesfairnessacrossconnectedclients. |     |           |           |       |           |         | streaming:   |     |          |     |            |     |              |     |
| -------------------------------------------------------- | --- | --------- | --------- | ----- | --------- | ------- | ------------ | --- | -------- | --- | ---------- | --- | ------------ | --- |
| A combination                                            |     | of client | and proxy | based | solutions | is pro- |              |     |          |     |            |     |              |     |
|                                                          |     |           |           |       |           |         | A. Algorithm |     | designer | and | programmer |     | implementing | the |
posed in [158] and [159]. The approach of [158] identifies HASsolutioninSectionVIII-A
each client’s chunk level requests and calculates a median B. Network/InternetserviceproviderinSectionVIII-B
chunk level utilized in the network. This information is then C. Videoservice/platformproviderinSectionVIII-C
distributedtotheattachedclients,whichallowsthemtoidentify
theirownchunklevelincomparisontootherclients.Basedon
A. HASAlgorithmDesignerandDeveloper
| this, they | adjust | future requests | such | that | a fair distribution | of  |     |     |     |     |     |     |     |     |
| ---------- | ------ | --------------- | ---- | ---- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
networkresourcesisachieved.Thesolutiondescribedin[159] GoalsandMainInterests: ThemaingoaloftheHASalgo-
|     |     |     |     |     |     |     | rithm designer |     | and developer |     | is to | provide | optimal QoE | for |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | --- | ----- | ------- | ----------- | --- |
actsslightlydifferentastheclientbufferlevelsaresharedwith
the proxy server, which then offers a certain range of chunk videostreamingandtomonitortheresultingQoEattheclient
levelsbasedontheaccordingbufferlevels.Forbothsolutions, side. Thereby, relevant QoE influence factors on different lev-
|             |          |       |              |     |              |            | els (system, | content, | user, | context) |     | are of | interest. Client-side |     |
| ----------- | -------- | ----- | ------------ | --- | ------------ | ---------- | ------------ | -------- | ----- | -------- | --- | ------ | --------------------- | --- |
| performance | analysis | shows | that network |     | utilization, | stability, |              |          |       |          |     |        |                       |     |
andfairnesscanbeincreasedcomparedtonetworkscontaining QoE monitoring allows direct feedback and the integration
|             |              |                 |                      |       |            |             | into the        | HAS | algorithm | in  | order to | optimize | the QoE | of an |
| ----------- | ------------ | --------------- | -------------------- | ----- | ---------- | ----------- | --------------- | --- | --------- | --- | -------- | -------- | ------- | ----- |
| standard    | HAS clients. |                 | Further improvements |       | exploiting | the         |                 |     |           |     |          |          |         |       |
| interaction | between      | a network-based |                      | proxy | and        | HAS clients | individualuser. |     |           |     |          |          |         |       |
are presented in[160] and [161].Both approaches aim at pro- LessonsLearned:
(cid:129) Stallingistheworstdegradationandhastobeavoidedat
vidinginformationtotheHASclientstoselecttheappropriate
videoquality.In[161],availablebandwidthmeasurementsare costsofinitialdelayorqualityadaptation.
forwarded to the clients, whereas in [160], the proxy defines (cid:129) Buffersizeofafewsegmentlengthsissufficientlylargein
whichqualitylevelshallbeused.Thus,qualityfluctuationscan practicetohavelessstalling.
be reduced and the QoE between several HAS clients may be (cid:129) A holistic QoE model which describes the influences of
eachHASparameterismissing.
sharedinafairmanner.
This section has shown that, beyond pure video QoE, the (cid:129) Notonlytechnicalparametersbutalsotheexpectedqual-
egoistic behavior of current adaptive video strategies results ityperceivedbytheenduserhastobetakenintoaccount
in interactions between two feedback loops (rate-adaptation foradaptationdecisions.
logic at the application layer and TCP congestion control at (cid:129) The most dominant adaptation factor is the adaptation
amplitude.
| the transport | layer | as depicted | in  | Fig. 6). | Unstable | network |     |     |     |     |     |     |     |     |
| ------------- | ----- | ----------- | --- | -------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
conditions, an unfair distribution of network resources, and (cid:129) Algorithmsshouldplayoutthehighestpossiblequality.
under-utilizationoftheseresourcesaretheresult.Theseissues (cid:129) Adaptation frequency must not be too high to avoid
| donotonlyimpactHASclientsonthenetworkbutalsoseverely |     |     |     |     |     |     | flickering. |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
impact other applications by large queuing delays and packet (cid:129) Communication between clients and proxy may enhance
user-perceivedquality.
| losses. Countermeasures |     |     | addressing | these | issues exist | and can |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---------- | ----- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
becategorizedintoserverbased,networkbased,andproxyand (cid:129) Qualityswitcheswillbemoreorlessperceivabledepend-
client based approaches. However, each of these countermea- ing on the concrete content, the motion pattern, and the
surestacklesonlyasubsetoftheaforementionedissues,hence, selectedadaptationdimension.
researchonageneralsolutiontotheproblemisstillneeded. ChallengesandFutureWork: Theadaptationalgorithm(de-
|     |     |     |     |     |     |     | cision engine) |          | should | select | the appropriate |           | representations | in  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | ------ | ------ | --------------- | --------- | --------------- | --- |
|     |     |     |     |     |     |     | order to       | maximize | the    | QoE.   | The most        | important | decisions       | are |
VIII. KEYFINDINGSANDCHALLENGESFROMDIFFERENT
whichsegmentstodownload,whentostartthedownload,and
STAKEHOLDERPERSPECTIVES
howtomanagethevideobuffer.Ifadaptationisnecessary,the
In this section, the lessons learned and best practices are time of the quality switch should be based on the content in
summarized from the perspective of the different stakeholders ordertohidetheswitchingorresultingdegradation.Therefore,
involved in the HAS ecosystem. Throughout the survey, QoE the algorithm designer requires a proper QoE model which
was considered which reflects the end user perspective. In considers the application-layer QoE parameters that can be
general, the end user is interested in optimal QoE for video influenced by the HAS algorithm. As different types of ser-
streaming, but also an easy-to-use application, i.e., the user vice are used (video on demand, live streaming) in different
wants an app which just delivers good quality without need contexts, different algorithms (or parameter settings) have to
formanualconfigurationbeforeorduringserviceconsumption. be developed which need to be adjusted accordingly to the
Further,additionalenduseraspectslikeenergyconsumptionof service requirements. Therefore, QoE and context monitoring
smartphonesortheusedclientbandwidthareofinterest. has to be implemented and the monitored parameters need to
However,theenduserisapureconsumerofthevideoservice beintegratedinthealgorithms’adaptationdecision.
and cannot influence or interact with the service (although di- SomeoftheQoEinfluencefactorscanbemeasureddirectly
rectfeedbackmightbeconsideredinthefuture).Theresulting at the client side, e.g., system level parameters related to ap-
videoservicequalitydependsonthestakeholders,whichoffer plicationlevel(initialdelay,stalling,representationswitching)

SEUFERTetal.:SURVEYONQUALITYOFEXPERIENCEOFHAS 487
or related to device capabilities and screen resolution. Other sioning, but also for traffic management to avoid QoE prob-
influencefactorslikecontentlevelparameters(e.g.,usedvideo lems and resulting customer churn. Therefore, it is relevant
codec) or context level parameters (e.g., popularity) might be to know which parameters to measure for QoE prediction or
obtained directly from the video platform. Additionally, user to foresee networking problems, and how to monitor those
preferences should be taken into account, as some users, for parameterstechnically(onwhichtimescales,onwhichnetwork
example, may prefer a very low resolution for news or other elements, etc.). Existing measurement methodologies (e.g.,
contentinsteadofreducedframerate.Includingdirectfeedback [165] for YouTube QoE in 3G networks), the accuracies of
intotheadaptationdecisionsmayovercomethisproblem,how- each approach, and the costs/efforts for the implementation
ever,activationofusersandpossiblycheating/selfishbehavior andoperation(CAPEX/OPEX)arehighlyrelevantfornetwork
hastobetackled. providers,butwouldconstituteanownsurvey.
Current HAS algorithms are implemented in a network ag- TheQoEmonitoringresultsneedtobealignedwithconcrete
nostic fashion (i.e., there is no direct information about the traffic management mechanisms (e.g., routing, caching) and
network conditions) and try to estimate/predict the network service provisioning (e.g., dynamic bandwidth allocation, pri-
situation in the near future. Interfaces which allow an infor- oritization).Additionally,trafficfairnessandnetneutralityhave
mation exchange between application and network to specify to be taken into account, which is a non-trivial problem from
service demands or to specify the network situation could be a technical and law perspective. New traffic management ap-
beneficial. The additional information from the network layer proaches,whichintegrateinformationfromQoEmeasurements
canbeutilizedbythealgorithmtoadjusttheadaptation.Going butpossiblyalsofromotherstakeholders,havetobedeveloped
one step beyond, whole cross-layer solutions (cf. Economic to help network providers deliver a high service quality while
TrafficManagementsolutionsforCDNservices[162])canbe reducingtheirexpenses.
beneficialforallstakeholdersandcouldberealized,forexam-
ple,byApplication-LayerTrafficOptimization(ALTO,[163])
C. VideoServiceProviderPerspective
or the northbound interface of Software-Defined Networking
(SDN,[164]). Goals and Main Interests: The main goals of the video
service provider are optimal QoE and fairness for its end
users.Thiswillleadtoagrowingnumberofcustomerswhich
B. NetworkProviderPerspective
will increase revenues. At the same time, the video service
GoalsandMainInterests: Thenetworkproviderwantstoef- providerwantstominimizecostsintermsofstorageofvideos,
ficientlyutilizenetworkresourcesandavoidunnecessarycosts, network bandwidth, and energy consumption for data centers
e.g.,inter-domaintrafficorenergyconsumptionofhisnetwork andcontentdeliverynetworks.
entities. Moreover, he wants to fulfill his SLAs and provide LessonsLearned:
good QoS but also QoE to his customers for any services (cid:129) TheusageofH.264anditssuccessorslikeH.265/HEVCis
including HAS. Therefore, the network provider is interested currentlyrecommendedalsoforHASduetoitsefficiency.
in QoE monitoring (deployed in his network) to see if there (cid:129) Multi-layer codecs allow more download flexibility since
are any problems in the network. Network dimensioning has already downloaded parts of the video clip can be en-
tobeappliedinordertominimizeresourcesandcostswithout hanced at a later time. This reduces the risk of stalling
degradingQoE.Additionally,thenetworkprovidercaresabout but requires increased signaling traffic as several HTTP
newbusinessmodelsandSLAsforhighqualityservices(e.g., requestsareneededpersegment.
QoEtariffs)toattractnewcustomers. (cid:129) AH.264/SVCfileofavideoofacertainbitrateislarger
LessonsLearned: compared to an H.264/AVC file of the same video (in
(cid:129) Problems stemming from the network can be identified, same quality). AVC performs better under high latencies,
but there are many different options for influencing the while SVC adapts more easily to sudden and temporary
datatransportinthenetwork. bandwidthfluctuationswhenusingasmallreceiverbuffer.
(cid:129) Othergoalmetrics(notonlyQoE)playanimportantrole (cid:129) Anadaptationinmultipledimensionsisperceivedasbetter
forthenetworkprovider(e.g.,inter-domaintraffic,SLAs). thanasingledimensionadaptation.
(cid:129) VideostreamingperformanceisgoodwhenTCPthrough- (cid:129) Whenpreparingthestreamingcontent,acontentanalysis
put is roughly twice the video bit rate, i.e., there is a could allow for improved video segmentation and selec-
significant system overhead as the expense for reliable tionofthebestadaptationdimension(s).
transmission. (cid:129) LargersegmentsizesleadtoimprovementsinQoE,higher
(cid:129) EgoisticclientbehaviorcanharmnetworkwideHASQoE coding efficiency, and higher network utilization. How-
and is best countered by employing either a centralized ever,ithasanegativeimpactonstallingandfairness.
controlunitoracooperativeclient-proxybasedcontrolin (cid:129) Image quality is more important for QoE than resolution
order to establish fair QoE distribution across competing duetocompressionartifacts.
HASinstances (cid:129) HAS can take advantage of frame rate adaptation, espe-
Challenges and Future Work: The network provider needs cially for high motion content where small frame rate
traffic and QoE models in order to understand the relevant reductionsarelessvisible.
QoE influence factors and the technical factors which can be (cid:129) Establishing a fair bandwidth distribution among clients
influenced. QoE monitoring is required for network dimen- anddevicesmayincreasetheoverallQoEoftheclients.

488 IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015
(cid:129) Reducing quality too much in any dimension will lead to decreased TCP performance, which is caused by interactions
| badQoE. |     |     |     |     |     |     |     | betweentwofeedbackloops:HASrate-adaptationlogicatthe |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
Challenges and Future Work: When preparing the content, application layer and TCP congestion control at the transport
thevideoserviceproviderhastoselectappropriateparameters layer. In addition, we reviewed a number of measures that
countersubsetsoftheseinteractions,rangingfromserverbased
| for segment | length | and representation |     |     | bit rates. | Moreover, | the |     |     |     |     |     |     |
| ----------- | ------ | ------------------ | --- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
optimal encodings and adaptation dimensions have to be cho- approaches over network based approaches and collaborative
sen. The offered representation levels and dimensions should solutionsthatutilizeclient-proxycommunication.
be aligned to the adaptation algorithm on the end user side. We discussed numerous related works on the Quality of
A content analysis could be incorporated, such that possible Experience of HAS in order to foster future research and
|     |     |     |     |     |     |     |     | development | of  | new mechanisms. |     | We showed | that current |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------------- | --- | --------- | ------------ |
qualityswitchescanbehiddentothegreatestextent.
Moreover,technicalinfrastructureisrequiredtosupportthe HAS solutions only decide on adaptation based on bandwidth
customers.Thismeans,apowerfulcontentdeliverynetworkis measurements and buffer levels. Hence, the resulting QoE,
neededandpropermechanismsforoptimalresourceutilization which is affected by adaptation, is not optimal. As a holistic
and load balancing are required, which should be properly model would be beneficial for all involved stakeholders, QoE
researchersshouldaimatmultidimensionalQoEmodels,taking
| aligned | with video | codecs | and | video | delivery | protocols. | The |     |     |     |     |     |     |
| ------- | ---------- | ------ | --- | ----- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
distributionofthevideocontenthastoplacethecontentclose into account all facets of QoE and a systematic approach to
to the end user in order to minimize transmission delays and measureHASQoE.Asthecontextofserviceconsumptionhas
increase the throughput. Therefore, smart content placement a big influence on the perceived quality, a concept for context
and caching strategies can be developed and integrated which monitoring has to be developed and implemented. Moreover,
utilize social information about the end users (e.g., TailGate collaborative solutions which include information from other
[166], [167]). Additionally, fairness among customers should stakeholders or direct feedback from end users have to be
betakenintoaccount,suchthatallusersobtainthesameservice investigated on the technical side. The information obtained
fromotherstakeholderscanbebeneficialinsituationsinwhich
quality.
onlylimitedinformationaboutsystem,content,user,orcontext
isavailableandcorrespondingparametersareestimated.Thus,
|     |     | IX. | CONCLUSION |     |     |     |     |            |           |        |     |             |                |
| --- | --- | --- | ---------- | --- | --- | --- | --- | ---------- | --------- | ------ | --- | ----------- | -------------- |
|     |     |     |            |     |     |     |     | future HAS | solutions | should | be  | QoE-driven, | context aware, |
In this work, the evolving research field of HAS was sur- and collaborative, such that especially end users but also all
veyed. To sum up, quality adaptation in video streaming and other involved stakeholders benefit from improved adaptation
its influence on QoE is not well understood so far. It has decisionsandimprovedqualityofvideostreamingservices.
| been shown | by related | work | that | HAS | clearly | outperforms |     |     |     |     |     |     |     |
| ---------- | ---------- | ---- | ---- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
classical streaming as it significantly reduces stalling which ACKNOWLEDGMENT
| is considered | to be | the worst | quality | degradation. |     | As  | current |             |     |            |          |               |           |
| ------------- | ----- | --------- | ------- | ------------ | --- | --- | ------- | ----------- | --- | ---------- | -------- | ------------- | --------- |
|               |       |           |         |              |     |     |         | The authors |     | would like | to thank | the anonymous | reviewers |
solutionsarenotQoE-drivensofarandonlyofferwhatcanbe
fortheirvaluableandconstructivecommentsandsuggestions,
| called a | “best effort | QoE”, | this | work outlined |     | the influence | of  |     |     |     |     |     |     |
| -------- | ------------ | ----- | ---- | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
aswellasStanislavLangeforproofreading.Theauthorsalone
adaptationonQoE.
areresponsibleforthecontent.
| From     | investigating  | adaptation |     | strategy | parameters, |               | it could |     |     |     |     |     |     |
| -------- | -------------- | ---------- | --- | -------- | ----------- | ------------- | -------- | --- | --- | --- | --- | --- | --- |
| be found | that stalling, | initial    |     | delay,   | memory      | requirements, |          |     |     |     |     |     |     |
REFERENCES
| and bandwidth | utilization |     | heavily | depend | on  | buffer | size and |            |        |            |        |          |                  |
| ------------- | ----------- | --- | ------- | ------ | --- | ------ | -------- | ---------- | ------ | ---------- | ------ | -------- | ---------------- |
|               |             |     |         |        |     |        |          | [1] “Cisco | visual | networking | index: | Forecast | and methodology, |
segmentsize.However,asmallbufferofafewsegmentlengths
2012–2017,”SanJose,CA,USA,Tech.Rep.,2013.
wasshowntobesufficientformostbandwidthconditions.The [2] J.Roettgers,“Don’ttouchthatdial:HowYouTubeisbringingadaptive
|                 |     |           |                |     |            |     |           | streaming | to  | mobile, TVs,” | 2013. | [Online]. Available: | http://gigaom. |
| --------------- | --- | --------- | -------------- | --- | ---------- | --- | --------- | --------- | --- | ------------- | ----- | -------------------- | -------------- |
| most dominating |     | factor is | the adaptation |     | amplitude, |     | for which |           |     |               |       |                      |                |
com/2013/03/13/youtube-adaptive-streaming-mobile-tv
| a high amplitude |     | (i.e., a | detectable | quality | change) |     | results | in  |     |     |     |     |     |
| ---------------- | --- | -------- | ---------- | ------- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- |
[3] A.Sackl,P.Zwickl,andP.Reichl,“Thetroublewithchoice:Anempir-
lowacceptanceandperceivedquality.Moreover,theadaptation
icalstudytoinvestigatetheinfluenceofchargingstrategiesandcontent
selectiononQoE,”inProc.9thInt.CNSM,Zurich,Switzerland,2013,
| frequency | should | be rather | low, | as switching |     | is a degradation |     |     |     |     |     |     |     |
| --------- | ------ | --------- | ---- | ------------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
pp.298–303.
| itself. Apart | from | these parameters, |     | also | time | on each | quality |     |     |     |     |     |     |
| ------------- | ---- | ----------------- | --- | ---- | ---- | ------- | ------- | --- | --- | --- | --- | --- | --- |
[4] T.Hoßfeldetal.,“QuantificationofYouTubeQoEviacrowdsourcing,”
layerandbaselayerqualityinfluencetheQoEofusers.
|             |            |            |             |                   |          |       |            | in Proc.     | IEEE       | Int. Symp.    | Multimedia, | Dana          | Point, CA, USA, 2011, |
| ----------- | ---------- | ---------- | ----------- | ----------------- | -------- | ----- | ---------- | ------------ | ---------- | ------------- | ----------- | ------------- | --------------------- |
| For each    | adaptation | dimension, |             | main              | findings |       | and QoE    | pp.494–499.  |            |               |             |               |                       |
|             |            |            |             |                   |          |       |            | [5] O. Oyman |            | and S. Singh, | “Quality    | of experience | for HTTP adaptive     |
| functions   | have been  | presented. |             | Multi-dimensional |          |       | adaptation |              |            |               |             |               |                       |
|             |            |            |             |                   |          |       |            | streaming    | services,” | IEEE          | Commun.     | Mag., vol.    | 50, no. 4, pp. 20–27, |
| outperforms | single     | dimension  | adaptation, |                   | and      | thus, | should be  | Apr.2012.    |            |               |             |               |                       |
consideredinfutureHASmechanismsandcontentpreparation. [6] Y. Wang, “Survey of objective video quality measurements,” EMC
Theorder ofimportance ofthedifferentadaptation dimension Corp.,Hopkinton,MA,USA,Tech.Rep.WPI-CS-TR-06-02,2006.
[7] U.EngelkeandH.-J.Zepernick,“Perceptual-basedqualitymetricsfor
is image quality before frame rate and finally resolution, i.e., imageandvideoservices:Asurvey,”inProc.3rdEuroNGIConf.Netw.,
a decrease of image quality is perceived worst. Although this Trondheim,Norway,2007,pp.190–197.
[8] W.LinandC.-C.J.Kuo,“Perceptualvisualqualitymetrics:Asurvey,”
order seems to be valid for most video contents, there exist J. Vis. Commun. Image Represent., vol. 22, no. 4, pp. 297–312,
| somevideotypesforwhichtheordercanbedifferent. |     |     |     |     |     |     |     | May2011. |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
Beyond the impact of adaptation on pure video QoE, we [9] S. Chikkerur, V. Sundaram, M. Reisslein, and L. Karam, “Objective
videoqualityassessmentmethods:Aclassification,review,performance
| also showed | that              | QoE of | other   | applications |       | can be      | impaired |              |     |             |             |          |                     |
| ----------- | ----------------- | ------ | ------- | ------------ | ----- | ----------- | -------- | ------------ | --- | ----------- | ----------- | -------- | ------------------- |
|             |                   |        |         |              |       |             |          | comparison,” |     | IEEE Trans. | Broadcast., | vol. 57, | no. 2, pp. 165–182, |
| due to      | network stability |        | issues, | high         | round | trip times, | and      | Jun.2011.    |     |             |             |          |                     |

| SEUFERTetal.:SURVEYONQUALITYOFEXPERIENCEOFHAS |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 489 |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[10] N. Zong,Surveyandgapanalysis forHTTP streaming standardsand [34] A. Zambelli, Smooth streaming technical overview, Microsoft Corp.,
implementations, Internet Engineering Task Force Network Working Redmond,WA,USA,Tech.Rep.[Online].Available:http://www.iis.net/
Group,Fremont,CA,USA,Tech.Rep.[Online].Available:http://tools. learn/media/on-demand-smooth-streaming/smooth-streaming-
technical-overview
ietf.org/html/draft-zong-httpstreaming-gap-analysis-01
[11] K.J.Ma,R.Barto,andS.Bhatia,“AsurveyofschemesforInternet- [35] AppleInc., HTTPLiveStreamingOverview2013.[Online].Available:
basedvideodelivery,”J.Netw.Comput.Appl.,vol.34,no.5,pp.1572– https://developer.apple.com/library/ios/documentation/networkingin-
1586,Sep.2011. ternet/conceptual/streamingmediaguide/Introduction/Introduction.html
[12] V. Adzic, H. Kalva, and B. Furht, “A survey of multimedia content [36] AdobeSystemsInc., HTTPDynamicStreaming2013.[Online].Avail-
able:http://www.adobe.com/products/hds-dynamic-streaming.html
adaptationformobiledevices,”MultimediaToolsAppl.,vol.51,no.1,
pp.379–396,Jan.2011. [37] Adobe Systems Inc., HTTP Dynamic Streaming on the Adobe
[13] H. Luo and M.-L. Shyu, “Quality of service provision in mobile Flash Platform 2010. [Online]. Available: https://bugbase.adobe.
multimedia—Asurvey,”Human-CentricComput.Inf.Sci.,vol.1,no.5, com/index.cfm?event=file.view&id=2943064&seqNum=6&name=
httpdynamicstreaming_wp_ue.pdf
pp.1–15,Nov.2011.
[14] K.D.Singh,Y.Hadjadj-Aoul,andG.Rubino,“Qualityofexperience [38] EuropeanTelecommunicationsStandardInstitute(ETSI).(2009).Uni-
estimationforadaptiveHTTP/TCPvideostreamingusingH.264/AVC,” versalMobileTelecommunicationSystem(UMTS);LTE;Transparent
inProc.IEEECCNC,LasVegas,NV,USA,2012,pp.127–131. end-to-end Packet-Switched Streaming Service (PSS); Protocols and
Codecs,Sophia-AntipolisCedex,France,3GPPTS26.234Version9.1.0
[15] “Qualinetwhitepaperondefinitionsofqualityofexperience(2012),”
Release9.
EuropeanNetworkonQualityofExperienceinMultimediaSystemsand
Services(COSTActionIC1003),Lausanne,Switzerland,2012. [39] EuropeanTelecommunicationsStandardInstitute(ETSI).(2010).Uni-
[16] R.K.P.Mok,E.W.W.Chan,X.Luo,andR.K.C.Chan,“Inferringthe versal Mobile Telecommunication System (UMTS); LTE; Transpar-
QoEofHTTPvideostreamingfromuser-viewingactivities,”inProc. entend-to-endPacket-SwitchedStreamingService(PSS);Progressive
|     |     |     |     |     |     |     |     | download | and | dynamic | adaptive | streaming | over HTTP | (3GP-DASH), |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- | -------- | --------- | --------- | ----------- | --- |
ACMSIGCOMMW-MUST,Toronto,ON,Canada,2011,pp.31–36.
|     |     |     |     |     |     |     |     | Sophia-Antipolis |     | Cedex, | France, | 3GPP | TS 26.247 | Version | 1.0.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ------- | ---- | --------- | ------- | ----- |
[17] T.Hoßfeldetal.,“Initialdelayvs.interruptions:Betweenthedeviland
| thedeepbluesea,”inProc.4thInt.WorkshopQoMEX,YarraValley, |     |     |     |     |     |     |     | Release10. |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Vic.,Australia,2012,pp.1–6. [40] Information Technology—Dynamic Adaptive Streaming Over HTTP
(DASH)—Part1:MediaPresentationDescriptionandSegmentFormats,
| [18] S. Egger, | P.  | Reichl, | T. Hoßfeld, | and | R. Schatz, | “Time | is band- |     |     |     |     |     |     |     |     |
| -------------- | --- | ------- | ----------- | --- | ---------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ISO/IEC23009-1:2012,2012.
width?Narrowingthegapbetweensubjectivetimeperceptionandqual-
|               |              |     |            |      |         |             |       | [41] DASHIndustryForum,     |     | ForPromotionofMPEG-DASH2013.[Online]. |     |     |     |     |     |
| ------------- | ------------ | --- | ---------- | ---- | ------- | ----------- | ----- | --------------------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
| ity of        | experience,” | in  | Proc. IEEE | ICC, | Ottawa, | ON, Canada, | 2012, |                             |     |                                       |     |     |     |     |     |
| pp.1325–1330. |              |     |            |      |         |             |       | Available:http://dashif.org |     |                                       |     |     |     |     |     |
GuidelinesforImplementation:DASH-AVC/264InteroperabilityPoints,
| [19] R.E.Kooij,A.Kamal,andK.Brunnström,“Perceivedqualityofchannel |     |     |     |     |     |     |     | [42] |          |        |                 |            |     |                      |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ------ | --------------- | ---------- | --- | -------------------- | --- |
|                                                                   |     |     |     |     |     |     |     | DASH | Industry | Forum, | 2013. [Online]. | Available: |     | http://dashif.org/w/ |     |
zapping,”inProc.CSN,PalmadeMallorca,Spain,2006,pp.155–158.
2013/06/DASH-AVC-264-base-v1.03.pdf
| [20] S. Egger, | T.  | Hoßfeld, | R. Schatz, | and M. | Fiedler, | “Waiting | times in |                 |           |     |         |        |                 |     |            |
| -------------- | --- | -------- | ---------- | ------ | -------- | -------- | -------- | --------------- | --------- | --- | ------- | ------ | --------------- | --- | ---------- |
|                |     |          |            |        |          |          |          | [43] Wikipedia, | 615782083 |     | List of | Codecs | 2014. [Online]. |     | Available: |
qualityofexperienceforwebbasedservices,”inProc.4thInt.Workshop
QoMEX,YarraValley,Vic.,Australia,2012,pp.86–96. http://en.wikipedia.org/w/index.php?title=List_of_codecs&amp;
oldid=615782083,615782083
[21] A.Sackl,S.Egger,andR.Schatz,“Where’sthemusic?Comparingthe
|     |     |     |     |     |     |     |     | [44] Extensible | Markup | Language | (XML) | 1.0 (Fifth | Edition), | World | Wide |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | -------- | ----- | ---------- | --------- | ----- | ---- |
QoEimpactoftemporalimpairmentsbetweenmusicandvideostream-
WebConsortium(W3C),Cambridge,MA,USA,2013.
| ing,”     | in Proc. | 5th Int. | Workshop | QoMEX, | Klagenfurt, | Austria, | 2013, |                                                                   |     |     |     |     |     |     |     |
| --------- | -------- | -------- | -------- | ------ | ----------- | -------- | ----- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|           |          |          |          |        |             |          |       | [45] FlashMediaManifest(F4M)FormatSpecification,AdobeSystemsInc., |     |     |     |     |     |     |     |
| pp.64–69. |          |          |          |        |             |          |       | SanJose,CA,USA,2013.                                              |     |     |     |     |     |     |     |
[22] A.RaakeandS.Egger,“Qualityandqualityofexperience,”inQuality
|     |     |     |     |     |     |     |     | [46] M. Levkov, | “Video | Encoding | and | Transcoding |     | Recommendations |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | -------- | --- | ----------- | --- | --------------- | --- |
ofExperience:AdvancedConcepts,ApplicationsandMethods,S.Möller
|                 |     |                                      |     |     |     |     |     | for HTTP | Dynamic | Streaming | in  | the Adobe | Flash | Platform,” | 2010. |
| --------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | -------- | ------- | --------- | --- | --------- | ----- | ---------- | ----- |
| andA.Raake,Eds. |     | NewYork,NY,USA:Springer-Verlag,2014. |     |     |     |     |     |          |         |           |     |           |       |            |       |
[Online].Available:http://download.macromedia.com/flashmediaserver/
[23] T.DePessemier,K.DeMoor,W.Joseph,L.DeMarez,andL.Martens,
“Quantifying the influence of rebuffering interruptions on the user’s http_encoding_recommendations.pdf
|         |               |     |        |              |            |      |        | [47] HbbTVSpecification,HbbTVAssociation,Erlangen,Germany,2012. |     |     |     |     |     |     |     |
| ------- | ------------- | --- | ------ | ------------ | ---------- | ---- | ------ | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| quality | of experience |     | during | mobile video | watching,” | IEEE | Trans. |                                                                 |     |     |     |     |     |     |     |
|         |               |     |        |              |            |      |        | [48] InformationTechnology—HighEfficiencyCodingandMediaDelivery |     |     |     |     |     |     |     |
Broadcast.,vol.59,no.1,pp.47–61,Mar.2013.
inHeterogeneousEnvironments—Part2:HighEfficiencyVideoCoding,
| [24] A. Finamore, |     | M. Mellia, | M. M. | Munafò, | R. Torres, | and | S. G. Rao, |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | ----- | ------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
ISO/IEC23008-2:2013,2013.
“YouTubeeverywhere:Impactofdeviceandinfrastructuresynergieson [49] Information Technology—Generic Coding of Moving Pictures and
userexperience,”inProc.InternetMeas.Conf.,Berlin,Germany,2011,
|     |     |     |     |     |     |     |     | Associated | Audio | Information: |     | Systems, | ISO/IEC | 13818-1:2000, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ------------ | --- | -------- | ------- | ------------- | --- |
pp.345–360.
2000.
| [25] L. Chen, | Y.  | Zhou, and | D. M. | Chiu, “Video | browsing—A |     | study of |                                                                   |     |     |     |     |     |     |     |
| ------------- | --- | --------- | ----- | ------------ | ---------- | --- | -------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|               |     |           |       |              |            |     |          | [50] InformationTechnology—CodingofAudio-visualObjects—Part12:ISO |     |     |     |     |     |     |     |
userbehaviorinonlineVoDservices,”inProc.22ndICCCN,Nassau, BaseMediaFileFormat,ISO/IEC14496-12:2005,2005.
Bahamas,2013,pp.1–7. [51] T. Siglin, Unifying global video strategies: MP4 file fragmentation
[26] Y.QiandM.Dai,“Theeffectofframefreezingandframeskippingon
|     |     |     |     |     |     |     |     | for broadcast, |     | mobile and | web delivery, |     | Transitions, | Inc., | Bellevue, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | ------------- | --- | ------------ | ----- | --------- |
videoquality,”inProc.2ndInt.Conf.IIH-MSP,Pasadena,CA,USA,
|     |     |     |     |     |     |     |     | KY, USA. | [Online]. | Available: | http://184.168.176.117/reports-public/ |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | -------------------------------------- | --- | --- | --- | --- |
2006,pp.423–426.
Adobe/20111116-fMP4-Adobe-Microsoft.pdf
[27] T. N. Minhas and M. Fiedler, “Impact of disturbance locations on [52] F4V/FLVtechnologycenter,AdobeSystemsInc.,SanJose,CA,USA,
| videoqualityofexperience,”inProc.2ndWorkshopQoEMCS,Lisbon, |     |     |     |     |     |     |     | 2013. |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Portugal,2011,pp.1–5.
|     |     |     |     |     |     |     |     | [53] I.Kofler,R.Kuschnig,andH.Hellwagner,“ImplicationsoftheISObase |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
[28] Q.Huynh-ThuandM.Ghanbari,“Temporalaspectofperceivedquality
mediafileformatonadaptiveHTTPstreamingofH.264/SVC,”inProc.
inmobilevideobroadcasting,”IEEETrans.Broadcast.,vol.54,no.3, IEEECCNC,LasVegas,NV,USA,2012,pp.549–553.
pp.641–651,Sep.2008. [54] K. Ramkishor, T. S. Raghu, K. Siuman, and P. S. S. B. K. Gupta,
[29] J.Yao,S.S.Kanhere,I.Hossain,andM.Hassan,“Empiricalevaluation “Adaptation of video encoders for improvement in quality,” in Proc.
ofHTTPadaptivestreamingundervehicularmobility,”inProc.10thInt.
IEEEISCAS,Bangkok,Thailand,2003,pp.II-692–II-695.
IFIPTC6Netw.Conf.,Valencia,Spain,2011,pp.92–105. [55] T. Lohmar, T. Einarsson, P. Frojdh, F. Gabin, and M. Kampmann,
[30] T.Zinner,T.Hoßfeld,T.N.Minash,andM.Fiedler,“Controlledvs.un- “Dynamic adaptive HTTP streaming of live content,” in Proc. IEEE
controlleddegradationsofQoE—Theprovisioning–deliveryhysteresis Int.Symp.WoWMoMNetw.,Lucca,Italy,2011,pp.1–8.
incaseofvideo,”inProc.1stWorkshopQoEMCS,Tampere,Finland, [56] V.Adzic,H.Kalva,andB.Furht,“Optimizingvideoencodingforadap-
2010,pp.1–3.
|     |     |     |     |     |     |     |     | tive streaming |     | over HTTP,” | IEEE | Trans. | Consum. | Electron., | vol. 58, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | ---- | ------ | ------- | ---------- | -------- |
[31] MoveNetworks, MoveNetworks2010.[Online].Available:http://www. no.2,pp.397–403,May2012.
movenetworkshd.com [57] J. Lievens, S. Satti, N. Deligiannis, P. Schelkens, and A. Munteanu,
[32] A.Zambelli,“Ahistoryofmediastreamingandthefutureofconnected “Optimized segmentation of H.264/AVC video for HTTP adaptive
TV,”TheGuardian,2013.[Online].Available:http://www.theguardian.
streaming,”inProc.IFIP/IEEEInt.Symp.IM,Ghent,Belgium,2013,
| com/media-network/media-network-blog/2013/mar/01/history- |     |     |     |     |     |     |     | pp.1312–1317. |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
streaming-future-connected-tv [58] J.Ohm,G.Sullivan,H.Schwarz,T.K.Tan,andT.Wiegand,“Compari-
[33] D. F. Brueck and M. B. Hurst, “Apparatus, system, method for sonofthecodingefficiencyofvideocodingstandards—IncludingHigh
multi-bitrate content streaming,” U.S. Patent 7818444 B2, Oct. 19, Efficiency Video Coding (HEVC),” IEEE Trans. Circuits Syst. Video
| 2010. |     |     |     |     |     |     |     | Technol.,vol.22,no.12,pp.1669–1684,Dec.2012. |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |

490 IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015
[59] InformationTechnology—CodingofAudio-VisualObjects—Part10:Ad- [84] S.Oechsner,T.Zinner,J.Prokopetz,andT.Hoßfeld,“Supportingscal-
vancedVideoCoding,ISO/IEC14496-10:2012,2013. ablevideocodecsinaP2Pvideo-on-demandstreamingsystem,”inProc.
[60] M. Karczewicz and R. Kurceren, “The SP- and SI-frames design for 21stITCSSMultimediaAppl.—Traffic,Perform.QoE,Miyazaki,Japan,
H.264/AVC,”IEEETrans.CircuitsSyst.VideoTechnol.,vol.13,no.7, 2010,pp.48–53.
pp.637–644,Jul.2003. [85] C.Sieber,T.Hoßfeld,T.Zinner,P.Tran-Gia,andC.Timmerer,“Imple-
[61] Information Technology—Generic Coding of Moving Pictures and mentationanduser-centriccomparisonofanoveladaptationlogicfor
Associated Audio Information: Video, ISO/IEC 13818-2:1996, DASHwithSVC,”inProc.IFIP/IEEEInt.WorkshopQCMan,Ghent,
1996. Belgium,2013,pp.1318–1323.
[62] H. Schwarz, D. Marpe, and T. Wiegand, “Overview of the scal- [86] B. Wang, J. Kurose, P. Shenoy, and D. Towsley, “Multimedia
able video coding extension of the H.264/AVC standard,” IEEE streaming via TCP: An analytic performance study,” ACM Trans.
Trans. Circuits Syst. Video Technol., vol. 17, no. 9, pp. 1103–1120, Multimedia Comput., Commun. Appl., vol. 4, no. 2, pp. 16:1–16:22,
Sep.2007. May2008.
[63] M.Wien,H.Schwarz,andT.Oelbaum,“PerformanceanalysisofSVC,” [87] H.F.Nielsenetal.,“NetworkperformanceeffectsofHTTP/1.1,CSS1,
IEEETrans.CircuitsSyst.VideoTechnol.,vol.17,no.9,pp.1194–1203, PNG,”ACMSIGCOMMComput.Commun.Rev.,vol.27,no.4,pp.155–
Sep.2007. 166,Oct.1997.
[64] R.Gupta,A.Pulipaka,P.Seeling,L.Karam,andM.Reisslein,“H.264 [88] S.Akhshabi,A.C.Begen,andC.Dovrolis,“Anexperimentalevalua-
CoarseGrainScalable(CGS)andMediumGrainScalable(MGS)en- tionofrate-adaptationalgorithmsinadaptivestreamingoverHTTP,”in
codedvideo:Atracebasedtrafficandqualityevaluation,”IEEETrans. Proc. 2nd Annu. ACM Conf. MMSys, Santa Clara, CA, USA, 2011,
Broadcast.,vol.58,no.3,pp.428–439,Sep.2012. pp.157–168.
[65] M. Grafl et al., “Scalable video coding guidelines and performance [89] K. Miller, N. Corda, S. Argyropoulos, A. Raake, and A. Wolisz,
evaluationsforadaptivemediadeliveryofhighdefinitioncontent,”in “Optimal adaptation trajectories for block-request adaptive video
Proc.IEEEISCC,Split,Croatia,2013,pp.000855–000861. streaming,”inProc.20thInt.PVWorkshop,SanJose,CA,USA,2013,
[66] M. Grafl, C. Timmerer, H. Hellwagner, W. Cherif, and A. Ksentini, pp.1–8.
“EvaluationofhybridscalablevideocodingforHTTP-basedadaptive [90] T. Hoßfeld, M. Seufert, C. Sieber, T. Zinner, and P. Tran-Gia, “Close
mediastreamingwithhigh-definitioncontent,”inProc.14thInt.Symp. to optimum? User-centric evaluation of adaptation logics for HTTP
WorkshopsWoWMoMNetw.,Madrid,Spain,2013,pp.1–7. adaptive streaming,” PIK—Praxis der Informationverarbeitung und-
[67] J. Famaey et al., “On the merits of SVC-based HTTP adaptive Kommunikation(PIK)2014.
streaming,”inProc.IFIP/IEEEInt.Symp.IM,Ghent,Belgium,2013, [91] P.Pahalawatta,R.Berry,T.Pappas,andA.Katsaggelos,“Content-aware
pp.419–426. resourceallocationandpacketschedulingforvideotransmissionover
[68] J.-S.Leeetal.,“Subjectiveevaluationofscalablevideocodingforcon- wirelessnetworks,”IEEEJ.Sel.AreasCommun.,vol.25,no.4,pp.749–
tentdistribution,”inProc.18thACMInt.Conf.Multimedia,Florence, 759,May2007.
Italy,2010,pp.65–72. [92] F.Dobrianetal.,“Understandingtheimpactofvideoqualityonuser
[69] T.Oelbaum,H.Schwarz,M.Wien,andT.Wiegand,“Subjectiveperfor- engagement,”inProc.ACMSIGCOMM,Toronto,ON,Canada,2011,
manceevaluationoftheSVCextensionofH.264/AVC,”inProc.15th pp.362–373.
IEEEICIP,SanDiego,CA,USA,2008,pp.2772–2775. [93] A. Balachandran et al., “A quest for an Internet video quality-of-
[70] C.Müller,D.Renzi,S.Lederer,S.Battista,andC.Timmerer,“Using experiencemetric,”inProc.11thACMWorkshopHotNets-XI,Redmond,
scalable video coding for dynamic adaptive streaming over HTTP in WA,USA,2012,pp.97–102.
mobile environments,” in Proc. 20th EUSIPCO, Bucharest, Romania, [94] N.Cranley,P.Perry,andL.Murphy,“Userperceptionofadaptingvideo
2012,pp.2208–2212. quality,” Int. J. Human-Comput. Stud., vol. 64, no. 8, pp. 637–647,
[71] R. Huysegems, B. De Vleeschauwer, T. Wu, and W. Van Leekwijck, Aug.2006.
“SVC-based HTTP adaptive streaming,” Bell Labs Tech. J., vol. 16, [95] O.Abboud,T.Zinner,K.Pussep,S.Al-Sabea,andR.Steinmetz,“On
no.4,pp.25–41,Mar.2012. the impact of quality adaptation in SVC-based P2P video-on-demand
[72] Y.Sanchezetal.,“EfficientHTTP-basedstreamingusingscalablevideo systems,”inProc.2ndAnnu.ACMConf.MMSys,SantaClara,CA,USA,
coding,”SignalProcess.,ImageCommun.,vol.27,no.4,pp.329–342, 2011,pp.223–232.
Apr.2012. [96] R.Kuschnig,I.Kofler,andH.Hellwagner,“AnevaluationofTCP-based
[73] Z.Lietal.,“Networkfriendlyvideodistribution,”inProc.3rdInt.Conf. rate-controlalgorithmsforadaptiveInternetstreamingofH.264/SVC,”
NOF,Gammarth,Tunisia,2012,pp.1–8. in Proc. 1st Annu. ACM Conf. MMSys, Phoenix, AZ, USA, 2010,
[74] T.Kim,N.Avadhanam,andS.Subramanian,“Dimensioningreceiver pp.157–168.
bufferrequirementforunidirectionalVBRvideostreamingoverTCP,” [97] P.Ni,R.Eg,A.Eichhorn,C.Griwodz,andP.Halvorsen,“Flickereffects
inProc.IEEEICIP,Atlanta,GA,USA,2006,pp.3061–3064. inadaptivevideostreamingtohandhelddevices,”inProc.19thACMInt.
[75] T. Arsan, “Review of bandwidth estimation tools and application to Conf.MM,Scottsdale,AZ,USA,2011,pp.463–472.
bandwidthadaptivevideostreaming,”inProc.9thInt.Conf.HONET, [98] B.Lewcio,B.Belmudez,A.Mehmood,M.Wältermann,andS.Möller,
Istanbul,Turkey,2012,pp.152–156. “Videoqualityinnextgenerationmobilenetworks-perceptionoftime-
[76] Z.Yuan,H.Venkataraman,andG.-M.Muntean,“iBE:Anovelband- varyingtransmission,”inProc.IEEEInt.WorkshopTech.CQR,Naples,
widthestimationalgorithmformultimediaservicesoverIEEE802.11 FL,USA,2011,pp.1–6.
wirelessnetworks,”inProc.12thIFIP/IEEEInt.Conf.MMNS,Venice, [99] A.K.Moorthy,L.K.Choi,A.C.Bovik,andG.DeVeciana,“Videoqual-
Italy,2009,pp.69–80. ityassessmentonmobiledevices:Subjective,behavioralandobjective
[77] Z.Yuan,H.Venkataraman,andG.-M.Muntean,“MBE:Model-based studies,”IEEEJ.Sel.TopicsSignalProcess.,vol.6,no.6,pp.652–671,
available bandwidth estimation for IEEE 802.11 data communica- Oct.2012.
tions,” IEEE Trans. Veh. Technol., vol. 61, no. 5, pp. 2158–2171, [100] T.Hoßfeld,M.Seufert,C.Sieber,andT.Zinner,“Assessingeffectsizes
Jun.2012. ofinfluencefactorstowardsaQoEmodelforHTTPadaptivestreaming,”
[78] T.Kupka,P.Halvorsen,andC.Griwodz,“Anevaluationofliveadaptive inProc.6thInt.WorkshopQoMEX,Singapore,2014.
HTTPsegmentstreamingrequeststrategies,”inProc.IEEE36thConf. [101] M.GraflandC.Timmerer,“Representationswitchsmoothingforadap-
LCN,Bonn,Germany,2011,pp.604–612. tiveHTTPstreaming,”inProc.4thInt.WorkshopPQS,Vienna,Austria,
[79] C. C. Wüst and W. F. J. Verhaegh, “Quality control for scalable 2013,pp.178–183.
media processing applications,” J. Sched., vol. 7, no. 2, pp. 105–117, [102] M.Zink,J.Schmitt,andR.Steinmetz,“Layer-encodedvideoinscalable
Mar.2004. adaptivestreaming,”IEEETrans.Multimedia,vol.7,no.1,pp.75–84,
[80] D.JarnikovandT.Ozcelebi,“Clientintelligenceforadaptivestreaming Feb.2005.
solutions,”inProc.IEEEICME,Singapore,2010,pp.1499–1504. [103] Y.Pitrey,U.Engelke,M.Barkowsky,R.Pépion,andP.LeCallet,“Sub-
[81] C.Liu,I.Bouazizi,andM.Gabbouj,“RateadaptationforadaptiveHTTP jectivequalityofSVC-codedvideoswithdifferenterror-patternscon-
streaming,”inProc.2ndAnnu.ACMConf.MMSys,SantaClara,CA, cealedusingspatialscalability,”inProc.3rdEUVIPWorkshop,Paris,
USA,2011,pp.169–174. France,2011,pp.180–185.
[82] K.Miller,E.Quacchio,G.Gennari,andA.Wolisz,“Adaptationalgo- [104] C. Alberti et al., “Automated QoE evaluation of dynamic adaptive
rithmforadaptivestreamingoverHTTP,”inProc.19thInt.PVWork- streamingoverHTTP,”inProc.5thInt.WorkshopQoMEX,Klagenfurt,
shop,Munich,Germany,2012,pp.173–178. Austria,2013,pp.58–63.
[83] C. Müller, S. Lederer, and C. Timmerer, “An evaluation of dynamic [105] N.Boutenetal.,“QoEoptimizationthroughin-networkqualityadapta-
adaptivestreamingoverHTTPinvehicularenvironments,”inProc.4th tionforHTTPadaptivestreaming,”inProc.8thInt.CNSM,LasVegas,
WorkshopMoVID,ChapelHill,NC,USA,2012,pp.37–42. NV,USA,2012,pp.336–342.

SEUFERTetal.:SURVEYONQUALITYOFEXPERIENCEOFHAS 491
[106] Sintel, The Durian Open Movie Project, Blender Foundation, [130] H.Knoche,J.D.McCarthy,andM.A.Sasse,“Cansmallbebeautiful?:
Amsterdam,TheNetherlands,2010. AssessingimageresolutionrequirementsformobileTV,”inProc.13th
[107] Y.-F.Ou,Y.Zhou,andY.Wang,“Perceptualqualityofvideowithframe Annu.ACMInt.Conf.Multimedia,Singapore,2005,pp.829–838.
ratevariation:Asubjectivestudy,”inProc.IEEEICASSP,Dallas,TX, [131] R. T. Apteker, J. A. Fisher, V. S. Kisimov, and H. Neishlos, “Video
USA,2010,pp.2446–2449. acceptabilityandframerate,”IEEEMultiMedia,vol.2,no.3,pp.32–
[108] F. Pereira, “Sensations, perceptions and emotions towards quality of 40,1995.
experience evaluation for consumer electronics video adaptations,” in [132] D.Wang,F.Speranza,A.Vincent,T.Martin,andP.Blanchfield,“Toward
Proc. 1st Int. Workshop VPQM Consum. Electron., Scottsdale, AZ, optimalratecontrol:Astudyoftheimpactofspatialresolution,frame
USA,2005.[Online].Available:http://enpub.fulton.asu.edu/resp/vpqm/ rate,quantizationonsubjectivevideoqualityandbitrate,”inProc.SPIE
vpqm2005/vpqm05_cover.htm VCIP,Lugano,Switzerland,2003,pp.198–209.
[109] M. K. Asadi and J.-C. Duford, “Multimedia adaptation by trans- [133] T. Hayashi et al., “Effects of IP packet loss and picture frame reduc-
modinginMPEG-21,”inProc.Int.WIAMIS,Lisbon,Portugal,2004, tiononMPEG1subjectivequality,”inProc.WorkshopSignalProcess.,
p.83. Copenhagen,Denmark,1999,pp.515–520.
[110] M.-N. Garcia and A. Raake, “Parametric packet-layer video quality [134] J.ChenandJ.Thropp,“Reviewoflowframerateeffectsonhumanper-
model for IPTV,” in Proc. 10th Int. Conf. ISSPA, Kuala Lumpur, formance,”IEEETrans.Syst.,Man,Cybern.A,Syst.,Humans,vol.37,
Malaysia,2010,pp.349–352. no.6,pp.1063–1076,Nov.2007.
[111] M. Seufert, M. Slanina, S. Egger, and M. Kottkamp, “To pool or not [135] M.Masry,S.S.Hemami,W.M.Osberger,andA.M.Rohaly,“Subjective
to pool: A comparison of temporal pooling methods for HTTP adap- qualityevaluationoflow-bit-ratevideo,”inProc.SPIEPhoton.West,
tivevideostreaming,”inProc.5thInt.WorkshopQoMEX,Klagenfurt, Electron.Imag.,SanJose,CA,USA,2001,pp.102–113.
Austria,2013,pp.52–57. [136] J.D.McCarthy,M.A.Sasse,andD.Miras,“Sharporsmooth?:Com-
[112] G.Zhaietal.,“Cross-dimensionalperceptualqualityassessmentforlow paringtheeffectsofquantizationvs.framerateforstreamedvideo,”in
bit-ratevideos,”IEEETrans.Multimedia,vol.10,no.7,pp.1316–1324, Proc.CHIComput.Syst.,Vienna,Austria,2004,pp.535–542.
Nov.2008. [137] N.VandenEnde,H.DeHesselle,andL.Meesters,“Towardscontent-
[113] K.YamagishiandT.Hayashi,“Parametricpacket-layermodelformon- awarecoding:Userstudy,”inProc.5thEuroITVConf.,Amsterdam,The
itoring video quality of IPTV services,” in Proc. IEEE ICC, Beijing, Netherlands,2007,pp.185–194.
China,2008,pp.110–114. [138] Y.Wang,S.-F.Chang,andA.C.Loui,“Subjectivepreferenceofspatio-
[114] H.Knoche,J.D.Mccarthy,andM.A.Sasse,“Howlowcanyougo?The temporalrateinvideoadaptationusingmulti-dimensionalscalablecod-
effectoflowresolutionsonshottypesinmobileTV,”MultimediaTools ing,”inProc.IEEEICME,Taipei,Taiwan,2004,pp.1719–1722.
Appl.,vol.36,no.1/2,pp.145–166,Jan.2008. [139] J.Korhonen,U.Reiter,andJ.You,“Subjectivecomparisonoftemporal
[115] L. Janowski and P. Romaniak, “QoE as a function of frame rate and andqualityscalability,”inProc.3rdInt.WorkshopQoMEX,Mechelen,
resolutionchanges,”inProc.3rdInt.WorkshopFMN,Krakow,Poland, Belgium,2011,pp.161–166.
2010,pp.34–45. [140] R.HoudailleandS.Gouache,“ShapingHTTPadaptivestreamsfora
[116] P. Le Callet, S. Péchard, S. Tourancheau, A. Ninassi, and D. Barba, betteruserexperience,”inProc.3rdAnnu.ACMConf.MMSys,Chapel
“Towardsthenextgenerationofvideoandimagequalitymetrics:Im- Hill,NC,USA,2012,pp.1–9.
pact of display, resolution, contents and visual attention in subjective [141] S.Akhshabi,L.Anantakrishnan,A.C.Begen,andC.Dovrolis,“What
assessment,” in Proc. 2nd Int. Workshop IMQA, Chiba, Japan, 2007, happens when HTTP adaptive streaming players compete for band-
pp.1–9. width?” in Proc. 22nd ACM Int. Workshop NOSSDAV, Toronto, ON,
[117] R.R.Pastrana-Vidal,J.-C.Gicquel,C.Colomes,andH.Cherifi,“Frame Canada,2012,pp.9–14.
droppingeffectsonuserqualityperception,”inProc.5thInt.WIAMIS, [142] L.DeCiccoandS.Mascolo,“Anadaptivevideostreamingcontrolsys-
Lisbon,Portugal,2004. tem:Modeling,validation,performanceevaluation,”IEEE/ACMTrans.
[118] G.GhineaandJ.P.Thomas,“QoSimpactonuserperceptionandun- Netw.,vol.22,no.2,pp.526–539,Apr.2014.
derstanding of multimedia video clips,” in Proc. 6th ACM Int. Conf. [143] J.Estebanetal.,“InteractionsbetweenHTTPadaptivestreamingand
Multimedia,Bristol,U.K.,1998,pp.49–54. TCP,”inProc.22ndACMWorkshopNOSSDAV,Toronto,ON,Canada,
[119] R.K.Rajendran,M.VanDerSchaar,andS.-F.Chang,“FGS+:Opti- 2012,pp.21–26.
mizingthejointSNR–temporalvideoqualityinMPEG-4finegrained [144] T.-Y.Huang,N.Handigol,B.Heller,N.McKeown,andR.Johari,“Con-
scalable coding,” in Proc. IEEE ISCAS, Scottsdale, AZ, USA, 2002, fused,timid,unstable:Pickingavideostreamingrateishard,”inProc.
pp.I-445–I-448. ACMInternetMeas.Conf.,Boston,MA,USA,2012,pp.225–238.
[120] J.-S.Lee,F.DeSimone,andT.Ebrahimi,“Subjectivequalityevaluation [145] A. Mansy, B. Ver Steeg, and M. Ammar, “SABRE: A client based
via paired comparison: Application to scalable video coding,” IEEE technique for mitigating the buffer bloat effect of adaptive video
Trans.Multimedia,vol.13,no.5,pp.882–893,Oct.2011. flows,” in Proc. 4th Annu. ACM Conf. MMSys, Oslo, Norway, 2013,
[121] S. Jumisko-Pyykkö and J. Häkkinen, “Evaluation of subjective video pp.214–225.
qualityofmobiledevices,”inProc.13thAnnu.ACMInt.Conf.Multi- [146] J. Gettys, “Bufferbloat: Dark buffers in the Internet,” IEEE Internet
media,Singapore,2005,pp.535–538. Comput.,vol.15,no.3,pp.96–96,May/Jun.2011.
[122] S. Winkler and C. Faller, “Maximizing audiovisual quality at low bi- [147] P.Casas,M.Seufert,S.Egger,andR.Schatz,“Qualityofexperience
trates,”inProc.1stInt.WorkshopVPQMConsum.Electron.,Scottsdale, inremotevirtualdesktopservices,”inProc.IFIP/IEEEInt.Symp.IM,
AZ,USA,2005. Ghent,Belgium,2013,pp.1352–1357.
[123] Guidelines for Implementation: DASH-HEVC/265 Interoperabolity [148] T. Hoßfeld, R. Schatz, M. Varela, and C. Timmerer, “Challenges of
Points,DASHIndustryForum,2013.[Online].Avaialable:http://dashif. QoEmanagementforcloudapplications,”IEEECommun.Mag.,vol.50,
org/w/2013/10/DASH-HEVC-265-base-v0.92.pdf no.4,pp.28–36,Apr.2012.
[124] X. Wang et al., “DASH (HEVC)/LTE: QoE-based dynamic adaptive [149] S.Egger,R.Schatz,andS.Scherer,“Ittakestwototango—Assessing
streaming of HEVC content over wireless networks,” in Proc. IEEE theimpactofdelayonconversationalinteractivityonperceivedspeech
VCIP,SanDiego,CA,USA,2012.[Online].Available:http://ieeexplore. quality,”inProc.Interspeech,Makuhari,Japan,2010,pp.1321–1324.
ieee.org/xpl/articleDetails.jsp?arnumber=6410858 [150] A. Raake et al., “IP-based mobile and fixed network audiovisual me-
[125] J.LeFeuvre,J.Thiesse,M.Parmentier,M.Raulet,andC.Daguet,“Ultra dia services,” IEEE Signal Process. Mag., vol. 28, no. 6, pp. 68–79,
high definition HEVC dash data set,” in Proc. 5th Annu. ACM Conf. Nov.2011.
MMSys,Singapore,2014,pp.7–12. [151] X. Liu and A. Men, “QoE-aware traffic shaping for HTTP adaptive
[126] J.Bankoskietal.,“Towardsanextgenerationopen-sourcevideocodec,” streaming,”Int.J.MultimediaUbiquitousEng.,vol.9,no.2,pp.33–44,
in Proc. IST/SPIE Electron. Imag.—Vis. Inf. Process. Commun. IV, Mar.2014.
Burlingame,CA,USA,2013,pp.866606-1–866606-13. [152] S.Akhshabi,L.Anantakrishnan,C.Dovrolis,andA.C.Begen,“Server-
[127] D. Grois, D. Marpe, A. Mulayoff, B. Itzhaky, and O. Hadar, “Per- basedtrafficshapingforstabilizingoscillatingadaptivestreamingplay-
formancecomparisonofH.265/MPEG-HEVC,VP9H.264/MPEG-AVC ers,”inProc.23rdACMInt.WorkshopNOSSDAV,Oslo,Norway,2013,
encoders,”inProc.30thPCS,SanJose,CA,USA,2013,pp.394–397. pp.19–24.
[128] O.Verscheure,P.Frossard,andM.Hamdi,“User-orientedQoSanalysis [153] M.Ghobadi,Y.Cheng,A.Jain,andM.Mathis,“Trickle:Ratelimiting
inMPEG-2videodelivery,”Real-TimeImag.,vol.5,no.5,pp.305–314, YouTubevideostreaming,”inProc.USENIXConf.ATC,Boston,MA,
Oct.1999. USA,2012,pp.1–6.
[129] J.DeVriendt,D.DeVleeschauwer,andD.Robinson,“Modelfores- [154] S. Laga et al., “Optimizing scalable video delivery through openflow
timating QoE of video delivered using HTTP adaptive streaming,” in layer-based routing,” in Proc. IEEE NOMS, Krakow, Poland, 2014,
Proc.IFIP/IEEEInt.Symp.IM,Ghent,Belgium,2013,pp.1288–1293. pp.1–4.

492 IEEECOMMUNICATIONSURVEYS&TUTORIALS,VOL.17,NO.1,FIRSTQUARTER2015
[155] N.Boutenetal.,“Deadline-basedapproachforimprovingdeliveryof Martin Slanina received the M.Sc. and Ph.D. de-
SVC-basedHTTPadaptivestreamingcontent,”inProc.IEEENOMS, greesinelectronicsandcommunicationfromBrno
Krakow,Poland,2014,pp.1–7. UniversityofTechnology,Brno,CzechRepublic,in
[156] A.E.Essailietal.,“Quality-of-experiencedrivenadaptiveHTTPmedia
2005and2009,respectively.HeiscurrentlyanAs-
delivery,”inProc.IEEEICC,Budapest,Hungary,2013,pp.2480–2485. sistantProfessoratBrnoUniversityofTechnology.
[157] X.Zhu,Z.Li,R.Pan,J.Gahm,andH.Hu,“Fixingmulti-clientoscilla- Themainfocusareaofhisresearchisvideocoding,
tionsinHTTP-basedadaptivestreaming:Acontroltheoreticapproach,” display,andQualityofExperienceinvideoservices,
inProc.IEEE15thInt.WorkshopMMSP,Pula,Italy,2013,pp.230–235. mainly in the context of mobile communication
[158] S.Petrangeli,M.Claeys,S.Latre,J.Famaey,andF.DeTurck,“Amulti-
networks.
agentQ-learning-basedframeworkforachievingfairnessinHTTPadap-
tivestreaming,”inProc.IEEENOMS,Krakow,Poland,2014,pp.1–9.
| [159] V. Krishnamoorthi, |     | N.  | Carlsson, | D. Eager, | A.  | Mahanti, and |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --------- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
N.Shahmehri,“Helpinghandorhiddenhurdle:Proxy-assistedHTTP-
basedadaptivestreamingperformance,”inProc.IEEE21stInt.Symp.
MASCOTS,SanFrancisco,CA,USA,2013,pp.182–191.
[160] P. Georgopoulos, Y. Elkhatib, M. Broadbent, M. Mu, and N. Race, Thomas Zinner received the Diploma and Ph.D.
“Towardsnetwork-wideQoEfairnessusingopenflow-assistedadaptive
|     |     |     |     |     |     |     |     |     | degrees | in  | computer | science | from the | University |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------- | ------- | -------- | ---------- |
videostreaming,”inProc.ACMSIGCOMMWorkshopFutureHuman-
|     |     |     |     |     |     |     |     |     | of  | Würzburg, | Würzburg, | Germany, |     | in 2007 and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | -------- | --- | ----------- |
CentricMultimediaNetw.,2013,pp.15–20.
|     |     |     |     |     |     |     |     |     | 2012, | respectively. | His | Ph.D. | thesis | is on perfor- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------- | --- | ----- | ------ | ------------- |
[161] R. K. Mok, X. Luo, E. W. Chan, and R. K. Chang, “QDASH: A mance modeling of QoE-aware multipath video
QoE-aware DASH system,” in Proc. 3rd Annu. ACM Conf. MMSys, transmission in the future Internet. He is now the
ChapelHill,NC,USA,2012,pp.11–22.
Headofthe“NextGenerationNetworks”Research
| [162] T. Hoßfeld | et al.,   | “An economic |       | traffic management |             | approach to en- |     |     |         |              |                  |          |           |           |
| ---------------- | --------- | ------------ | ----- | ------------------ | ----------- | --------------- | --- | --- | ------- | ------------ | ---------------- | -------- | --------- | --------- |
|                  |           |              |       |                    |             |                 |     |     | Group,  | Chair        | of Communication |          | Networks, | Uni-      |
| able the         | triplewin | for users,   | ISPs, | overlay            | providers,” | in Towards      |     |     |         |              |                  |          |           |           |
|                  |           |              |       |                    |             |                 |     |     | versity | of Würzburg. |                  | His main | research  | interests |
the Future Internet—A European Research Perspective, G. Tselentis, cover video streaming techniques, implementation
J.Domingue,A.Galis,A.Gavras,D.Hausheer,S.Krco,V.Lotz,and
ofQoEawarenesswithinnetworks,software-defined
| T. Zahariadis, | Eds. | Amsterdam, |     | The Netherlands: |     | IOS Press, 2009, |     |     |     |     |     |     |     |     |
| -------------- | ---- | ---------- | --- | ---------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
networking(SDN)andnetworkvirtualization,networkfunctionvirtualization
ser.FutureInternetAssembly,pp.24–34.
|                                           |     |     |     |                           |     |     | and the benefits | of  | cloudification, | as  | well as the | performance | assessment | of  |
| ----------------------------------------- | --- | --- | --- | ------------------------- | --- | --- | ---------------- | --- | --------------- | --- | ----------- | ----------- | ---------- | --- |
| [163] InternetEngineeringTaskForce(IETF), |     |     |     | ALTOStatusPages.[Online]. |     |     |                  |     |                 |     |             |             |            |     |
thesetechnologiesandarchitectures.
Available:http://tools.ietf.org/wg/alto
[164] M.Jarschel,T.Zinner,T.Hoßfeld,P.Tran-Gia,andW.Kellerer,“Inter-
faces,attributes,usecases:AcompassforSDN,”IEEECommun.Mag.,
vol.52,no.6,pp.210–217,Jun.2014.
[165] P.Casas,M.Seufert,andR.Schatz,“YOUQMON:Asystemforon-
| line monitoring |     | of YouTube | QoE | in operational | 3G  | networks,” ACM |     |     |        |         |          |     |         |           |
| --------------- | --- | ---------- | --- | -------------- | --- | -------------- | --- | --- | ------ | ------- | -------- | --- | ------- | --------- |
|                 |     |            |     |                |     |                |     |     | Tobias | Hoßfeld | received | the | Diploma | and Ph.D. |
SIGMETRICSPerform.Eval.Rev.,vol.41,no.2,pp.44–46,Sep.2013.
|                   |     |                 |          |           |         |               |     |     | degrees | in        | computer  | science  | from the | University  |
| ----------------- | --- | --------------- | -------- | --------- | ------- | ------------- | --- | --- | ------- | --------- | --------- | -------- | -------- | ----------- |
| [166] S. Traverso | et  | al., “TailGate: | Handling | long-tail | content | with a little |     |     |         |           |           |          |          |             |
|                   |     |                 |          |           |         |               |     |     | of      | Würzburg, | Würzburg, | Germany, |          | in 2003 and |
helpfromfriends,”inProc.21stInt.Conf.WWW,Lyon,France,2012,
pp.151–160. 2009, respectively. His professional thesis (habili-
[167] M. Seufert et al., “Socially-aware traffic management,” in Social tation) was on “Modeling and analysis of Internet
applicationsandservices.”HehasbeenaProfessor
| Informatics—The |     | Social | Impact of | Interactions | Between | Humans and |     |     |     |         |           |             |     |             |
| --------------- | --- | ------ | --------- | ------------ | ------- | ---------- | --- | --- | --- | ------- | --------- | ----------- | --- | ----------- |
|                 |     |        |           |              |         |            |     |     | and | Head of | the Chair | of Modeling |     | of Adaptive |
IT,K.A.Zweig,W.Neuser,V.Pipek,M.Rohde,andI.Scholtes,Eds.
Systems,UniversityofDuisburg-Essen,Essen,Ger-
Berlin,Germany:Springer-Verlag,2014,pp.25–43.
many,since2014.Duringthetimeofthiswork,he
|     |     |     |     |     |     |     |     |     | was | heading | the “Future | Internet | Applications | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | -------- | ------------ | --- |
Overlays”ResearchGroup,ChairofCommunication
Michael Seufert received the Diploma degree in Networks,UniversityofWürzburg.Hehaspublishedmorethan100research
computer science in 2011 from the University of papersinmajorconferencesandjournals,receivingfourbestconferencepaper
Würzburg, Würzburg, Germany, where he is cur- awards,threeawardsforhisPh.D.thesis,andtheFredW.EllersickPrize2013
fromtheIEEECommunicationsSocietyforoneofhisarticlesonQoE.
|     |     | rently     | working | toward the | Ph.D. | degree. He ad-   |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | ------- | ---------- | ----- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | ditionally | passed  | the first  | state | examinations for |     |     |     |     |     |     |     |     |
teachingmathematicsandcomputerscienceinsec-
|     |     | ondary | schools. | From 2012–2013, |     | he was with |     |     |     |     |     |     |     |     |
| --- | --- | ------ | -------- | --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
FTWTelecommunicationResearchCenter,Vienna,
Austria,workingintheareaofuser-centeredinterac-
PhuocTran-GiaisaProfessorandDirectorofthe
tionandcommunicationeconomics.Heiscurrently
a Researcher at the Chair of Communication Net- Chair of Communication Networks, University of
works,UniversityofWürzburg.HisresearchmainlyfocusesonQoEofInternet Würzburg,Würzburg,Germany.Heisalsoamem-
|     |     |     |     |     |     |     |     |     | ber | of the | Advisory | Board of | Infosim | (Germany) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | -------- | ------- | --------- |
applications,socialnetworks,performancemodelingandanalysis,andtraffic
specializedinIPnetworkmanagementproductsand
managementsolutions.
|     |     |     |     |     |     |     |     |     | services. | He               | is also a | Cofounder     | and | Board Mem-    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------------- | --------- | ------------- | --- | ------------- |
|     |     |     |     |     |     |     |     |     | ber       | of Weblabcenter, |           | Inc. (Dallas, |     | TX), special- |
izedincrowdsourcingtechnologies.Hereceivedthe
Sebastian Egger received the master’s degree in DiplomaandPh.D.degreesinelectricalengineering
sociologyfromtheUniversityofGraz,Graz,Austria, fromtheUniversityofStuttgart,Germany,in1977,
and the Ph.D. degree in telecommunications from and from the University of Siegen, Germany, in
Graz University of Technology, Graz. Since 2010, 1982, respectively, and was at industries at Alcatel (SEL) and IBM Zurich
hehasbeeninvolvedinstandardizationactivitiesof
ResearchLaboratory.HeisactiveinseveralEUframeworkprojectsandCOST
theETSISTQandITU-TStudyGroup12onPerfor- actions.HewastheCoordinatoroftheGerman-wideG-LabProject“National
mance,QoS,andQoE.In2014,hejoinedtheDepart- Platform for Future Internet Studies” aimingto foster experimentally driven
mentofInnovationSystems,AITAustrianInstitute researchtoexploitfutureInternettechnologies.Hehaspublishedmorethan
ofTechnologyGmbH,Vienna,Austria,whereheis 100researchpapersinmajorconferencesandjournals.Hisresearchactivities
working on technology experience in the domains focusonperformanceanalysisofthefollowingmajortopics:FutureInternet
ofhuman-to-humanmediatedinteraction,interactive and Smartphone Applications; QoE Modeling and Resource Management;
services,andHCI.HismainresearchinterestsareinQualityofExperiencefor SoftwareDefinedNetworkingandCloudNetworks;NetworkDynamicsand
interactivespeech,videoandwebservices,aswellasHCIsupportsystemsfor Control; and Crowdsourcing. Prof. Tran-Gia was a recipient of the Fred W.
userswithspecialneeds.
EllersickPrize2013fromtheIEEECommunicationsSociety.