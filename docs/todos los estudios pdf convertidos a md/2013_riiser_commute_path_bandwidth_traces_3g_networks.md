Commute Path Bandwidth Traces from 3G Networks:
Analysis and Applications
Haakon Riiser1, Paul Vigmostad1, Carsten Griwodz2,3, Pål Halvorsen2,3
1OperaSoftwareASA,Norway
2SimulaResearchLaboratory,Norway
3DepartmentofInformatics,UniversityofOslo,Norway
{haakon.riiser, paulv}@opera.com
{griff, paalh}@ifi.uio.no
ABSTRACT “traffic from mobile devices tripled in 2011, ...
more than 20 % of global YouTube views come
In this dataset paper, we present and make available real-
frommobiledevices,and... YouTubeisavailable
worldmeasurementsofthethroughputthatwasachievedat
on 350 million devices.”
the application layer when adaptive HTTP streaming was
performed over 3G networks using mobile devices. For the Similarly,Sandvinereportsthat“real-timeentertainmentis
streamingsessions,weusedpopularcommuteroutesinand huge,globalandgrowing”[16,15]formobiledevices,where
aroundOslo(Norway)travelingwithdifferenttypesofpub- North America, Latin America, Europe and Asia-Pacific
lic transportation (metro, tram, train, bus and ferry). We have audio/video downstream mobile traffic of 27 %, 24 %,
also have a few logs using a car. Each log provides a times- 17 % and 14 %, respectively. Sandvine also predicts that
tamp, GPS coordinates and the measured number of bytes audioandvideostreamingwillexceed60%ofNorthAmer-
downloaded for approximately every second of the route. ica’s mobile data by late 2014. For mobile devices, Cisco’s
Thedatasetcanbeusedinseveralways,butthemostobvi- Visual Networking Index predicts an 18-fold increase from
ous application is to emulate the same network bandwidth 2011 to 2016 [2]. This trend is also enabled and fueled by
behavior (on specific geographical positions) for repeated allmajorcontentandserviceprovidersthatmakevideode-
experiments. livery“apps”to popular mobile video platforms. Thus, the
amountofmediadatastreamedtomobiledevicescomprises
CategoriesandSubjectDescriptors alreadyalargepartofthetotaldatadownloadedintheIn-
ternet, and the scope and size of mobile video streaming is
C.2.1 [Network Architecture and Design]: [Wireless
increasing at a very fast pace.
communication]
One challenge when delivering time-dependent data such
as audio and video to moving devices is the changing net-
GeneralTerms
work conditions and the resulting fluctuations in available
Experimentation, Measurement, Performance bandwidth. HTTP-based adaptive streaming [17], which is
tolerant to these fluctuations, is rapidly adopted by com-
mercialvendorsofstreamingtechnologytobeabletoadapt
Keywords
to resource availability. Using adaptive streaming protocols
bandwidthtraces,adaptivestreaming,bitrateadaption,mo- such as Microsoft’s Smooth Streaming [18], Apple’s HTTP
bile internet, 3G, wireless, fluctuating bandwidth LiveStreaming[9]orMPEG’sDynamicAdaptiveStreaming
overHTTP(DASH),adaptiveHTTPstreamingisnowalso
1. INTRODUCTION available on mobile devices. An adaptive streaming service
can be implemented as a combination of simple servers and
Mobile video streaming is an active area of research and
intelligent clients that make adaptation decisions based on
development that is driven both by the tremendous growth
localobservationssuchastheobservedbandwidthavailabil-
in smartphones and tablets, and by modern wireless net-
ity.
works capable of streaming video in real-time even while
An important question in these scenarios is how to best
the receiver is moving. For example, YouTube reports [4]
adapt the video quality (and thus the bitrate) to the avail-
that
ablenetworkbandwidth. Somestreamingsystemsavailable
today have been designed for wireless streaming, but deliv-
eringvideowithoutinterruptionsisconsiderablymorechal-
lenging when the client’s access network is a mobile wire-
Permissiontomakedigitalorhardcopiesofallorpartofthisworkfor
personalorclassroomuseisgrantedwithoutfeeprovidedthatcopiesare less network with severe and frequent bandwidth fluctua-
notmadeordistributedforprofitorcommercialadvantageandthatcopies tions and outages. In such scenarios, the behavior of the
bearthisnoticeandthefullcitationonthefirstpage.Tocopyotherwise,to qualityadaptionschemesvariesgreatlyamongthedifferent
republish,topostonserversortoredistributetolists,requirespriorspecific solutions [8, 10]. To avoid recurring buffer underruns and
permissionand/orafee.
frequent quality switches, both of which are harmful to the
MMSys’13,February26-March1,2013,Oslo,Norway.
viewer’s quality of experience, several research groups have
Copyright2013ACM978-1-4503-1894-5/13/02...$15.00.
114

|                                                |                 |         |           |          |              |            |         | 1289406399 | 549692 | 59.851754 |     | 10.781778 |     | 248069 | 1008 |
| ---------------------------------------------- | --------------- | ------- | --------- | -------- | ------------ | ---------- | ------- | ---------- | ------ | --------- | --- | --------- | --- | ------ | ---- |
| evaluated                                      | the performance |         | of        | adaption | schemes      | [5,        | 8, 10]  |            |        |           |     |           |     |        |      |
|                                                |                 |         |           |          |              |            |         | 1289406400 | 550772 | 59.851864 |     | 10.781833 |     | 191698 | 1080 |
| (and proposed                                  |                 | changes | [11]).    | However, | they         | all use    | differ- |            |        |           |     |           |     |        |      |
|                                                |                 |         |           |          |              |            |         | 1289406401 | 551773 | 59.851964 |     | 10.781901 |     | 280579 | 1001 |
| ent bandwidth                                  |                 | traces  | due to    | lack of  | an available | dataset,   |         |            |        |           |     |           |     |        |      |
|                                                |                 |         |           |          |              |            |         | 1289406402 | 552893 | 59.85206  |     | 10.781969 |     | 248971 | 1120 |
| e.g., Akhshabietal.[5]usedasyntheticbandwidth, |                 |         |           |          |              |            | Mu¨ller |            |        |           |     |           |     |        |      |
| et al. [8]                                     | used real-world |         | bandwidth | traces   | from         | Klagenfurt |         |            |        |           |     |           |     |        |      |
(Austria) and Riiser et al. [10] used real-world bandwidth Figure 1: Sample log data.
| traces from | Oslo | (Norway). | Even | though | the | experiments |     |     |     |     |     |     |     |     |     |
| ----------- | ---- | --------- | ---- | ------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
showsimilartrends[8,10],theyarenotdirectlycomparable
since the authors have used different network traces. With and bandwidth plots) and custom-made software useful for
the dataset made available with this paper, we allow future simulationshavebeenmadeavailableonline[14]. Thedataset
researchers to reuse our traces, which we created during in- currentlyconsistsof86tracesfrom11differentroutes. The
vestigationsresultinginseveralarticles[6,7,10,11,13],and logs are in plain ASCII text, with six fields of data per log
compare the results directly. entry, as shown in figure 1. The data fields are defined as
follows:
ThedatasetmostlycontainsbandwidthlogsfromTelenor’s
| 3G mobile | network | in  | and around | Oslo. |     | The network | is  |     |     |     |     |     |     |     |     |
| --------- | ------- | --- | ---------- | ----- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• Column1istheUnixtimestamp(numberofseconds
| based on | the Universal |            | Mobile   | Telecommunications |        |        | System |       |             |     |          |        |     |     |     |
| -------- | ------------- | ---------- | -------- | ------------------ | ------ | ------ | ------ | ----- | ----------- | --- | -------- | ------ | --- | --- | --- |
|          |               |            |          |                    |        |        |        | since | 1970-01-01) | of  | the data | point. |     |     |     |
| (UMTS)   | and the       | High-Speed | Downlink |                    | Packet | Access | (HS-   |       |             |     |          |        |     |     |     |
DPA) architectures. The dataset includes bandwidth mea- • Column 2 is a monotonically increasing times-
surements from popular commute routes in Oslo and a few tamp in milliseconds(sincesomeunspecifiedstart-
| otherexamples. |            | Thecommuteroutesallhavemultiplesam- |      |       |        |                |     | ing | point). |     |     |     |     |     |     |
| -------------- | ---------- | ----------------------------------- | ---- | ----- | ------ | -------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
| ples, and      | all routes | come                                | with | a map | of the | path. Further- |     |     |         |     |     |     |     |     |     |
more, we present statistics from the network traffic. This • Columns 3 and 4 are GPS coordinates in decimal
datawascollectedattheapplication-levelinaHTTP-based degrees. Column3isthelatitudecoordinateandcol-
media streaming client. Hence, it does not contain packet- umn 4 is the longitude coordinate.
| level information |     | similar | to tcpdump. |     | Bandwidth | numbers |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------- | ----------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• Column5isthenumberofbytesreceivedsincethe
areone-secondaverages,asthiswassufficientforthemedia
|           |             |     |           |          |     |            |     | previous | measurement |     | (the | previous | line | in the | log). |
| --------- | ----------- | --- | --------- | -------- | --- | ---------- | --- | -------- | ----------- | --- | ---- | -------- | ---- | ------ | ----- |
| streaming | simulations |     | for which | the data | was | originally | in- |          |             |     |      |          |      |        |       |
tented. We hope that the dataset can be used by others to • Column 6 is the number of milliseconds elapsed
advanceresearchinthefieldandprovidebettersystemsup- since the previous measurement (the previous line in
portformobileapplicationslikeadaptivevideostreaming. thelog). Column6equalsthedifferenceinthecolumn
|     |     |     |     |     |     |     |     | 2 values | of  | this and | the previous |     | line. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | ------------ | --- | ----- | --- | --- |
2. MEASUREMENTSANDLOGS
Thismeansthatothertypesofinformationcaneasilybeex-
We have earlier reported significant fluctuations in net- tracted,e.g.,togetkilobytespersecondforaspecificsample,
work conditions when streaming video over HSDPA net- simply divide column 5 by column 6.
| works [12]. | To        | summarize    | our | earlier | results,   | we have   | per- |                        |     |     |     |     |     |     |     |
| ----------- | --------- | ------------ | --- | ------- | ---------- | --------- | ---- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| formed      | bandwidth | measurements |     | in      | real-world | streaming |      |                        |     |     |     |     |     |     |     |
|             |           |              |     |         |            |           |      | 3. ROUTESANDBANDWIDTHS |     |     |     |     |     |     |     |
scenariosalongseveralcommuteroutesinandaroundOslo,
|         |       |          |               |     |     |      |         | In the  | previous      | section, | we presented |       | the logs, | and         | here, |
| ------- | ----- | -------- | ------------- | --- | --- | ---- | ------- | ------- | ------------- | -------- | ------------ | ----- | --------- | ----------- | ----- |
| Norway. | Based | on these | measurements, |     | we  | have | built a |         |               |          |              |       |           |             |       |
|         |       |          |               |     |     |      |         | we give | some examples |          | of the used  | paths | with      | correspond- |       |
datasetovermultipleroutesbyloggingthedownloadband-
|     |     |     |     |     |     |     |     | ing bandwidth | measurement |     | information. |     | With | a   | few ex- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | ------------ | --- | ---- | --- | ------- |
widthobservedwhilestreamingvideooverHTTP.Asamo-
|            |           |     |          |         |       |         |     | ceptions, | we selected | popular | commute       |     | routes  | to      | or from |
| ---------- | --------- | --- | -------- | ------- | ----- | ------- | --- | --------- | ----------- | ------- | ------------- | --- | ------- | ------- | ------- |
| bile video | receiver, | we  | used the | Netview | Media | Client1 | [1] |           |             |         |               |     |         |         |         |
|            |           |     |          |         |       |         |     | downtown  | Oslo,       | Norway. | For different |     | routes, | we also | used    |
runningonlaptopsequippedwithaGPS(HaicomHI-204III
|             |     |            |         |             |       |        |        | different   | types of  | public | transportation |     | (metro,      | bus, | ferry, |
| ----------- | --- | ---------- | ------- | ----------- | ----- | ------ | ------ | ----------- | --------- | ------ | -------------- | --- | ------------ | ---- | ------ |
| USB GPS)    | and | a 3G modem | (Huawei |             | Model | E1752  | HSPA   |             |           |        |                |     |              |      |        |
|             |     |            |         |             |       |        |        | train, tram | and car). | In     | the following  |     | subsections, | we   | list a |
| USB stick). | The | sender     | was     | a dedicated |       | server | with a |             |           |        |                |     |              |      |        |
fewexamples(ofthetotal11routes)withmapsoftheroutes
| 100 Mbit/s | Ethernet | connection, |     | located | near | the receiver. |     |           |        |         |          |           |     |               |     |
| ---------- | -------- | ----------- | --- | ------- | ---- | ------------- | --- | --------- | ------ | ------- | -------- | --------- | --- | ------------- | --- |
|            |          |             |     |         |      |               |     | and plots | of the | average | observed | bandwidth |     | over multiple |     |
Thiswasdonesothatourbandwidthandlatencymeasure-
ments indicate the performance of the wireless 3G connec- measurementsasafunctionofthepathposition(astraveled
|                                                  |             |     |        |            |       |             |     | distance | from the  | start). | Note        | that some | of   | the maps     | are |
| ------------------------------------------------ | ----------- | --- | ------ | ---------- | ----- | ----------- | --- | -------- | --------- | ------- | ----------- | --------- | ---- | ------------ | --- |
| tion,withminimalinterferencefromthewirednetwork. |             |     |        |            |       |             | For |          |           |         |             |           |      |              |     |
|                                                  |             |     |        |            |       |             |     | slightly | stretched | to fit  | the format, | and       | that | the measured |     |
| example,                                         | we observed |     | packet | round-trip | times | of approxi- |     |          |           |         |             |           |      |              |     |
bandwidthsinthebandwidthplotsarecalculatedoveraone
| mately 80  | ms   | between | the server | and | the     | client, and | the |                 |     |     |     |     |     |     |     |
| ---------- | ---- | ------- | ---------- | --- | ------- | ----------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
|            |      |         |            |     |         |             |     | second average. |     |     |     |     |     |     |     |
| round-trip | time | between | the server |     | and the | last node   | be- |                 |     |     |     |     |     |     |     |
fore the wireless hop was less than 2 ms. Thus, more than 3.1 Metrorailway
97%oftheobservedend-to-endlatencywasduetothefinal
|     |     |     |     |     |     |     |     | A popular | means | of  | commuting | in  | Oslo | is the | metro. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | --- | --------- | --- | ---- | ------ | ------ |
wireless hop.
Thisisanelectricpassengerrailwaywhereallthelinespass
| The Netview |         | Media   | Client | uses GPSD | [3]        | to communi- |       |         |             |         |     |          |       |     |     |
| ----------- | ------- | ------- | ------ | --------- | ---------- | ----------- | ----- | ------- | ----------- | ------- | --- | -------- | ----- | --- | --- |
|             |         |         |        |           |            |             |       | through | underground | tunnels | in  | downtown | Oslo. | The | un- |
| cate with   | the GPS | device, | and    | counts    | the number | of          | bytes |         |             |         |     |          |       |     |     |
dergroundpartofourtestedmetrocommuterouteisshown
| received | every | second. | It periodically |     | reports | to a | remote |     |     |     |     |     |     |     |     |
| -------- | ----- | ------- | --------------- | --- | ------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
database the GPS coordinates, timestamps, and bytes re- with the dotted line in figure 2(a).
Figure2(b)showsthemeasuredbandwidthalongthemetro
| ceivedsincethelastmeasurement. |     |     |     | Thedataset(logs,maps, |     |     |     |           |                  |     |      |     |             |     |         |
| ------------------------------ | --- | --- | --- | --------------------- | --- | --- | --- | --------- | ---------------- | --- | ---- | --- | ----------- | --- | ------- |
|                                |     |     |     |                       |     |     |     | path. All | the measurements |     | show | the | same trend, |     | and the |
1The Netview Media Client that was used to record this signal and bandwidth availability are predictable with only
data is proprietary (owned by Opera Software), hence we minor variations. The experienced bandwidth is typically
cannot distribute it together with the dataset. a bit above 1 Mbit/s when the metro is above the ground.
115

(a) Map. (b) Measured bandwidth. (a) Map. (b) Measured bandwidth.
Figure 2: Metro commute path: from Kalbakken Figure 4: Ferry commute path: Oslo ferry route
to Jernbanetorget in Oslo (the dotted line is in a between Nesodden and Aker Brygge.
tunnel).
ofspaceonboardandtablesforPCsanddeviceswithlarge
However,whenenteringthetunnelsafterapproximately5.5
|             |      |     |          |            |         |          | screens, | this   | way of  | commuting |     | is one that | is           | well suited |
| ----------- | ---- | --- | -------- | ---------- | ------- | -------- | -------- | ------ | ------- | --------- | --- | ----------- | ------------ | ----------- |
| kilometers, | both | the | Internet | connection | and the | GPS sig- |          |        |         |           |     |             |              |             |
|             |      |     |          |            |         |          | to use   | mobile | devices | during    | the | ferry       | ride. Figure | 4(b)        |
nalareessentiallylost(inperiodswithoutaGPSsignal,the
|          |              |     |       |              |              |      | shows    | that the | available | bandwidth |        | depends      | strongly | the      |
| -------- | ------------ | --- | ----- | ------------ | ------------ | ---- | -------- | -------- | --------- | --------- | ------ | ------------ | -------- | -------- |
| position | is estimated |     | based | on the metro | time table). | This |          |          |           |           |        |              |          |          |
|          |              |     |       |              |              |      | position | along    | the trip. | The       | signal | is strongest |          | when the |
means that when the metro was underground (the dotted ferry is close to land (Nesodden at the start of the path,
| line), | we were | hardly | able | to receive any | data at | all. |                         |        |     |          |                             |      |          |         |
| ------ | ------- | ------ | ---- | -------------- | ------- | ---- | ----------------------- | ------ | --- | -------- | --------------------------- | ---- | -------- | ------- |
|        |         |        |      |                |         |      | and Aker                | Brygge | in  | downtown | Oslo)                       | with | observed | average |
|        |         |        |      |                |         |      | bandwidthsabove2Mbit/s. |        |     |          | However,thesignalconditions |      |          |         |
3.2 Bus
|     |     |     |     |     |     |     | far from   | land      | are usually |            | problematic. | The         | signal   | is never   |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----------- | ---------- | ------------ | ----------- | -------- | ---------- |
|     |     |     |     |     |     |     | completely | gone      | while       | crossing   | the          | Oslo-fjord, |          | but the 3G |
|     |     |     |     |     |     |     | users      | rarely    | experience  | bandwidths |              | above       | 1 Mbit/s | in this    |
|     |     |     |     |     |     |     | part of    | the path. |             |            |              |             |          |            |
3.4 Tram
|          | (a)           | Map      |           | (b) Measured   | bandwidth. |              |         |        |      |         |         |          |            |       |
| -------- | ------------- | -------- | --------- | -------------- | ---------- | ------------ | ------- | ------ | ---- | ------- | ------- | -------- | ---------- | ----- |
| Figure   | 3: Bus        | commute  |           | path: Oslo     | bus along  | Mos-         |         |        |      |         |         |          |            |       |
| seveien, | between       |          | Ljan and  | Oslo Central   | Station.   |              |         |        |      |         |         |          |            |       |
|          |               |          |           |                |            |              |         | (a)    | Map. |         | (b)     | Measured | bandwidth. |       |
| Figures  | 3(a)          | and 3(b) | show      | a bus          | path going | into Oslo    |         |        |      |         |         |          |            |       |
| and the  | corresponding |          | bandwidth | measurements,  |            | respec-      |         |        |      |         |         |          |            |       |
|          |               |          |           |                |            |              | Figure  | 5:     | Tram | commute | path:   | Oslo     | tram       | route |
| tively.  | The           | average  | values    | in figure 3(b) | vary       | greatly, but |         |        |      |         |         |          |            |       |
|          |               |          |           |                |            |              | between | Ljabru | and  | Oslo    | Central | Station. |            |       |
themeasurementsshowthataminimumbandwidthofabout
| 1.5 Mbit/s | should    | normally |           | be possible | with an    | average of  |     |     |     |     |     |     |     |     |
| ---------- | --------- | -------- | --------- | ----------- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| about      | 2 Mbit/s. | A        | challenge | using       | this route | is that the |     |     |     |     |     |     |     |     |
busroutehasasteephillontheeastside,whichpreventsa Another method of commuting in Oslo using public trans-
stablereceptionofsignalsfromeasternGPSsatellites. Fur- portation is by tram. Figure 5(a) shows one of the tested
thermore, the Oslofjord is in the west, leaving few possible tram routes, whose tracks are parallel to but high above
sites for 3G towers on that side. Consequently, both the the bus route presented above. Observed bandwidth is pre-
GPS and the UMTS signals are unstable. sented in figure 5(b). Along the whole path, we have found
|     |     |     |     |     |     |     | acceptablebutfluctuatingbandwidth. |     |     |     |     | Inthefirstpartofthe |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | ------------------- | --- | --- |
3.3 Ferry route, weobservedaverypredictablebandwidthacrossthe
|     |     |     |     |     |     |     | different | measurements, |     | though | rarely | exceeding |     | 1 Mbit/s. |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ------ | ------ | --------- | --- | --------- |
Our third scenario is traveling by ferry (figure 4(a)). Most At a long down-slope towards the end of the trip, the mea-
commuters from the Nesodden peninsula travel by ferry to surements vary more (larger standard deviation), but the
Oslo, as traveling by car requires a large detour. With lots average bandwidth is almost the same.
116

| 3.5 | Train |     |     |     |     |     |     | 4. EXAMPLESOFUSE |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
Inourwork,wehaveusedthebandwidthmeasurementsto
|     |     |     |     |     |     |     |     | emulateidenticalnetworkbehaviorfor      |           |           |            |           | videostreamingses- |               |           |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --------- | --------- | ---------- | --------- | ------------------ | ------------- | --------- |
|     |     |     |     |     |     |     |     | sions using                             | adaptive  | HTTP      |            | streaming | protocols.         |               | The goal  |
|     |     |     |     |     |     |     |     | was to evaluate                         |           | different | adaption   |           | strategies,        | i.e.,         | decisions |
|     |     |     |     |     |     |     |     | on how                                  | to change | from      | one        | quality   | (and thus          | bitrate)      | level     |
|     |     |     |     |     |     |     |     | to another,                             | as        | a user    | moves      | along     | a path             | while viewing | a         |
|     |     |     |     |     |     |     |     | videoinaVideo-on-Demandscenario[10,11]. |           |           |            |           |                    | Additionally, |           |
|     |     |     |     |     |     |     |     | we have                                 | used the  | logs      | to emulate | the       | network            | in a          | scenario  |
wherethelogsareusedtomakealocation-basedbandwidth-
|     |     |      |     |     |          |            |     | lookup                                          | service     | [13, 11] | which      | also       | may be   | combined | with a    |
| --- | --- | ---- | --- | --- | -------- | ---------- | --- | ----------------------------------------------- | ----------- | -------- | ---------- | ---------- | -------- | -------- | --------- |
|     |     |      |     |     |          |            |     | transparent                                     | handover    |          | between    | multiple   | networks | [7,      | 6].       |
|     |     |      |     |     |          |            |     | To produce                                      | the         | same     | network    | conditions |          | for all  | tests, we |
|     |     |      |     |     |          |            |     | developed                                       | a bandwidth |          | throttling |            | module   | for the  | Apache    |
|     | (a) | Map. |     | (b) | Measured | bandwidth. |     |                                                 |             |          |            |            |          |          |           |
|     |     |      |     |     |          |            |     | webserver(alsoavailablefromthedatasetweb-page). |             |          |            |            |          |          | This      |
moduletakesasinputabandwidthlog,likethelogsavailable
| Figure6: | Traincommutepath: |     |     |     | Trainroutebetween |     |     |     |     |     |     |     |     |     |     |
| -------- | ----------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inthisdataset,thatcontainsasinglekbit/snumberforevery
Oslo and Vestby. second of the session. After loading the bandwidth log, the
|     |     |     |     |     |     |     |     | first HTTP | request | starts  | the      | session. | At  | time t     | after the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- | -------- | -------- | --- | ---------- | --------- |
|     |     |     |     |     |     |     |     | session    | starts, | the web | server’s | maximum  |     | throughput | for       |
The trains to and from Oslo are frequently used by peo- the next second will be B(t), where B(t) is the bandwidth
ple traveling longer distances, and in figure 6, we show the attimetinthelogthatwasusedasinputtothethrottling
map and bandwidth plot for the 40 km long Oslo–Vestby module. This approach means that the client program, i.e.,
route. We observe large fluctuations in bandwidth, some- the media player in our HTTP streaming scenario, can get
timesjumpingbetween3Mbit/sandalmostnoconnectivity exactlythesamebandwidthconditionseverytime,ensuring
at all. both fairness and reproducibility in our experiments, while
|     |     |     |     |     |     |     |     | at the same | time | being | as realistic |     | as a field | trial. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ----- | ------------ | --- | ---------- | ------ | --- |
3.6 Car
|     |     |     |     |     |     |     |     | 5. CONCLUSION                        |           |              |         |      |                   |             |         |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --------- | ------------ | ------- | ---- | ----------------- | ----------- | ------- |
|     |     |     |     |     |     |     |     | We have                              | provided  | a            | dataset | that | enables           | researchers | to      |
|     |     |     |     |     |     |     |     | simulate                             | bandwidth | fluctuations |         | as   | observed          | in a        | live 3G |
|     |     |     |     |     |     |     |     | networkinvehicularmobilityscenarios. |           |              |         |      | Usingthisdataset, |             |         |
researcherscantesttheirideasusingrealisticnetworktraces,
|     |     |     |     |     |     |     |     | and get            | reproducible |     | results | useful | for comparisons |     | with    |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ------------ | --- | ------- | ------ | --------------- | --- | ------- |
|     |     |     |     |     |     |     |     | other researchers. |              | We  | hope    | that   | the dataset     | can | be used |
topushresearchforwardinthefieldofdatadeliverytomo-
|     |     |     |     |     |     |     |     | bile devices, | and | in streaming |     | scenarios | in  | particular. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | --------- | --- | ----------- | --- |
Acknowledgements
(a) Map. (b) Measured bandwidth. This work has been performed in the context of the HyS-
|        |        |       |         |     |       |           |     | tream project      | (project |            | number   | 176847)  | and      | the iAD | centre |
| ------ | ------ | ----- | ------- | --- | ----- | --------- | --- | ------------------ | -------- | ---------- | -------- | -------- | -------- | ------- | ------ |
|        |        |       |         |     |       |           |     | for Research-based |          | Innovation |          | (project | number   | 174867) | –      |
| Figure | 7: Car | path: | Driving |     | a car | from Oslo | to  |                    |          |            |          |          |          |         |        |
|        |        |       |         |     |       |           |     | both funded        | by       | Norwegian  | Research |          | Council. |         |        |
Grimstad.
| The route | Oslo–Grimstad, |     | shown |     | in figure | 7(a), is used | by  |     |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ----- | --- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
everyone driving from Oslo going south on the E18 high- 6. REFERENCES
| way. Itisanapproximately280kilometerdrive. |     |     |     |     |     | Figure7(b) |     |             |       |         |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | ---------- | --- | ----------- | ----- | ------- | --- | --- | --- | --- | --- |
|                                            |     |     |     |     |     |            |     | [1] Netview | Media | Client. |     |     |     |     |     |
showstheachievedbandwidth,whereweobservedhighpeaks
http://www.netview.no/
| over3Mbit/swithanaverageofabout1Mbit/s. |     |     |     |     |     | However, |     |                            |     |     |     |     |       |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | -------------------------- | --- | --- | --- | --- | ----- | --- | --- |
|                                         |     |     |     |     |     |          |     | index.php?page=downloader, |     |     |     |     | 2011. |     |     |
asalsoseenintheplot,thereareseveralareaswith(nearly)
no available bandwidth. [2] Cisco visual networking index: Forecast and
|     |     |     |     |     |     |     |     | methodology, |     | 2011-2016. |     | http://www.cisco.com/en/ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- | ------------------------ | --- | --- | --- |
US/solutions/collateral/ns341/ns525/ns537/
3.7 Summary
ns705/ns827/white_paper_c11-481360_ns827_
|             |     |           |       |          |     |                   |     | Networking_Solutions_White_Paper.html, |     |       |         |         |     | 2012. |     |
| ----------- | --- | --------- | ----- | -------- | --- | ----------------- | --- | -------------------------------------- | --- | ----- | ------- | ------- | --- | ----- | --- |
| In summary, |     | the above | plots | indicate |     | that the achieved |     |                                        |     |       |         |         |     |       |     |
|             |     |           |       |          |     |                   |     | [3] GPSD                               | —   | a GPS | service | daemon. |     |       |     |
bandwidthoscillatesseverelywhenusingmovingmobilede-
vices. How much depends on the geographical location and http://catb.org/gpsd/index.html, 2012.
the speed of the moving vehicle, and this behavior is def- [4] YouTube statistics.
initely something that should be taken into account when http://www.youtube.com/t/press_statistics, Nov.
| designing | systems | for | the mobile | scenario. |     |     |     | 2012. |     |     |     |     |     |     |     |
| --------- | ------- | --- | ---------- | --------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
117

[5] S. Akhshabi, A. C. Begen, and C. Dovrolis. An HTTP: Standards and design principles. In
experimental evaluation of rate-adaptation algorithms Proceedings of the ACM International Conference on
in adaptive streaming over http. In Proceedings of the Multimedia Systems (MMSys), pages 133–144, Feb.
| ACM | International |     | Conference |     | on Multimedia |     |     | 2011. |
| --- | ------------- | --- | ---------- | --- | ------------- | --- | --- | ----- |
Systems (MMSys), pages 157–168, Feb. 2011. [18] A. Zambelli. Smooth streaming technical overview.
[6] K. Evensen, A. Petlund, H. Riiser, P. Vigmostad, http://learn.iis.net/page.aspx/626/
D. Kaspar, C. Griwodz, and P. Halvorsen. Demo: smooth-streaming-technical-overview/, 2009.
| Quality-adaptive                               |               | video          | streaming      |              | with            | dynamic    |         |     |
| ---------------------------------------------- | ------------- | -------------- | -------------- | ------------ | --------------- | ---------- | ------- | --- |
| bandwidth                                      |               | aggregation    | on             | roaming,     | multi-homed     |            |         |     |
| clients                                        | (demo).       | In Proceedings |                | of           | the ACM         |            |         |     |
| International                                  |               | Conference     |                | on Mobile    | Systems,        |            |         |     |
| Applications                                   |               | and Services   |                | (MobiSys),   | June            | 2011.      |         |     |
| [7] K. Evensen,                                |               | A. Petlund,    | H.             | Riiser,      | P.              | Vigmostad, |         |     |
| D. Kaspar,                                     |               | C. Griwodz,    | and            | P.           | Halvorsen.      | Mobile     |         |     |
| video                                          | streaming     | using          | location-based |              | network         |            |         |     |
| predictionandtransparenthandover.InProceedings |               |                |                |              |                 |            | of      |     |
| the ACM                                        | International |                | Workshop       |              | on Network      |            | and     |     |
| Operating                                      | Systems       |                | Support        | for Digital  |                 | Audio      | and     |     |
| Video                                          | (NOSSDAV),    |                | June           | 2011.        |                 |            |         |     |
| [8] C. Mu¨ller,                                | S.            | Lederer,       | and            | C. Timmerer. |                 | An         |         |     |
| evaluation                                     | of            | dynamic        | adaptive       |              | streaming       | over       | http in |     |
| vehicular                                      | environments. |                | In             | Proceeding   |                 | of the     | ACM     |     |
| Workshop                                       | on            | Mobile         | Video          | (MoVid),     | Feb.            | 2012.      |         |     |
| [9] R. Pantos                                  | and           | W.             | May. HTTP      |              | live streaming. |            |         |     |
http://tools.ietf.org/html/
| draft-pantos-http-live-streaming-07,  |             |                  |            |                 |                   | 2011.         |          |     |
| ------------------------------------- | ----------- | ---------------- | ---------- | --------------- | ----------------- | ------------- | -------- | --- |
| [10] H. Riiser,                       | H.          | S. Bergsaker,    |            | P. Vigmostad,   |                   | C.            | Griwodz, |     |
| and P.                                | Halvorsen.  | A                | comparison |                 | of quality        | scheduling    |          |     |
| in commercial                         |             | adaptive         | http       | streaming       |                   | solutions     | on a     |     |
| 3g network.                           |             | In Proceedings   |            | of the          | ACM               | Workshop      | on       |     |
| Mobile                                | Video       | (MoVid),         | Feb.       | 2012.           |                   |               |          |     |
| [11] H. Riiser,                       | T.          | Endestad,        | P.         | Vigmostad,      |                   | C. Griwodz,   |          |     |
| and P.                                | Halvorsen.  | Video            | streaming  |                 | using             | a             |          |     |
| location-based                        |             | bandwidth-lookup |            |                 | service           | for           | bitrate  |     |
| planning.                             | ACM         | Transactions     |            | on              | Multimedia        |               |          |     |
| Computing,                            |             | Communications   |            | and             | Applications      |               |          |     |
| (TOMCCAP),                            |             | 8(3),            | 2012.      |                 |                   |               |          |     |
| [12] H. Riiser,                       | P.          | Halvorsen,       | C.         | Griwodz,        | and               | B.            | Hestnes. |     |
| Performance                           |             | measurements     |            | and             | evaluation        | of            | video    |     |
| streaming                             | in          | HSDPA            | networks   | with            | 16QAM             |               |          |     |
| modulation.                           |             | In Proceedings   |            | of the          | IEEE              | International |          |     |
| conference                            | on          | Multimedia       |            | and Expo        | (ICME),           |               | pages    |     |
| 489–492,                              | June        | 2008.            |            |                 |                   |               |          |     |
| [13] H. Riiser,                       | P.          | Vigmostad,       |            | C. Griwodz,     |                   | and           |          |     |
| P. Halvorsen.                         |             | Bitrate          | and        | video           | quality           | planning      | for      |     |
| mobile                                | streaming   | scenarios        |            | using           | a gps-based       |               |          |     |
| bandwidth                             |             | lookup           | service.   | In Proceedings  |                   | of            | the IEEE |     |
| International                         |             | Conference       |            | on Multimedia   |                   | and           | Expo     |     |
| (ICME),                               | July        | 2011.            |            |                 |                   |               |          |     |
| [14] H. Riiser,                       | P.          | Vigmostad,       |            | C. Griwodz,     |                   | and           |          |     |
| P. Halvorsen.                         |             | DATASET:         |            | HSDPA-bandwidth |                   |               | logs for |     |
| mobile                                | HTTP        | streaming        |            | scenarios.      | http://home.ifi.  |               |          |     |
| uio.no/paalh/dataset/hsdpa-tcp-logs/, |             |                  |            |                 |                   | Oct.          | 2012.    |     |
| [15] Sandvine                         | Intelligent |                  | Broadband  |                 | Networks.         | Global        |          |     |
| internet                              | phenomena   |                  | report:    | 1h              | 2012. http://www. |               |          |     |
sandvine.com/news/global_broadband_trends.asp,
| Apr.          | 2012.       |          |           |     |           |            |     |     |
| ------------- | ----------- | -------- | --------- | --- | --------- | ---------- | --- | --- |
| [16] Sandvine | Intelligent |          | Broadband |     | Networks. | Sandvine   |     |     |
| report:       | Mobile      | networks | teeming   |     | with      | streaming. |     |     |
http://www.sandvine.com/news/pr_detail.asp?
| ID=366,              | Apr. | 2012.   |     |          |           |     |      |     |
| -------------------- | ---- | ------- | --- | -------- | --------- | --- | ---- | --- |
| [17] T. Stockhammer. |      | Dynamic |     | adaptive | streaming |     | over |     |
118