Mahimahi: Accurate Record-and-Replay for HTTP
Ravi Netravali, Anirudh Sivaraman, Somak Das, and Ameesh Goyal, MIT CSAIL;
Keith Winstein, Stanford University; James Mickens, Harvard University;
Hari Balakrishnan, MIT CSAIL
https://www.usenix.org/conference/atc15/technical-session/presentation/netravali
This paper is included in the Proceedings of the
2015 USENIX Annual Technical Conference (USENIC ATC ’15).
July 8–10, 2015 • Santa Clara, CA, USA
ISBN 978-1-931971-225
Open access to the Proceedings of the
2015 USENIX Annual Technical Conference
(USENIX ATC ’15) is sponsored by USENIX.

Mahimahi:AccurateRecord-and-ReplayforHTTP
RaviNetravali*,AnirudhSivaraman*,SomakDas*,AmeeshGoyal*,KeithWinstein†,JamesMickens‡,HariBalakrishnan*
*MITCSAIL †StanfordUniversity ‡HarvardUniversity
ravinet,anirudh,somakrdas,ameesh,hari @csail.mit.edu,keithw@cs.stanford.edu,mickens@eecs.harvard.edu
{ }
Abstract appswithinmobile-phoneemulators)canberununmod-
ifiedwithinMahimahi.Additionally,Mahimahi’sreplay
ThispaperpresentsMahimahi,aframeworktorecord
semantics can be extended to support the server-side
trafficfromHTTP-basedapplications,andlaterreplayit
logicofmanyapplications,suchasYouTube.
underemulatednetworkconditions.Mahimahiimproves
Mahimahi has three notable features that distinguish
uponpriorrecord-and-replayframeworksinthreeways.
it from other record-and-replay tools such as Google’s
First,itismoreaccuratebecauseitcarefullyemulatesthe
web-page-replay[11]andFiddler[34]:
multi-server natureofWebapplications,presentin98%
oftheAlexaUSTop500Webpages.Second,itisolates 1. Accuracy: Mahimahi is careful about emulating
themulti-servernatureofWebapplications.Instead
itsownnetworktraffic,allowingmultipleMahimahiin-
of responding to all requests from a single server,
stancesemulatingdifferentnetworkstorunconcurrently
Mahimahicreatesaseparateserverforeachdistinct
withoutmutualinterference.Andthird,itisdesignedas
servercontactedwhilerecording.Wefindthatem-
asetofcomposableshells,providingease-of-useandex-
ulatingmultipleserversisakeyfactorinaccurately
tensibility.
measuringWebpageloadtimes( 4.1).
We evaluate Mahimahi by: (1) analyzing the perfor- §
2. Isolation: Using Linux’s network namespaces [7],
manceofHTTP/1.1,SPDY,andQUIConacorpusof500
Mahimahiisolatesitstrafficfromtherestofthehost
sites,(2)usingMahimahitounderstandthereasonswhy
system, allowing multiple instances of its shells to
these protocols are suboptimal, (3) developing Cumu-
run in parallel with no mutual interference ( 4.2).
lus, a cloud-based browser designed to overcome these §
Becauseothertoolsmodifythenetworkconfigura-
problems, using Mahimahi both to implement Cumulus
tionoftheentirehost[11,34],theycannotprovide
byextendingoneofitsshells,andtoevaluateit,(4)us-
thisfeature.
ing Mahimahi to evaluate HTTP multiplexing protocols
3. Composability and extensibility: Mahimahi is
on multiple performance metrics (page load time and
structuredasasetofUNIXshells,allowingtheuser
speed index), and (5) describing how others have used
torununmodifiedclientbinarieswithineachshell.
Mahimahi.
RecordShellallowsausertorecordallHTTPtraffic
1 INTRODUCTION for any process spawned within it. ReplayShell re-
playsrecordedcontentusinglocalserversthatem-
HTTPisthedefactocommunicationprotocolforclient-
ulate the application servers. To emulate network
server applications today [27]. Beyond its widespread
conditions, Mahimahi includes DelayShell, which
use as an application-layer protocol for loading Web
emulates a fixed network propagation delay, and
pages, HTTP is now used for mobile apps [22], video
LinkShell, which emulates both fixed-capacity and
streaming[14],andinstantmessaging[19].
variable-capacity links. These shells can be nested
It is useful to evaluate the performance of these ap-
within one another, allowing the user to flexibly
plicationsundercontrolledexperimentalconditions.For
experiment with many different network configu-
example,browserdevelopersmaywishtoevaluatehow
rations. Mahimahi makes it easy to modify these
changes to their document object model (DOM) and
shellsandaddnewones;e.g.,torecord-and-replay
JavaScript parsers affect Web page load times, while
YouTubevideos,emulatepacketlosses,implement
network-protocoldesignersmightwanttounderstandthe
activequeuemanagementalgorithms,etc.( 4.3).
application-level impact of new multiplexing protocols §
WeusedMahimahitoevaluateWebmultiplexingpro-
like QUIC [30]. Similarly, a mobile app developer may
tocols.WewereabletoeasilyextendMahimahitosup-
wish to determine the user-perceived latency [28] for
port QUIC, a new protocol in active development at
userinteractionsoverdifferentwirelessnetworks.
Google.WecomparedHTTP/1.1,SPDY[3],andQUIC
Motivated by such questions, we developed
Mahimahi1, a framework to record traffic from ap- toahypotheticaloptimalprotocolandfoundthatallthree
are suboptimal. We then used Mahimahi to understand
plications that use HTTP, and later replay recorded
the shortcomings of these multiplexing protocols. We
traffic under emulated network conditions. Mahimahi
foundthateachprotocolissuboptimalbecauseofthere-
works with any application that uses HTTP or HTTPS.
quest serialization caused by source-level object depen-
Application clients (Web browsers, video players, and
dencies present in today’s Web pages. Resolving each
1Mahimahiwaspreviouslyintroducedinademo[23]. dependencyrequiresanRTTbetweentheclientandori-
1
USENIX Association 2015 USENIX Annual Technical Conference 417

|     |     | Configuration   |     | HTTP/1.1 |     | SPDY     | QUIC-toy |     | Cumulus |     | Optimal |     |     |
| --- | --- | --------------- | --- | -------- | --- | -------- | -------- | --- | ------- | --- | ------- | --- | --- |
|     |     | 1Mbit/s,120ms   |     | 8.7,15.0 |     | 8.6,12.6 | 7.6,10.8 |     | 6.4,9.8 |     | 5.3,8.8 |     |     |
|     |     | 14Mbits/s,120ms |     | 4.3,6.0  |     | 3.9,5.6  | 3.8,5.4  |     | 2.4,3.6 |     | 1.8,2.9 |     |     |
|     |     | 25Mbits/s,120ms |     | 4.3,6.0  |     | 3.9,5.4  | 3.6,4.9  |     | 2.0,3.2 |     | 1.7,2.7 |     |     |
Table1:Median,75%ilepageloadtimes,inseconds,fortheAlexaUSTop500sitesfordifferentlinkratesandthe
same minimum RTT (120 ms). Comparing the median page load times, Cumulus is between 18-33% of the hypo-
theticaloptimal,outperformingthebestoftheotherschemes(shownineachrowinitalics)bybetween19%to80%
intheseconfigurations.Moreover,weshowlaterthatasRTTgrows,thegapfromoptimalforHTTP/1.1,SPDYand
QUICgrowsquickly,whereasCumulusisalotclosertooptimal.
gin Web servers; Mahimahi allowed us to pinpoint the 2.1 Record-and-replaytools
problembecausewewereabletoconductalargenumber
|     |     |     |     |     |     |     | The most | prominent | Web | page | record-and-replay |     | tools |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | ---- | ----------------- | --- | ----- |
ofemulationexperimentsunderdifferentnetworkcondi-
|     |     |     |     |     |     |     | are Google’s | web-page-replay |     |     | [11] and | Telerik’s | Fid- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------------- | --- | --- | -------- | --------- | ---- |
tionsquickly.
|     |     |     |     |     |     |     | dler [34]. | web-page-replay |     | uses | DNS indirection |     | to in- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | ---- | --------------- | --- | ------ |
We used these findings to develop Cumulus, a new terceptHTTPtrafficduringbothrecordandreplay,while
system to improve HTTP application performance, es- Fiddler adjusts the system-wide proxy settings in the
pecially on long-delay paths. Cumulus has two compo- Windows networking stack. With both tools, all HTTP
nents: the “Remote Proxy,” a headless browser that the requests from a browser are sent to a proxy server that
| user runs | on a | well-provisioned | cloud | server, | and | the |         |             |     |          |       |                 |     |
| --------- | ---- | ---------------- | ----- | ------- | --- | --- | ------- | ----------- | --- | -------- | ----- | --------------- | --- |
|           |      |                  |       |         |     |     | records | the request | and | forwards | it to | the correspond- |     |
“Local Proxy,” a transparent, caching HTTP proxy that ingoriginserver.Responsesalsopassthroughtheproxy
runsontheuser’scomputer.Thesetwocomponentsco- serverandarerecordedandsentbacktothebrowser.
| operate to | move | the resolution | of  | object | dependencies |     |      |              |      |     |               |     |            |
| ---------- | ---- | -------------- | --- | ------ | ------------ | --- | ---- | ------------ | ---- | --- | ------------- | --- | ---------- |
|            |      |                |     |        |              |     | Both | tools suffer | from | two | shortcomings. |     | First, be- |
closertooriginWebservers,reducingtheeffectiveRTT.
causetheyserveallHTTPresponsesfromasingleserver,
Mahimahi’sshellstructureallowedustoimplementCu-
neithertoolpreservesthemulti-servernatureofWebap-
mulus with ease by adapting RecordShell to implement plications. Consolidating HTTP resources onto a single
theLocalProxy.
serverduringreplayallowsbrowserstouseasinglecon-
To evaluate Cumulus, we used Mahimahi yet again, nectiontofetchallresources,whichisimpossiblewhen
thistimeonthesamelargenumberofnetworkconfigu- resources are on different servers. Mahimahi faithfully
rationsusedtounderstandHTTP/1.1,SPDY,andQUIC. emulates the multi-server nature of Web applications,
Our key result is that page load times with Cumulus leadingtomoreaccuratemeasurements( 4.1).
| do not degrade |     | dramatically | with | increasing | round-trip |     |         |       |       |        |                    | §   |          |
| -------------- | --- | ------------ | ---- | ---------- | ---------- | --- | ------- | ----- | ----- | ------ | ------------------ | --- | -------- |
|                |     |              |      |            |            |     | Second, | these | tools | do not | provide isolation: |     | the net- |
times (RTTs), unlike the other multiplexing protocols. work conditions that web-page-replay and Fiddler em-
| Some representative |     | results | are shown | in  | Table | 1. We |              |     |       |           |        |      |          |
| ------------------- | --- | ------- | --------- | --- | ----- | ----- | ------------ | --- | ----- | --------- | ------ | ---- | -------- |
|                     |     |         |           |     |       |       | ulate affect | all | other | processes | on the | host | machine. |
have also evaluated Cumulus on AT&T’s live cellular These include the link rate, link delay, and DNS in-
| network in       | Boston, | finding | that it     | outperforms | existing   |     |                |          |                      |        |         |            |        |
| ---------------- | ------- | ------- | ----------- | ----------- | ---------- | --- | -------------- | -------- | -------------------- | ------ | ------- | ---------- | ------ |
|                  |         |         |             |             |            |     | direction      | settings | for web-page-replay, |        |         | and the    | system |
| Web accelerators |         | such as | Opera Turbo | [1]         | and Chrome |     |                |          |                      |        |         |            |        |
|                  |         |         |             |             |            |     | proxy address, |          | specified            | in the | Windows | networking |        |
DataCompressionProxy[15]. stack, for Fiddler. During replay, this lack of isolation
Mahimahi has been used in other projects, including could lead to inaccurate measurements if cross traffic
an analysis of mobile app traffic patterns to compare fromotherprocessesreachesthereplayingproxyserver.
| single-path | and | multi-path | TCP [13], | and | an evaluation |     |          |              |      |           |          |     |          |
| ----------- | --- | ---------- | --------- | --- | ------------- | --- | -------- | ------------ | ---- | --------- | -------- | --- | -------- |
|             |     |            |           |     |               |     | The lack | of isolation | also | precludes | multiple |     | indepen- |
ofintelligentnetworkselectionschemes[12].Mahimahi dent instances of web-page-replay or Fiddler from run-
has also been used in Stanford’s graduate networking ning concurrently—a useful feature for expediting ex-
course [41] and at Mozilla to understand and improve periments, or for experimenting with different applica-
networking within browsers. Mahimahi and our experi- tionsconcurrently.Mahimahiovercomestheseproblems
mentaldataareavailableunderanopensourcelicenseat byusingLinux’snetworknamespaces[7].
http://mahimahi.mit.edu. Mahimahi has been Other record-and-replay tools such as Time-
queuedforinclusionwiththeDebiandistribution.
|           |     |      |     |     |     |     | lapse/Dolos     | [8]       | and       | WaRR         | [6] target   | reproducible |         |
| --------- | --- | ---- | --- | --- | --- | --- | --------------- | --------- | --------- | ------------ | ------------ | ------------ | ------- |
|           |     |      |     |     |     |     | application     | debugging |           | by capturing | program      | executions   |         |
|           |     |      |     |     |     |     | (including      | user      | input and | activity)    | and          | replaying    | them,   |
| 2 RELATED |     | WORK |     |     |     |     |                 |           |           |              |              |              |         |
|           |     |      |     |     |     |     | while providing |           | popular   | debugging    | abstractions |              | includ- |
This section describes prior work on Web record-and- ing breakpoints. These systems are complementary to
replaytoolsandnetworkemulationframeworks. Mahimahi; they can be run within ReplayShell, which
2
418  2015 USENIX Annual Technical Conference  USENIX Association

| ensures | that served | HTTP | content, | including |     | dynamic |     |     |     |     |     |     |     |
| ------- | ----------- | ---- | -------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
contentsuchasJavaScript,doesnotvaryduringreplay. (cid:5)(cid:19)(cid:24)(cid:15)(cid:22)(cid:19)(cid:15)(cid:24)(cid:1) (cid:9)(cid:15)(cid:13)(cid:20)(cid:22)(cid:14)(cid:15)(cid:14)(cid:1)
(cid:10)(cid:17)(cid:24)(cid:15)(cid:1)
2.2 EmulationFrameworks
|            |          |      |           |      |         |      |     | (cid:4)(cid:10)(cid:10)(cid:7)(cid:1)          | (cid:8)(cid:15)(cid:13)(cid:20)(cid:22)(cid:14)(cid:15)(cid:14)(cid:1) |     |                                                         |                                                         |                                                         |
| ---------- | -------- | ---- | --------- | ---- | ------- | ---- | --- | ---------------------------------------------- | ---------------------------------------------------------------------- | --- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
|            |          |      |           |      |         |      |     | (cid:7)(cid:22)(cid:20)(cid:28)(cid:29)(cid:1) | (cid:9)(cid:16)(cid:24)(cid:15)(cid:1)                                 |     | (cid:4)(cid:5)(cid:6)(cid:1)                            | (cid:4)(cid:5)(cid:6)(cid:1)                            | (cid:4)(cid:5)(cid:6)(cid:1)                            |
| Tools like | dummynet | [10] | and netem | [20] | emulate | net- |     |                                                |                                                                        |     |                                                         |                                                         |                                                         |
|            |          |      |           |      |         |      |     |                                                |                                                                        |     | (cid:2)(cid:21)(cid:12)(cid:13)(cid:16)(cid:15)(cid:1)  | (cid:2)(cid:21)(cid:12)(cid:13)(cid:16)(cid:15)(cid:1)  | (cid:2)(cid:21)(cid:12)(cid:13)(cid:16)(cid:15)(cid:1)  |
|            |          |      |           |      |         |      |     |                                                |                                                                        |     | (cid:10)(cid:15)(cid:22)(cid:26)(cid:15)(cid:22)(cid:1) | (cid:10)(cid:15)(cid:22)(cid:26)(cid:15)(cid:22)(cid:1) | (cid:10)(cid:15)(cid:22)(cid:26)(cid:15)(cid:22)(cid:1) |
workconditionsincludinglinkrate,one-waydelay,and
| stochastic | loss. | Mahimahi | uses its | own network |     | emula- |     |     |                                                                |     |     |                                                                |     |
| ---------- | ----- | -------- | -------- | ----------- | --- | ------ | --- | --- | -------------------------------------------------------------- | --- | --- | -------------------------------------------------------------- | --- |
|            |       |          |          |             |     |        |     |     | (cid:2)(cid:22)(cid:20)(cid:27)(cid:23)(cid:15)(cid:22)(cid:1) |     |     | (cid:3)(cid:22)(cid:20)(cid:27)(cid:23)(cid:15)(cid:22)(cid:1) |     |
tionshells,LinkShellandDelayShell.Unlikedummynet
and netem, LinkShell can emulate variable-rate cellu- (cid:7)(cid:22)(cid:16)(cid:26)(cid:12)(cid:24)(cid:15)(cid:1)(cid:6)(cid:15)(cid:24)(cid:27)(cid:20)(cid:22)(cid:17)(cid:1)(cid:6)(cid:12)(cid:18)(cid:15)(cid:23)(cid:21)(cid:12)(cid:13)(cid:15)(cid:1) (cid:8)(cid:22)(cid:17)(cid:26)(cid:12)(cid:24)(cid:15)(cid:1)(cid:7)(cid:15)(cid:24)(cid:27)(cid:20)(cid:22)(cid:18)(cid:1)(cid:7)(cid:12)(cid:19)(cid:15)(cid:23)(cid:21)(cid:12)(cid:13)(cid:15)(cid:1)
lar links, in addition to static link rates, because it runs (cid:11)(cid:23)(cid:15)(cid:22)(cid:1)(cid:3)(cid:20)(cid:18)(cid:21)(cid:25)(cid:24)(cid:15)(cid:22)(cid:1) (cid:11)(cid:23)(cid:15)(cid:22)(cid:1)(cid:4)(cid:20)(cid:19)(cid:21)(cid:25)(cid:24)(cid:15)(cid:22)(cid:1)
overpacket-deliverytraces.Mahimahialsoallowsusers
|             |     |            |            |          |     |         |     | (a)RecordShell |     |     | (b)ReplayShell |     |     |
| ----------- | --- | ---------- | ---------- | -------- | --- | ------- | --- | -------------- | --- | --- | -------------- | --- | --- |
| to evaluate | new | in-network | algorithms | (instead |     | of Drop |     |                |     |     |                |     |     |
Figure1:RecordShellhasatransparentproxyforHTTP
TailFIFO)bymodifyingthesourcecodeofLinkShell.A
traffic.ReplayShellhandlesallHTTPtrafficinsideapri-
similarevaluationusingweb-page-replaywouldrequire
developing anew kernel modulefor dummynet, amore vate network namespace. Arrows indicate the direction
ofHTTPRequestandResponsetraffic.
complicatedtask.
Mahimahiisgeneralenoughtorecordandreplayany
|                    |              |             |       |           |        |          | plication  | inside      | DelayShell |     | inside LinkShell |     | inside Re- |
| ------------------ | ------------ | ----------- | ----- | --------- | ------ | -------- | ---------- | ----------- | ---------- | --- | ---------------- | --- | ---------- |
| HTTP client-server |              | application | under | emulated  |        | condi-   |            |             |            |     |                  |     |            |
| tions. It          | is, however, | limited     | in    | that it   | only   | emulates | playShell. |             |            |     |                  |     |            |
| one physical       | client       | connected   | to an | arbitrary | number | of       |            |             |            |     |                  |     |            |
|                    |              |             |       |           |        |          | 3.1        | RecordShell |            |     |                  |     |            |
servers.Mahimahisupportsasinglesharedlinkfromthe
clienttoallservers,aswellasmulti-homedclients( 5.5), RecordShell(Figure1a)recordsHTTPdataandstoresit
|          |                |     |                      |     |     | §         | ondiskinastructuredformatforsubsequentreplay.On |     |     |     |     |     |     |
| -------- | -------------- | --- | -------------------- | --- | --- | --------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
| allowing | the evaluation |     | of multipath-capable |     |     | transport |                                                 |     |     |     |     |     |     |
startup,RecordShellspawnsaman-in-the-middleproxy
| protocols | such as | MPTCP | [25]. Mahimahi |     | cannot | emu- |     |          |         |          |             |     |          |
| --------- | ------- | ----- | -------------- | --- | ------ | ---- | --- | -------- | ------- | -------- | ----------- | --- | -------- |
|           |         |       |                |     |        |      | on  | the host | machine | to store | and forward |     | all HTTP |
latearbitrarynetworktopologiessuchastransit-stub[9];
|               |              |     |           |             |     |       | traffic | both | to and | from an | application | running | within |
| ------------- | ------------ | --- | --------- | ----------- | --- | ----- | ------- | ---- | ------ | ------- | ----------- | ------- | ------ |
| for emulating | applications |     | over such | topologies, |     | tools |         |      |        |         |             |         |        |
likeMininet[21]aremoresuitable. RecordShell.Tooperatetransparently,RecordShelladds
aniptablerulethatforwardsallTCPtrafficfromwithin
RecordShelltotheman-in-the-middleproxy.
3 MAHIMAHI
|     |     |     |     |     |     |     |     | When an | application | inside | RecordShell |     | attempts to |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ------ | ----------- | --- | ----------- |
Mahimahi is structured as a set of four UNIX shells, connecttoaserver,itconnectstotheproxyinstead.The
allowing users to run unmodified client binaries within proxy then establishes a TCP connection with the ap-
each shell. Each shell creates a new network names- plication,usestheSO ORIGINAL DSTsocketoptionto
paceforitselfpriortolaunchingtheshell.Quotingfrom determine the server’s address for the connection, and
the man page, “a network namespace is logically an- connects to the server on the application’s behalf. An
other copy of the network stack, with its own routes, HTTP parser running at the proxy captures traffic pass-
firewallrules,andnetworkdevices”[7].Aseparatenet- ing through it to parse HTTP requests and responses
work namespace minimizes disruption to the host ma- fromTCPsegments.OnceanHTTPrequestanditscor-
chineduringrecording,preventsaccidentaldownloadof responding response have both been parsed, the proxy
resources over the Internet during replay, and ensures writes them to disk, associating the request with the re-
that the host machine is isolated from all network con- sponse.Attheendofarecordsession,arecordeddirec-
figurationchangesthatarerequiredtoevaluateanappli- toryconsistsofasetoffiles,oneforeachHTTPrequest-
| cation. |     |     |     |     |     |     | responsepairseenduringthatsession. |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
RecordShell ( 3.1) records all HTTP traffic for sub- SSL traffic is handled similarly by splitting the SSL
§
sequent replay. ReplayShell ( 3.2) replays previously connection and establishing two separate SSL connec-
§
recorded HTTP content. DelayShell ( 3.3) delays all tions:onebetweentheproxyandtheapplicationandan-
§
packets originating from the shell by a user-specified other between the proxy and the server. The proxy can
amountandLinkShell( 3.4)emulatesanetworklinkby establishasecureconnectionwiththeapplicationintwo
|            |         |           | §    |                |     |         | ways. | In the | first approach, |     | RecordShell’s | proxy | uses a |
| ---------- | ------- | --------- | ---- | -------------- | --- | ------- | ----- | ------ | --------------- | --- | ------------- | ----- | ------ |
| delivering | packets | according | to a | user-specified |     | packet- |       |        |                 |     |               |       |        |
deliverytrace.AllcomponentsofMahimahirunonasin- newRootCA,inthesamewayFiddlerdoes[35].Clients
gle physical machine (which we call the host machine) mustmanuallytrustthisCAonceandindividualcertifi-
andcanbearbitrarilycomposedwitheachother.Forex- catesaresignedbythisRootCA.
ample,toreplayrecordedcontentoveracellularnetwork AnotherapproachisforRecordShell’sproxytousea
witha10msminimumRTT,onewouldrunaclientap- self-signed certificate. This approach may trigger warn-
3
USENIX Association   2015 USENIX Annual Technical Conference  419

| ings within | applications |     | that | only | accept | certificates |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | ---- | ---- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
signedbyanyoneofalistoftrustedCertificateAuthor-
| ities (CAs). | Most | modern | browsers |     | allow | users to dis- |     |     |     |     |     |     |     |
| ------------ | ---- | ------ | -------- | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- |
ablethesewarnings.Certainapplications,suchasmobile
phoneemulators,donotallowthesewarningstobedis-
abled;thefirstapproachhandlestheseapplications[31].
3.2 ReplayShell
| ReplayShell | (Figure |        | 1b) also | runs on | the          | test machine |     |     |     |     |     |     |     |
| ----------- | ------- | ------ | -------- | ------- | ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
| and mirrors | the     | server | side     | of Web  | applications | using        |     |     |     |     |     |     |     |
contentrecordedbyRecordShell.ReplayShellaccurately
| emulates | the multi-server |     | nature | of  | most Web | applica- |     |     |     |     |     |     |     |
| -------- | ---------------- | --- | ------ | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Figure2:LinkShellsupportslivegraphingofnetworkus-
tions today by spawning an Apache 2.2.22 Web server age,comparingthelinkcapacityoftheinputtraces(red
foreachdistinctIP/portpairseenwhilerecording.Each shading) to the amount of data a client application at-
server handles HTTPS traffic using Apache’s mod ssl temptstotransmit(blueline).
| module          | and may | be             | configured | to speak    | HTTP/1.1    | or          |               |          |     |            |                 |     |         |
| --------------- | ------- | -------------- | ---------- | ----------- | ----------- | ----------- | ------------- | -------- | --- | ---------- | --------------- | --- | ------- |
| SPDY(usingmod   |         | spdy).         |            |             |             |             |               |          |     |            |                 |     |         |
| To operate      |         | transparently, |            | ReplayShell |             | binds each  | 3.4 LinkShell |          |     |            |                 |     |         |
| Apache          | server  | to the         | same IP    | address     | and         | port number |               |          |     |            |                 |     |         |
|                 |         |                |            |             |             |             | LinkShell     | emulates | a   | link using | packet-delivery |     | traces. |
| as its recorded |         | counterpart.   |            | To do so,   | ReplayShell | cre-        |               |          |     |            |                 |     |         |
Itemulatesbothtime-varyinglinkssuchascellularlinks
atesaseparatedummy(virtual)interfaceforeachdistinct
serverIP.TheseinterfacescanhavearbitraryIPsbecause and links with a fixed link rate. When a packet arrives
|     |     |     |     |     |     |     | into the link, | it  | is directly | placed | into either | the | uplink |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | ------ | ----------- | --- | ------ |
theyareinaseparatenetworknamespace.
ordownlinkpacketqueue.LinkShellistrace-drivenand
AllclientrequestsarehandledbyoneofReplayShell’s
|          |          |          |        |           |              |            | releases packets |                 | from | each queue | based     | on the | corre- |
| -------- | -------- | -------- | ------ | --------- | ------------ | ---------- | ---------------- | --------------- | ---- | ---------- | --------- | ------ | ------ |
| servers, | each     | of which | can    | read all  | of the       | previously |                  |                 |      |            |           |        |        |
|          |          |          |        |           |              |            | sponding         | packet-delivery |      | trace.     | Each line | in the | trace  |
| recorded | content. | Each     | server | redirects | all incoming | re-        |                  |                 |      |            |           |        |        |
quests to a CGI script using Apache’s mod rewrite is a packet-delivery opportunity: the time at which an
|     |     |     |     |     |     |     | MTU-sized | packet | will | be delivered | in the | emulation.2 |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---- | ------------ | ------ | ----------- | --- |
module.TheCGIscriptoneachservercompareseachin-
|     |     |     |     |     |     |     | Accounting | is done | at  | the byte-level, | and | each delivery |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --- | --------------- | --- | ------------- | --- |
comingHTTPrequesttothesetofallrecordedrequest-
|                   |       |           |            |          |          |            | opportunity    | represents |         | the ability | to deliver | 1500       | bytes. |
| ----------------- | ----- | --------- | ---------- | -------- | -------- | ---------- | -------------- | ---------- | ------- | ----------- | ---------- | ---------- | ------ |
| response          | pairs | to locate | a matching |          | request  | and return |                |            |         |             |            |            |        |
|                   |       |           |            |          |          |            | Thus, a single |            | line in | the trace   | file can   | correspond | to     |
| the corresponding |       | response. |            | Incoming | requests | may be     |                |            |         |             |            |            |        |
influencedbylocalstatepresentintheclientapplication thedeliveryofseveralpacketswhosesizessumto1500
bytes.Deliveryopportunitiesarewastedifbytesareun-
(e.g.time-sensitivequerystringparameters)andmaynot
availableattheinstantoftheopportunity.
exactlymatchanyrecordedrequest.Wehandlesuchre-
questsusingamatchingheuristicthatenforcesthatsome LinkShell supports live graphing of network usage
partsoftherequestmustmatchexactly,whiletolerating andper-packetqueuingdelay,givingnear-instantaneous
somedegreeofimperfectioninotherparts. feedback on the performance of applications and net-
We expect the Host and User-Agent header fields, work protocols. Uplink and downlink capacity are cal-
along with the requested resource (without the query culatedusingtheinputpacket-deliverytraces,whilenet-
string), to exactly match the corresponding values in workusage,ineachdirection,isbasedontheamountof
somestoredrequest.Ifmultiplestoredrequestsmatchon data that a client application attempts to transmit or re-
theseproperties,thealgorithmselectstherequestwhose ceive.Per-packetqueuingdelayiscomputedasthetime
query string has the maximal common substring to the each packet remains in LinkShell’s uplink or downlink
| incomingquerystring. |     |     |     |     |     |     | queues. |               |     |              |         |       |      |
| -------------------- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ------------ | ------- | ----- | ---- |
|                      |     |     |     |     |     |     | Figure  | 2 illustrates |     | the downlink | network | usage | of a |
3.3 DelayShell
DelayShell emulates a link with a fixed minimum one- singleWebpageloadofhttp://www.cnn.com,us-
ingGoogleChromeoveranemulatedVerizonLTEcellu-
| way delay. | All | packets | sent | to and from | an  | application |     |     |     |     |     |     |     |
| ---------- | --- | ------- | ---- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
running inside DelayShell are stored in a packet queue. larnetworkwithaminimumRTTof100ms.Asshown,
Webserverstrytoexceedthelinkcapacityataround9.3
Aseparatequeueismaintainedforpacketstraversingthe
secondsintothetrace.
| link in  | each direction.    |       | When  | a packet | arrives, | it is as-      |     |     |     |     |     |     |     |
| -------- | ------------------ | ----- | ----- | -------- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| signed a | delivery           | time, | which | is the   | sum      | of its arrival |     |     |     |     |     |     |     |
| time and | the user-specified |       |       | one-way  | delay.   | Packets are    |     |     |     |     |     |     |     |
2Forexample,alinkthatcanpassoneMTU-sizedpacketpermil-
releasedfromthequeueattheirdeliverytime.Thistech-
lisecond(12Mbits/s)canberepresentedbyafilethatcontainsjust“1”
niqueenforcesafixeddelayonaper-packetbasis. (LinkShellrepeatsthetracefilewhenitreachestheend).
4
420  2015 USENIX Annual Technical Conference  USENIX Association

| 4 NOVELTY                                         |            |       |     |          |     |            |     | 1    |     |     |     |     |     |
| ------------------------------------------------- | ---------- | ----- | --- | -------- | --- | ---------- | --- | ---- | --- | --- | --- | --- | --- |
| Mahimahi                                          | introduces | three | new | features | in  | comparison |     |      |     |     |     |     |     |
| toexistingrecord-and-replaytools.Wedescribeeachof |            |       |     |          |     |            |     | 0.75 |     |     |     |     |     |
noitroporP evitalumuC
theseingreaterdetailbelow.
0.5
4.1 Multi-serveremulationforgreateraccuracy
| A key component |     | of ReplayShell |     | is that | it emulates | the |     |     |     |     |     |     |     |
| --------------- | --- | -------------- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
0.25
| multi-server | nature | of Web | applications. |     | As  | discussed |     |     |     |     |     |     |     |
| ------------ | ------ | ------ | ------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
ReplayShell, multi-server
in 3,ReplayShellcreatesanetworknamespacecontain- ReplayShell, single-server
web-page-replay
| §   |     |     |     |     |     |     |     | 0   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ing anApacheserverforeachdistinctserverencountered 0 30 60 90 120 150
in a recorded directory. We show through three experi- Absolute Value of Relative Percent Error
|            |           |      |              |     |        |             | Figure 3:           | Preserving | a    | Web  | page’s multi-server |           | nature |
| ---------- | --------- | ---- | ------------ | --- | ------ | ----------- | ------------------- | ---------- | ---- | ---- | ------------------- | --------- | ------ |
| ments that | emulating | this | multi-server |     | nature | is critical |                     |            |      |      |                     |           |        |
|            |           |      |              |     |        |             | yields measurements |            | that | more | closely             | resembles | mea-   |
totheaccuratemeasurementofWebpageloadtimes.
surementsontheInternet.
Alargenumberofwebsitestodayaremulti-server.We
measurethenumberofphysicalserversusedbyeachsite 30ms 120ms 300ms
inthetheAlexaUSTop500[5].Wefindthatthemedian 1Mbit/s 1.6%,27.6% 1.7%,10.8% 2.1%,9.7%
|     |     |     |     |     |     |     | 14Mbits/s | 19.3%,127.3% |     |     | 6.2%,42.4% | 3.3%,20.3% |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | --- | ---------- | ---------- | --- |
numberofserversis20,the95%ileis51,andthe99%ile
|     |     |     |     |     |     |     | 25Mbits/s | 21.4%,111.6% |     |     | 6.3%,51.8% | 2.6%,15.0% |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | --- | ---------- | ---------- | --- |
is58.Only9ofthe500Webpages(1.8%)weconsider
useasingleserver. Table2:Medianand95%iledifferenceinpageloadtime
Next, we illustrate the importance of preserving the withoutmulti-serveremulation.
| multi-server | nature | of Web | applications |     | by  | comparing |     |     |     |     |     |     |     |
| ------------ | ------ | ------ | ------------ | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Finally,werunmoreexhaustiveexperimentstoshow
| measurements        | collected |      | using         | ReplayShell |        | and web-     |            |        |              |           |         |             |            |
| ------------------- | --------- | ---- | ------------- | ----------- | ------ | ------------ | ---------- | ------ | ------------ | --------- | ------- | ----------- | ---------- |
|                     |           |      |               |             |        |              | the effect | that   | multi-server | emulation |         | has on      | Web page   |
| page-replay         | to real   | page | load times    | on          | the    | Internet. To |            |        |              |           |         |             |            |
|                     |           |      |               |             |        |              | load times | across | different    | network   |         | conditions. | Using      |
| obtain measurements |           | on   | the Internet, |             | we use | Selenium     |            |        |              |           |         |             |            |
|                     |           |      |               |             |        |              | an Amazon  | EC2    | m3.large     | instance  | located |             | in the US- |
toautomateGoogleChromeloading20Webpagesfrom
|     |     |     |     |     |     |     | east-1a | region | and running | Ubuntu | 13.10, | we  | measure |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ----------- | ------ | ------ | --- | ------- |
theAlexaUSTop500,25timeseach,insideaLinkShell
pageloadtimesforeachrecordedpageintheAlexaUS
| of 5 Mbits/s | and | a DelayShell |     | with a | minimum | RTT of |         |      |        |             |         |     |         |
| ------------ | --- | ------------ | --- | ------ | ------- | ------ | ------- | ---- | ------ | ----------- | ------- | --- | ------- |
|              |     |              |     |        |         |        | Top 500 | when | loaded | with Google | Chrome. |     | We con- |
100ms.WechoseaminimumRTTof100mstoequalize
|     |     |     |     |     |     |     | sider 9 different |     | configurations: |     | link rates | in  | 1,14,25 |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------------- | --- | ---------- | --- | ------- |
delaystoWebserverscontactedwhileloadingeachWeb
|            |        |             |     |        |        |         |           |          |               |            |       |                  | { }       |
| ---------- | ------ | ----------- | --- | ------ | ------ | ------- | --------- | -------- | ------------- | ---------- | ----- | ---------------- | --------- |
|            |        |             |     |        |        |         | Mbits/s   | and RTTs | in            | 30,120,300 | ms.   | We               | load each |
| page.3 For | a fair | comparison, | we  | record | copies | of each |           |          | {             |            | }     |                  |           |
|            |        |             |     |        |        |         | page over | each     | configuration |            | using | both ReplayShell |           |
WebpagewithRecordShellandweb-page-replayimme-
andthemodifiedversionofReplayShellusedabovethat
| diately following |     | the completion |            | of these | Internet    | mea-        |            |        |              |            |            |      |            |
| ----------------- | --- | -------------- | ---------- | -------- | ----------- | ----------- | ---------- | ------ | ------------ | ---------- | ---------- | ---- | ---------- |
|                   |     |                |            |          |             |             | eliminates | the    | multi-server | nature     | altogether |      | by setting |
| surements;        | Web | content        | can change |          | frequently, | which       |            |        |              |            |            |      |            |
|                   |     |                |            |          |             |             | up one     | Apache | server       | to respond | to all     | HTTP | requests   |
| can significantly |     | affect         | page load  | time.    | We          | then replay |            |        |              |            |            |      |            |
andresolvingallDNSqueriestothatserveralone.
| each recorded | Web | page | 25 times | using | ReplayShell, | a   |       |         |            |     |            |            |     |
| ------------- | --- | ---- | -------- | ----- | ------------ | --- | ----- | ------- | ---------- | --- | ---------- | ---------- | --- |
|               |     |      |          |       |              |     | Table | 2 shows | the median |     | and 95%ile | difference | in  |
modifiedversionofReplayShellthatservesallresources
pageloadtimewhenmulti-servernatureisnotpreserved,
| from a     | single server, | and       | web-page-replay. |      |        | With Re-  |          |          |              |       |                |               |          |
| ---------- | -------------- | --------- | ---------------- | ---- | ------ | --------- | -------- | -------- | ------------ | ----- | -------------- | ------------- | -------- |
|            |                |           |                  |      |        |           | compared | to when  | multi-server |       | nature         | is preserved. | Al-      |
| playShell, | we perform     | each      | page             | load | inside | LinkShell |          |          |              |       |                |               |          |
|            |                |           |                  |      |        |           | though   | the page | load         | times | are comparable |               | over a 1 |
| with a 5   | Mbits/s        | trace and | DelayShell       |      | with   | a minimum |          |          |              |       |                |               |          |
Mbit/slink,thelackofmulti-serveremulationyieldssig-
| RTT of | 100 ms, | as described | above. |     | We emulate | these |     |     |     |     |     |     |     |
| ------ | ------- | ------------ | ------ | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
nificantlyworseperformanceathigherlinkrates.
samenetworkconditionswithweb-page-replay.
| We define | the | error, per | site, | as the | absolute | value of | 4.2 Isolation |     |     |     |     |     |     |
| --------- | --- | ---------- | ----- | ------ | -------- | -------- | ------------- | --- | --- | --- | --- | --- | --- |
the percent difference between mean page load times By creating a new network namespace for each shell,
| (over 25 | runs) within | an  | emulation | environment |     | and on |     |     |     |     |     |     |     |
| -------- | ------------ | --- | --------- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Mahimahieliminatesmuchexperimentalvariabilitythat
the Internet. As shown in Figure 3, ReplayShell with results from interfering cross traffic during an experi-
multi-serveremulationyieldspageloadtimesthatmost ment. Each namespace is separate from the host ma-
accuratelyresemblepageloadtimescollectedontheIn- chine’s default namespace and every other namespace
ternet. The median error is 12.4%, compared to 36.7% and thus, processes run inside the namespace of a
| and 20.5% | with web-page-replay |     |     | and | single-server | Re- |          |      |                |     |          |      |            |
| --------- | -------------------- | --- | --- | --- | ------------- | --- | -------- | ---- | -------------- | --- | -------- | ---- | ---------- |
|           |                      |     |     |     |               |     | Mahimahi | tool | are completely |     | isolated | from | those run- |
playShell,respectively.4
|     |     |     |     |     |     |     | ning directly | on      | the host | or in | other      | namespaces. | As a     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | -------- | ----- | ---------- | ----------- | -------- |
|     |     |     |     |     |     |     | result, host  | machine | traffic  | does  | not affect | the         | measure- |
3The20sitesusedhereareallhostedbyCDNsincloseproximity
|     |     |     |     |     |     |     | ments reported |     | by Mahimahi. |     | Similarly, | network | emu- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | ---------- | ------- | ---- |
withpingtimesoflessthan5ms.
|     |     |     |     |     |     |     | lation done | by  | Mahimahi’s | tools | does | not affect | traffic |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | ----- | ---- | ---------- | ------- |
4Wearenotcertainwhysingle-serverReplayShellissomuchmore
accuratethanweb-page-replay. outside of Mahimahi’s network namespaces. This prop-
5
USENIX Association   2015 USENIX Annual Technical Conference  421

Machine1 Machine2 load the 500 sites inside DelayShell, with 0 ms fixed
CNBC 7584ms+-120ms 7612ms+-111ms per-packetdelay,insideReplayShell.Separately,weload
| wikiHow |     | 4804ms+-37ms |     | 4800ms+-37ms |     |     |     |     |     |     |     |     |     |
| ------- | --- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the500sitesinsideLinkShell,with1000Mbits/suplink
Table3:Meanandstandarddeviationforpageloadtimes anddownlinktraces,insideReplayShell.5 Eachofthese
acrosstwosimilarlyconfiguredmachines.
|     |     |     |     |     |     |     | experiments | was | performed | on the | same | Amazon | EC2 |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ------ | ---- | ------ | --- |
m3.largeinstanceconfiguredwithUbuntu13.10andlo-
1
|     |     |     |     |     |     |     | catedinthe | US-east-1aregion. |     | Wefindthatthemedian |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | --- | ------------------- | --- | --- | --- |
per-siteerrorswithDelayShellandLinkShell,relativeto
|     | noitroporP evitalumuC 0.75 |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ReplayShellalone,are0.33%and0.31%,respectively.
|     | 0.5 |     |     |     |     |     | 4.3 Composabilityandextensibility |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
Unmodifiedapplicationclientscanberunwithinanyof
|     | 0.25 |     |     |     |     |     | Mahimahi’s | shells. | For instance, | as  | described | in  | 5.5, a |
| --- | ---- | --- | --- | --- | --- | --- | ---------- | ------- | ------------- | --- | --------- | --- | ------ |
§
DelayShell 0 ms mobile device emulator can be run within Mahimahi to
LinkShell 1000 Mbits/s
|     | 0   |     |     |     |     |     | measuremobileappperformance.Similarly,tomeasure |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     | 0   |     | 1   | 2   | 3   |     |                                                 |     |     |     |     |     |     |
Relative Percent Error newperformancemetricssuchasthespeedindex,virtual
Figure4:DelayShellandLinkShellhaveanegligibleef-
|                                   |     |     |     |     |     |     | machinescanberunwithinMahimahi’sshells( |        |           |     |         |          | 5.4). |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --------------------------------------- | ------ | --------- | --- | ------- | -------- | ----- |
| fectonpageloadtimesinReplayShell. |     |     |     |     |     |     |                                         |        |           |     |         |          | §     |
|                                   |     |     |     |     |     |     | The default                             | replay | algorithm | is  | but one | instance | of a  |
ertyof Mahimahi,alongwith thefactthat itsshellscan server-side HTTP matching algorithm. Mahimahi’s re-
be arbitrarily nested, enables many different configura- play semantics can be easily extended to support the
tions to be simultaneously tested on a host machine, in server-side logic of many other applications and multi-
completeisolationfromoneanother. plexingprotocols;forexample,in 5.1.1,weextendRe-
§
Usingdistinctnetworknamespacesforeachshellalso playShell to use QUIC Web servers rather than default
enablesMahimahitoproducereproducibleresultswhile ApacheWebservers.Ithasalsobeenextendedtohandle
imposinglowoverheadoncollectedmeasurements. record-and-replayforYouTubevideos( 5.5).
§
|                  |     |     |          |                     |     |     | In addition | to DelayShell |     | and LinkShell, |     | whichemu- |     |
| ---------------- | --- | --- | -------- | ------------------- | --- | --- | ----------- | ------------- | --- | -------------- | --- | --------- | --- |
| Reproducibility: |     | To  | evaluate | the reproducibility |     | of  |             |               |     |                |     |           |     |
Mahimahi’s measurements, we perform repeated exper- late different minimum RTTs and link rates, Mahimahi
canbeextendedtosupportothernetworkcharacteristics.
| iments | on the same | host | machines | and | across | different |     |     |     |     |     |     |     |
| ------ | ----------- | ---- | -------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
host machines with similar hardware specifications. We For example, to emulate different levels of stochastic
packetloss,wecreatedLossShell[24],whichprobabilis-
| choose | two sites | from | the Alexa | US  | Top 500 | for this |     |     |     |     |     |     |     |
| ------ | --------- | ---- | --------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
ticallydropspacketsstoredinLinkShell’supstreamand
| experiment, | http://www.cnbc.com/ |     |     |     | and | http: |     |     |     |     |     |     |     |
| ----------- | -------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
//www.wikihow.com/,astheyareareatthemedian downstream queues. Similarly, Mahimahi can be mod-
|     |     |     |     |     |     |     | ified to | evaluate | in-network | algorithms |     | such | as queu- |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---------- | ---------- | --- | ---- | -------- |
and95%ilesitesizes(1.2MBand5.5MB,respectively).
WeusetwodifferentAmazonEC2m3.largeinstances, ingdisciplines.Bydefault,LinkShellimplementsaDrop
|     |     |     |     |     |     |     | Tail FIFO | queue, | but we | have extended |     | it to implement |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------ | ------------- | --- | --------------- | --- |
eachintheUS-east-1aregionandrunningUbuntu13.10.
CoDel,anactivequeuemanagementscheme[32].
| On each | machine, | we  | load | the CNBC | and | wikiHow |     |     |     |     |     |     |     |
| ------- | -------- | --- | ---- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Webpages100timeseachinsideReplayShell,overa14 Mahimahicouldalsobeusedtoreplayrecordedcon-
tenttoadifferentphysicalmachine.Considerascenario
| Mbits/s | link with | a minimum |     | RTT of | 120 ms. | Table 3 |     |     |     |     |     |     |     |
| ------- | --------- | --------- | --- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
showsasummaryofthedistributionofpageloadtimes wheretheapplicationtobeevaluatedisonlyavailableon
fromthese experiments.Meanpage loadtimesforeach Machine M, and a separate Linux Machine, A, is avail-
|          |           |      |       |            |     |          | able. An | EthShell | could | ferry packets | from | an  | Ethernet |
| -------- | --------- | ---- | ----- | ---------- | --- | -------- | -------- | -------- | ----- | ------------- | ---- | --- | -------- |
| site are | less than | 0.5% | apart | across the | two | machines |          |          |       |               |      |     |          |
suggesting that Mahimahi produces comparable results interface between M and A to a virtual network inter-
|     |     |     |     |     |     |     | face on | A. Analogously, |     | a UsbShell | could | ferry | pack- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | ---------- | ----- | ----- | ----- |
acrossdifferenthostmachines.Similarly,standarddevi-
ationsareallwithin1.6%oftheircorrespondingmeans, ets between an Ethernet-over-USB interface connected
implyingthatMahimahiproducesconsistentresultsona to a phone and a virtual interface on A. UsbShell could
|     |     |     |     |     |     |     | be used | to run performance |     | regression |     | tests on | actual |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------------ | --- | ---------- | --- | -------- | ------ |
singlehostmachine.
phonesratherthanemulators.Neitherofthesehasbeen
| Fidelity: | Mahimahi’s |     | shells | impose | low overhead | on  |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ------ | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
developedyet,butMahimahi’sdesignallowstheseshells
| collected | measurements, |     | even | when | they are | nested |     |     |     |     |     |     |     |
| --------- | ------------- | --- | ---- | ---- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
tobenestedinsideanyofMahimahi’sexistingshells.For
withinoneanother,leadingtohighfidelityintheresults.
|     |     |     |     |     |     |     | instance, | to test a | mobile | phone’s | browser | over | an LTE |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------ | ------- | ------- | ---- | ------ |
WeillustratethispropertyinFigure4,whichshowsthe
linkwitha100msRTT,wewouldnestUsbShellinside
overheadDelayShellandLinkShellimposeonpageload
DelayShellinsideLinkShellinsideReplayShell.
timemeasurements.Wefirstloadourrecordedcopiesof
| the Alexa | US  | Top 500 | sites | inside ReplayShell, |     | with- |     |     |     |     |     |     |     |
| --------- | --- | ------- | ----- | ------------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
5Wechose1000Mbits/stoensurethatlinkcapacitywasnotalim-
out LinkShell or DelayShell. For comparison, we then itingfactorinpageloadtime.
6
422  2015 USENIX Annual Technical Conference  USENIX Association

5 CASE STUDIES first byte of the first HTTP response is received by the
client,ignoringprocessingtimeattheserver.
5.1 UnderstandingWebPerformance
The second term represents the minimum time to
We use Mahimahi to evaluate Web page load times un-
transferallbytesbelongingtotheWebpageoverafixed
der three multiplexing protocols: HTTP/1.1, SPDY [3],
capacitylink.Wecalculatethesitesizebycountingthe
and QUIC [30], a protocol currently in development at
total number of bytes delivered over the emulated link
Google.Toputthesemeasurementsincontext,wecom-
fromtheWebserverstothebrowserbetweenthenaviga-
pareeachprotocolwithanoptimalprotocolforeachnet-
tionStartandloadEventEndevents.
workconfiguration.
The third term represents the time for the browser to
Toautomatethepageloadprocessandmeasurepage
processalltheHTTPresponsesandrendertheWebpage
load times, we use Selenium, a widely used browser-
(using the definition of “loaded” above). We measure
automation tool, along with Chrome Driver version 2.8
this as the page load time in ReplayShell alone without
andtheWebDriverAPI[38].Wemeasurepageloadtime
networkemulation,emulatinganinfinite-capacity,zero-
by calculating the time elapsed between thenavigation-
delaylink.
StartandloadEventEndevents[38].
In all evaluations, traffic originates from the Web 5.1.3 Canonicalnetworkresults
browser alone. We emulate link rates and minimum
We evaluate each protocol on 110 configurations: link
RTTs ( 3), but do not emulate competing cross traffic. rates in 0.2,0.3,0.6,1,1.7,2.9,5,8.5,14,25 Mbits/s
§
Foreachnetworkconfiguration,weemulateabuffersize { }
and RTTs between 0 ms and 300 ms in steps of 30 ms.
of1bandwidth-delayproductandevaluateallsitesinthe
These link rates and RTTs cover the majority of global
AlexaUSTop500.
network conditions reported by Akamai [4]. We also
5.1.1 Setup perform evaluations over cellular networks using modi-
fied versions of the Verizon and AT&T traces collected
HTTP/1.1: We evaluate HTTP/1.1 using ReplayShell
in [40]. For each network configuration, we compare
runningunmodifiedApache2.2.22.
HTTP/1.1, SPDY, and QUIC (and in the next subsec-
SPDY: ToevaluateSPDY,wecreateSPDYShell,which tion,Cumulus)withtheoptimalpageloadtimesdefined
enables the mod spdy extension on all Apache servers above.
within ReplayShell. The SPDY configuration evaluated Figure 5 shows the distributions of page load times
heredoesnotincludeserverpushbecausethepushpol- with each protocol for six of these configurations: 1
icy is specific to each website and is hard to infer auto- Mbit/sand25Mbits/s,withRTTsof30ms,120ms,and
matically.Ifpushpolicieswereknown,however,theCGI 300ms.WefindthatthegapfromoptimalforHTTP/1.1,
scriptwithinReplayShell’sserverscouldbemodifiedto SPDY,andQUICgrowsquicklywiththeRTT,andgrows
reflectthem. withthelinkrate(althoughnotasquickly).Forexample,
on a 1 Mbit/s link with a minimum RTT of 30 ms, the
QUIC: QUIC inherits several SPDY features, such as
median page load time for SPDY is 1.08 worse than
multiplexing streams onto a single transport-protocol ×
optimal. When the minimum RTT increases to 120 ms,
connection and stream priorities. By using UDP and its
themedianSPDYpageloadtimeis1.63 worsethanop-
ownsecurityinsteadofTCPandTLS,QUICovercomes ×
timal,worseningto2.02 worsethanoptimalwhenthe
twodrawbacksofSPDY:head-of-lineblockingbetween ×
minimumRTTrisesto300ms.ForthisRTT,increasing
streamsduetolostpacketsandthethree-wayhandshake
thelinkratefrom1Mbit/sto25Mbits/sdegradesmedian
requiredtoestablishasecureconnection.
SPDYperformanceto4.93 worsethanoptimal.
Unlike SPDY, Apache currently has no extensions ×
for QUIC. We create QUICShell by replacing Apache 5.1.4 Understandingsuboptimality
withinReplayShellwithanadaptedversionoftheQUIC In addition to quantifying the extent of suboptimality
toy server [29] from the Chromium project (commit of multiplexing protocols for the Web, the results pre-
5bb5b95fromMay,2015,availableathttps://goo. sentedinthiscasestudycorroboratethequalitativefind-
gl/Jdr8hi). We modify the toy server, which origi- ingsofmanypreviousmeasurementstudies[26,37,39].
nallysearchedforexactURLmatches,tousethematch- We used Mahimahi in conjunction with browser devel-
ingsemanticsinReplayShell’sCGIscript. opertoolstoidentifytherootcauseofthissuboptimality.
Wefoundthatthesuboptimalperformanceofeachmulti-
5.1.2 Optimalpageloadtime
plexingprotocolisaresultofrequestserializationcaused
Wedefinetheoptimalpageloadtimeforawebsiteas:
bysource-leveldependenciesbetweenobjectsonaWeb
minimumRTT+(siteSize/linkRate)+browserTime.
page;thisproblemisexacerbatedbysmalllimitsonthe
The first term represents the minimum time between numberofconcurrentconnectionsfromthebrowser,but
whenthefirstHTTPrequestismadeattheclientandthe persistsevenifthosebrowserlimitsareremoved.
7
USENIX Association 2015 USENIX Annual Technical Conference 423

1 Mbit/s link with minimum RTT of 30 ms 1 Mbit/s link with minimum RTT of 120 ms 1 Mbit/s link with minimum RTT of 300 ms
|     |                       | 1                       |     |     |     | 1                          |     |     |     | 1                          |     |     |     |     |
| --- | --------------------- | ----------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- |
|     | noitroporP evitalumuC | 0.75                    |     |     |     | noitroporP evitalumuC 0.75 |     |     |     | noitroporP evitalumuC 0.75 |     |     |     |     |
|     |                       | 0.5 SPDY: 1.08x Optimal |     |     |     | 0.5                        |     |     |     | 0.5                        |     |     |     |     |
Cumulus: 1.05x Optimal
|     |     |     |     |     |     |     |     | SPDY: 1.63x Optimal |     |     |     | SPDY: 2.02x Optimal |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | ------------------- | --- | --- |
Cumulus: 1.21x Optimal
Cumulus: 1.35x Optimal
|     |     |                    | Optimal  |       |     |      |                    | Optimal  |     |      |                    | Optimal  |       |     |
| --- | --- | ------------------ | -------- | ----- | --- | ---- | ------------------ | -------- | --- | ---- | ------------------ | -------- | ----- | --- |
|     |     | 0.25               | Cumulus  |       |     | 0.25 |                    | Cumulus  |     | 0.25 |                    | Cumulus  |       |     |
|     |     |                    |          | SPDY  |     |      |                    | SPDY     |     |      |                    | SPDY     |       |     |
|     |     |                    | QUIC-toy |       |     |      |                    | QUIC-toy |     |      |                    | QUIC-toy |       |     |
|     |     |                    | HTTP/1.1 |       |     |      |                    | HTTP/1.1 |     |      |                    | HTTP/1.1 |       |     |
|     |     | 0                  |          |       |     | 0    |                    |          |     | 0    |                    |          |       |     |
|     |     | 0 5                | 10 15    | 20 25 |     | 0    | 5                  | 10 15 20 | 25  |      | 0 5                | 10 15    | 20 25 |     |
|     |     | Page Load Time (s) |          |       |     |      | Page Load Time (s) |          |     |      | Page Load Time (s) |          |       |     |
25 Mbits/s link with minimum RTT of 30 ms 25 Mbits/s link with minimum RTT of 120 ms 25 Mbits/s link with minimum RTT of 300 ms
|     |                       | 1                       |     |     |     | 1                          |                     |     |     | 1                          |     |     |     |     |
| --- | --------------------- | ----------------------- | --- | --- | --- | -------------------------- | ------------------- | --- | --- | -------------------------- | --- | --- | --- | --- |
|     | noitroporP evitalumuC | 0.75                    |     |     |     | noitroporP evitalumuC 0.75 |                     |     |     | noitroporP evitalumuC 0.75 |     |     |     |     |
|     |                       | 0.5 SPDY: 1.15x Optimal |     |     |     | 0.5                        | SPDY: 2.39x Optimal |     |     | 0.5                        |     |     |     |     |
Cumulus: 1.07x Optimal  Cumulus: 1.22x Optimal  SPDY: 4.93x Optimal
Cumulus: 1.37x Optimal
|     |     |                    | Optimal  |       |     |      |                    | Optimal  |     |      |                    | Optimal  |       |     |
| --- | --- | ------------------ | -------- | ----- | --- | ---- | ------------------ | -------- | --- | ---- | ------------------ | -------- | ----- | --- |
|     |     | 0.25               | Cumulus  |       |     | 0.25 |                    | Cumulus  |     | 0.25 |                    | Cumulus  |       |     |
|     |     |                    |          | SPDY  |     |      |                    | SPDY     |     |      |                    | SPDY     |       |     |
|     |     |                    | QUIC-toy |       |     |      |                    | QUIC-toy |     |      |                    | QUIC-toy |       |     |
|     |     |                    | HTTP/1.1 |       |     |      |                    | HTTP/1.1 |     |      |                    | HTTP/1.1 |       |     |
|     |     | 0                  |          |       |     | 0    |                    |          |     | 0    |                    |          |       |     |
|     |     | 0 5                | 10 15    | 20 25 |     | 0    | 5                  | 10 15 20 | 25  |      | 0 5                | 10 15    | 20 25 |     |
|     |     | Page Load Time (s) |          |       |     |      | Page Load Time (s) |          |     |      | Page Load Time (s) |          |       |     |
Figure5:ThegapbetweenpageloadtimeswithHTTP/1.1,SPDY,orQUICandOptimalgrowsaslinkrateormini-
| mumRTTincreases.Cumulusisintroducedin |     |     |     |     |     | 5.2. |     |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
§
Web	Servers
Req:	HTTP	Request
Res:	HTTP	Response
...
Remote
|     |     | 		Proxy |      |              |                                      | PhantomJS	loads	page |     |               |          |      |          |              |     |     |
| --- | --- | ------- | ---- | ------------ | ------------------------------------ | -------------------- | --- | ------------- | -------- | ---- | -------- | ------------ | --- | --- |
|     |     | Local	  |      | Req1,	Scheme |                                      |                      |     | Bulk	response |          |      |          |              |     |     |
|     |     | Proxy	  |      |              |                                      |                      |     |               |          |      |          | ...          |     |     |
|     |     |         | Req1 |              |                                      |                      |     |               |          |      | Req3Res3 |              |     |     |
|     |     | User’s	 |      |              |                                      |                      |     |               | Res1Req2 | Res2 |          |              |     |     |
|     |     | Browser |      |              | Figure6:AsinglepageloadusingCumulus. |                      |     |               |          |      |          | Load	website |     |     |
The fundamental issue is that resolving each depen- headless browser, PhantomJS [2], to load the specified
dencyrequiresaround-tripcommunicationbetweenthe URL using the original HTTP headers. Once the page
client and origin Web servers. As a result, the negative is loaded, the Remote Proxy packages and compresses
effectofrequestserializationismorepronouncedathigh therecordedHTTPrequest/responsepairsintoabulkre-
RTTs (Figure 5). This finding motivated us to develop sponse,whichitsendstotheLocalProxy.
Cumulus,asystemthatusesMahimahitoimprovepage TheLocalProxyisamodifiedversionofRecordShell
loadtimesonlong-delaypaths. that caches HTTP objects rather than storing them in
|     |     |     |     |     |     |     |     | files. When | the | user’s | browser | requests | a URL | not res- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | ------- | -------- | ----- | -------- |
5.2 ImprovingWebperformancewithCumulus
|         |     |                     |     |     |         |         |     | ident in  | the Local | Proxy’s | cache, | the Local | Proxy | for-      |
| ------- | --- | ------------------- | --- | --- | ------- | ------- | --- | --------- | --------- | ------- | ------ | --------- | ----- | --------- |
| Cumulus |     | has two components: |     | the | “Remote | Proxy,” | a   |           |           |         |        |           |       |           |
|         |     |                     |     |     |         |         |     | wards the | request   | to the  | Remote | Proxy.    | Upon  | receiving |
headlessbrowserthattheuserrunsonawell-provisioned
abulkresponsefromtheRemoteProxy,theLocalProxy
| cloud   | server, | and   | the “Local | Proxy,” |            | a transparent, |     |            |        |        |           |          |             |      |
| ------- | ------- | ----- | ---------- | ------- | ---------- | -------------- | --- | ---------- | ------ | ------ | --------- | -------- | ----------- | ---- |
|         |         |       |            |         |            |                |     | responds   | to the | user’s | browser   | with the | appropriate | re-  |
| caching | HTTP    | proxy | that runs  | on      | the user’s | computer.      |     |            |        |        |           |          |             |      |
|         |         |       |            |         |            |                |     | sponse and | caches | the    | remaining | objects  | to handle   | sub- |
Thesetwocomponentscooperatetomovetheresolution
|           |     |              |        |           |     |          |     | sequent | browser | requests. | Figure | 6 illustrates |     | how Cu- |
| --------- | --- | ------------ | ------ | --------- | --- | -------- | --- | ------- | ------- | --------- | ------ | ------------- | --- | ------- |
| of object |     | dependencies | closer | to origin | Web | servers— |     |         |         |           |        |               |     |         |
mulusloadsasingleWebpage.
| reducing           |     | the effective | RTT—without |     | modifying |     | Web |                                   |     |     |     |     |     |     |
| ------------------ | --- | ------------- | ----------- | --- | --------- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
| browsersorservers. |     |               |             |     |           |     |     | 5.3 EvaluatingCumuluswithMahimahi |     |     |     |     |     |     |
The Remote Proxy listens for new requests from the We first evaluate Cumulus over each emulated network
Local Proxy. For each incoming request, the Remote configuration listed in 5.1.3. Page loads with Cumulus
§
Proxy launches an unmodified RecordShell and runs a usedGoogleChromeandaRemoteProxyrunningonthe
8
424  2015 USENIX Annual Technical Conference  USENIX Association

|     |                      | 1 Mbit/s link |     |     |                      | 14 Mbits/s link |     |     |     |                      | 25 Mbits/s link |     |     |
| --- | -------------------- | ------------- | --- | --- | -------------------- | --------------- | --- | --- | --- | -------------------- | --------------- | --- | --- |
|     | 3                    |               |     |     | 6                    |                 |     |     |     | 6                    |                 |     |     |
|     |                      | Cumulus       |     |     | Cumulus              |                 |     |     |     | Cumulus              |                 |     |     |
|     |                      | SPDY          |     |     |                      | SPDY            |     |     |     |                      | SPDY            |     |     |
|     |                      | QUIC-toy      |     |     | QUIC-toy             |                 |     |     |     | QUIC-toy             |                 |     |     |
|     |                      | HTTP/1.1      |     |     | HTTP/1.1             |                 |     |     |     | HTTP/1.1             |                 |     |     |
|     | lamitpO htiw oitaR 2 |               |     |     | lamitpO htiw oitaR 4 |                 |     |     |     | lamitpO htiw oitaR 4 |                 |     |     |
|     | 1                    |               |     |     | 2                    |                 |     |     |     | 2                    |                 |     |     |
|     | 0                    |               |     |     | 0                    |                 |     |     |     | 0                    |                 |     |     |
0 60 120 180 240 300 0 60 120 180 240 300 0 60 120 180 240 300
|     |     | Minimum RTT (ms) |     |     |     | Minimum RTT (ms) |     |     |     |     | Minimum RTT (ms) |     |     |
| --- | --- | ---------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | ---------------- | --- | --- |
Figure 7: Cumulus’s performance does not degrade dramatically as RTTs increase (at fixed link rates), unlike
HTTP/1.1,SPDY,andQUIC.Eachpointplotstheratioofmedianprotocolperformancetomedianperformanceofthe
optimalscheme(lowerisbetter).
|     |     | 1       |     |     |     |     |     | 15  |        |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
|     |     | Cumulus |     |     |     |     |     |     | Google |     |     |     |     |
|     |     | better  |     |     |     |     |     |     | TMZ    |     |     |     |     |
12
0.75
|     |     |     |     |     |     |     |     | pudeepS 9 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
FDC
0.5
Cumulus is 4x
6 faster than
Chrome Proxy
0.25
|     |     |     | Cumulus vs. Opera Turbo |     |     |     |     | 3   |     |     |     |     |     |
| --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Cumulus vs. Chrome Proxy
Cumulus
|     |     |     | Cumulus vs. Chrome |     |     |     |     |     |     |     |     | better  |     |
| --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
0
|     |     | 0 1 | 2 3     | 4   | 5   |     |     | 0 0 | 50  | 100 150 | 200 250  | 300 350 | 400 |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------- | --- |
|     |     |     | Speedup |     |     |     |     |     |     |         | RTT (ms) |         |     |
Figure8:EvaluatingCumulusontheliveAT&TCellular Figure9:BenefitswithCumulusincreaseasRTTorWeb
| NetworkinBoston. |     |     |     |     |     |     | pagecomplexityincrease. |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
other side of each emulated link. We find that Cumulus PC laptop tethered to a Samsung Galaxy Note running
| outperformsSPDYby1.03–3.60 |         |            |             | overtheseconfigura- |               |     |         |         |         |        |              |      |             |
| -------------------------- | ------- | ---------- | ----------- | ------------------- | ------------- | --- | ------- | ------- | ------- | ------ | ------------ | ---- | ----------- |
|                            |         |            | ×           |                     |               |     | Android | OS      | version | 4.2.2. | Cumulus      | used | a Remote    |
| tions                      | (Figure | 5). Figure | 7 shows how | the                 | ratio between |     |         |         |         |        |              |      |             |
|                            |         |            |             |                     |               |     | Proxy   | running | onan    | Amazon | EC2 instance |      | inVirginia. |
medianpageloadtimeswitheachprotocolandtheopti- Cumulus had median speedups of 1.36 , 1.23 , and
| mal | varies | as RTTs increase | at fixed | link | rates. We | find |      |              |     |        |                  | ×   | ×      |
| --- | ------ | ---------------- | -------- | ---- | --------- | ---- | ---- | ------------ | --- | ------ | ---------------- | --- | ------ |
|     |        |                  |          |      |           |      | 1.28 | over Chrome, |     | Chrome | Data Compression |     | Proxy, |
×
that Cumulus is less affected by increases in RTT com- andOperaTurbo,respectively.Figure8showstheCDF
paredtotoday’smultiplexingprotocols.Forexample,at
ofspeedups.
alinkrateof14Mbits/sandanRTTof60ms,Cumulus
| is1.13 |     | worsethanoptimalwhileSPDYis1.44 |     |     |     | worse |       |                            |     |     |     |     |     |
| ------ | --- | ------------------------------- | --- | --- | --- | ----- | ----- | -------------------------- | --- | --- | --- | --- | --- |
|        | ×   |                                 |     |     | ×   |       | 5.3.2 | UnderstandingCumulus’gains |     |     |     |     |     |
thanoptimal.WhenRTTincreasesto180ms,Cumulus
|        |     |                         |     |     |              |     | Cumulus | moves | dependency |        | resolution | to        | the Remote |
| ------ | --- | ----------------------- | --- | --- | ------------ | --- | ------- | ----- | ---------- | ------ | ---------- | --------- | ---------- |
| is1.39 |     | worse,whereasSPDYis2.61 |     |     | worsethanop- |     |         |       |            |        |            |           |            |
|        | ×   |                         |     | ×   |              |     | Proxy   | where | RTTs       | to Web | servers    | are lower | than from  |
timal.
theclient.Thebenefitofthistechniquedependson:
5.3.1 Someliveexperiments
|     |     |     |     |     |     |     | 1. TheRTTbetweentheuserandoriginWebservers. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
We also compare the performance of Google Chrome 2. ThecomplexityoftheWebpage.
runinsideCumuluswithChrome,andwithChromeData
|     |     |     |     |     |     |     | To understand |     | the | importance | of  | each factor, | we use |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ---------- | --- | ------------ | ------ |
CompressionProxy[15,16]andOperaTurbo[1],which Mahimahi’s shell abstraction to load two Web pages in
are cloud browsers that use proxy servers for compres- emulation: TMZ’s homepage with 508 objects and the
sion. We load each page in the Alexa US Top 500 five Google homepage with only 15 objects. We use De-
timeswitheachsystem,rotatingamongthesystemsun- layShell to emulate fixed minimum RTTs from 0 ms to
dertesttomitigatetheeffectsofnetworkvariability.We
400ms.ForeachRTT,weloadeachpagefivetimeswith
define Cumulus’s “speedup” relative to a system as the Chrome Data Compression Proxy—which compresses
ratioofthepageloadtimeusingthatsystemtothepage objects in-flight, but does not perform dependency res-
loadtimeusingCumulus. olution on the user’s behalf—and Cumulus, which per-
We ran experiments over the live AT&T formsdependencyresolutionandcompressesobjectsin-
| LTE/GSM/WCDMAcellularnetworkinBostonusinga |     |     |     |     |     |     | flight. |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
9
USENIX Association   2015 USENIX Annual Technical Conference  425

Page loads with Cumulus used a Remote Proxy run-
1
ning on the other side of the emulated long-delay link.
0.8
Speedups for Cumulus relative to Chrome Data Com-
0.6
pressionProxyareshowninFigure9.
0.4
Weobservetwotrends:
0.2
1. For a given Web page, speedups with Cumulus in-
00 5000 10000 15000 20000 25000
creaseasRTTincreases.
2. ForafixedRTT,speedupswithCumulusarelarger
formorecomplexWebpages.
Our results show a 4 speedup relative to Chrome
×
Data Compression Proxy at an RTT of 100 ms, a typi-
calRTTforcellularandtranscontinentallinks.Thiscor-
roborates the well-known intuition that Web page load
timesaredominatedbynetworklatenciesratherthanlink
rates,andsuggeststhatthecombinationofremotedepen-
dencyresolutionandobjectcompressionhelpsCumulus
achieveperformancenotfarfromoptimal.
5.4 Speedindex
Allofourmeasurementsthusfarhavebeenofpageload
time. We now show that it is straightforward to use a
differentperformancemetric.WeuseGoogle’sproposed
speedindex[17]asanexample.
5.4.1 Definition
Pageloadtimemaynotaccuratelymeasurewhenapage
is usable by the client. For long Web pages, content
“above-the-fold” of the screen is important to retrieve
quickly,butothercontentmaynotbe.Takingthispoint
intoconsiderationformeasurementisespeciallyrelevant
for pages that support infinite scrolling. For example,
Facebook“preloads”wallpostingsbelowtheuser’scur-
rent location on its page in anticipation of a user scroll.
In such cases, the “onload” event used to measure page
loadtimewouldfirelongafterthepageisreadyforuser
interaction.Speedindexisanattempttoaddressthisis-
sue.
SpeedindextracksthevisualprogressofaWebpage
inthevisibledisplayarea.Alowerspeedindexsignifies
that the content is rendered more quickly. For example,
apagethatimmediatelypaints90%ofitsvisualcontent
willreceivealowerspeedindexthanapagethatprogres-
sively paints 90% of its content, even if both pages fire
theironloadeventatthesametime.
Speedindexiscalculatedbymeasuringthecomplete-
nessofapage’sdisplayareaovertime.Completenessis
defined as the pixel-by-pixel difference of a page snap-
shotwiththefinalloadedWebpage.Oncetheentirepage
hasloaded,thecompletenesspercentageofthepageren-
deringovertimeisplotted.Speedindexisdefinedasthe
area“above-the-curve”(Figure10a).
5.4.2 Measuringspeedindex
WecalculatespeedindexusingWebPagetest[17],which
records videos of page loads at 10 frames per second
426 2015 USENIX Annual Technical Conference USENIX Association
dedaol
noitcarF
Fraction of page loaded with time
Speed Index:10475.0
Time (ms)
(a)Speedindexistheareaabovethecurveofthecompleteness
ofapageloadasafunctionoftime.
1
0.8
0.6
0.4
0.2
0
dedaol
noitcarF
Fraction of page loaded with time
Speed Index = Opt. Page Load Time
Opt. Page Load Time
(b) We define an upper bound on optimal speed index by as-
suming that a page instantaneously jumps from 0% to 100%
completenessattheoptimalpageloadtime.
Figure10:Speedindexcalculation.
andplotsthepercentagecompletenessovertimebycom-
paring each frame with the final captured frame. To
measure speed index, we create SpeedIndexShell where
we run a private instance of WebPagetest inside Re-
playShell. To automate testing, we use WebPagetest’s
wpt batch.py API [18]. Because WebPagetest runs
onlyonWindows,werunWebPagetestwithinaVirtual-
BoxWindowsvirtualmachine,insideReplayShell.
5.4.3 Optimalspeedindex
Calculating an optimal speed index is difficult. Instead,
we define an upper bound6 on the optimal speed index.
We assume that a site renders in one shot at the opti-
mal page load time; Figure 10b illustrates its implica-
tions on the “optimal” speed index. As shown, the per-
centage completeness of a given Web page is 0% until
the optimal page load time where the percentage com-
pletenessjumpsto100%.Asaresult,the“areaabovethe
curve,”or optimalspeedindex, equalstheoptimalpage
loadtime.Therecouldbebetterrenderingstrategiesthat
moregraduallyrenderthepagebetween0andtheopti-
malpageloadtime,butsuchimprovedcharacterizations
oftheoptimalspeedindexwillonlyfurtherincreasethe
already large slowdowns (Figure 11) from the optimal
speedindex.
5.4.4 Staticlinkresults
WemeasurethespeedindexforeachsiteintheAlexaUS
Top500overnetworkswithlinkratesbetween1Mbit/s
and 25 Mbits/s and a fixed minimum RTT of 120 ms
(Figure11).Wenoticesimilarpatternstothosediscussed
withpageloadtimes:thegapbetweenspeedindexwith
HTTP/1.1 and optimal speed index grows as link rates
6Recallthatalowerspeedindexisbetter.
10

1
0.75
0.5
0.25
0
0 5000 10000 15000 2000025000
USENIX Association 2015 USENIX Annual Technical Conference 427
noitroporP
evitalumuC
1 Mbit/s link with minimum RTT of 120 ms
1
0.75
0.5 HTTP/1.1 is 1.52x
worse than optimal
0.25
Optimal
HTTP/1.1
0
0 5000 10000 15000 2000025000
Speed Index
noitroporP
evitalumuC
14 Mbits/s link with minimum RTT of 120 ms
1
0.75
HTTP/1.1 is 3.35x 0.5
worse than optimal
0.25
Optimal
HTTP/1.1
0
0 5000 10000 15000 2000025000
Speed Index
noitroporP
evitalumuC
25 Mbits/s link with minimum RTT of 120 ms
HTTP/1.1 is 3.63x
worse than optimal
Optimal
HTTP/1.1
Speed Index
Figure11:GapbetweenspeedindexwithHTTP/1.1andOptimalgrowsaslinkrateincreases(fixedminimumRTT).
increase; over a 1 Mbit/s link with a 120 ms minimum Browser networking: Engineers at Mozilla are using
RTT, speed index with HTTP/1.1 is 1.52 worse than Mahimahi to improve the speed of Firefox’s network-
×
optimalatthemedian,whileovera25Mbits/slinkwith ing.Here,Mahimahiishelpfulinunderstandinghowim-
a 120 ms minimum RTT, the median speed index with provements to link utilization and pipelining of HTTP
HTTP/1.1is3.63 worsethanoptimal. requestsaffectWebperformanceovervariousnetworks.
×
5.5 Externalcasestudies 6 CONCLUSION
ThissectiondescribesexternalusecasesofMahimahiin Mahimahi is an accurate and flexible record-and-replay
research,educational,andindustrialsettings. framework for HTTP applications. Mahimahi’s shell-
Mobile app record-and-replay: RecordShell has baseddesignmakesitcomposableandextensible,allow-
been used to characterize mobile app traffic by record- ing the evaluation of arbitrary applications and network
ingallHTTPtraffictoandfrommobileappsrunningin- protocols.Itaccuratelyemulatesthemulti-servernature
sideanAndroidemulator[13].Usingthisrecordedtraf- of Web applications during replay, and by isolating its
fic,theyevaluatedtheperformanceofmobileappsover own traffic, allows several instances to run in parallel
Wi-Fi and LTE networks by running an Android emu- withoutaffectingcollectedmeasurements.
latorinsideReplayShelltomeasurethedurationofdata We presented several case studies to evaluate
transfers for mobile apps over these wireless networks. Mahimahianddemonstrateitsbenefits.Theseincludea
TheresultsshowedthatLTEoutperformsWi-Fi40%of studyofHTTP/1.1,SPDY,andQUICundervariousem-
thetimeonflowcompletiontime. ulated network conditions. We used Mahimahi both to
Mobile multi-homing: To emulate mobile multi- conduct the experiments and to understand the reasons
homingwithWi-FiandLTE,theauthorsin[12]extended for the suboptimality of these protocols. We then used
LinkShell to create MpShell [33]. They then compared ourkeyfinding—thattheseprotocolsaresuboptimaldue
single-path TCP and MPTCP by replaying mobile app to source-level dependencies in Web pages—to design
trafficover20differentemulatednetworkconditions. Cumulus. Mahimahi was useful in our implementation
Record-and-replay for video streaming: Mahimahi ofCumulus,aswellasinourexperimentstomeasureits
has been extended to handle record and replay for performance.Asround-triptimesandlinkratesincrease,
YouTube videos [36]. Compared to Web pages, video theperformanceofCumulusdegradesmuchslowerthan
replay requires more involved matching logic on the previousHTTPmultiplexingprotocols.
serverside.HTTPrequestsencodethelocation(startand WehavereleasedMahimahiunderanopensourceli-
end time) and quality of video chunks requested by the censeathttp://mahimahi.mit.edu.
client’s video player. Both the location and quality at-
tributescanchangesignificantlyfromruntorun,andbe-
7 ACKNOWLEDGEMENTS
tweenrecordandreplay. We thank Amy Ousterhout, Pratiksha Thaker, the ATC
Educational uses: Mahimahi is being used by stu- reviewers,andourshepherd,LiubaShrira,fortheirhelp-
dents in Stanford’s graduate networking course [41] to ful comments and suggestions. This material is based
understand the performance of their networked applica- upon work supported in part by the National Science
tions under controlled conditions. As part of a protocol Foundation under Grant No. CNS-1407470. We thank
design contest conducted in the same course, students the members of the MIT Center for Wireless Networks
usedLinkShell’slivegraphingofnetworkusageandper- and Mobile Computing (Wireless@MIT) for their sup-
packetqueuingdelaytoobtainreal-timefeedbackonthe port.
performanceoftheircongestion-controlprotocols.
11

REFERENCES //sites.google.com/a/webpagetest.
org/docs/advanced-features/
[1] OperaTurbo.
http://www.opera.com/turbo. webpagetest-batch-processing-apis.
[2] PhantomJS. http://phantomjs.org/. [19] R.Jennings,E.Nahum,D.Olshefski,D.Saha,
[3] SPDY:Anexperimentalprotocolforafasterweb. Z.-Y.Shae,andC.Waters. AstudyofInternet
http://www.chromium.org/spdy/ instantmessagingandchatprotocols. Network,
spdy-whitepaper. IEEE,20(4):16–21,2006.
[4] Akamai. StateoftheInternet. http://www. [20] A.Jurgelionis,J.Laulajainen,M.Hirvonen,and
akamai.com/stateoftheinternet/, A.Wang. Anempiricalstudyofnetemnetwork
2013. emulationfunctionalities. InICCCN,2011.
[5] Alexa. TopsitesintheUnitedStates. [21] B.Lantz,B.Heller,andN.McKeown. Anetwork
http://www.alexa.com/topsites/ inalaptop:Rapidprototypingforsoftware-defined
countries/US. networks. InHotNets,2010.
[6] S.AndricaandG.Candea. WaRR:Atoolfor [22] K.Ma,R.Bartos,S.Bhatia,andR.Nair. Mobile
high-fidelitywebapplicationrecordandreplay. In videodeliverywithHTTP. Communications
DSN,2011. Magazine,IEEE,49(4):166–175,2011.
[7] E.W.Biederman. ip-netns. [23] R.Netravali,A.Sivaraman,K.Winstein,S.Das,
http://man7.org/linux/man-pages/ A.Goyal,andH.Balakrishnan. Mahimahi:A
man8/ip-netns.8.html. lightweighttoolkitforreproducibleweb
[8] B.Burg,R.Bailey,A.J.Ko,andM.D.Ernst. measurement(demo). InSIGCOMM,2014.
Interactiverecord/replayforwebapplication [24] R.Netravali,K.J.Winstein,andA.Sivaraman.
debugging. InUIST,2013. LossShell. https://github.com/
[9] K.Calvert,M.Doar,andE.Zegura. Modeling
ravinet/mahimahi/tree/lossshell.
Internettopology. IEEECommunications [25] C.Paasch,S.Barre,etal. MultipathTCPinthe
Magazine,35(6):160–163,1997. Linuxkernel.
[10] M.CarboneandL.Rizzo. Dummynetrevisited.
http://multipath-tcp.org/.
SIGCOMMCCR,40(2):12–20,2010. [26] J.PadhyeandH.F.Nielsen. Acomparisonof
[11] Chromium. web-page-replay. SPDYandHTTPperformance. Technicalreport,
https://github.com/chromium/ Microsoft,2012.
web-page-replay. [27] L.Popa,A.Ghodsi,andI.Stoica. HTTPasthe
[12] S.Deng. IntelligentNetworkSelectionandEnergy narrowwaistofthefutureInternet. InHotnets,
ReductionforMobileDevices. 2010.
http://people.csail.mit.edu/ [28] L.Ravindranath,J.Padhye,S.Agarwal,
shuodeng/papers/thesis.pdf. R.Mahajan,I.Obermiller,andS.Shayandeh.
[13] S.Deng,R.Netravali,A.Sivaraman,and AppInsight:Mobileappperformancemonitoring
H.Balakrishnan. WiFi,LTE,orboth?Measuring inthewild. InOSDI,2012.
multi-homedwirelessInternetperformance. In [29] J.Roskind. ExperimentingwithQUIC.
http://blog.chromium.org/2013/06/
IMC,2014.
[14] P.Gill,M.Arlitt,Z.Li,andA.Mahanti. YouTube
experimenting-with-quic.html.
trafficcharacterization:Aviewfromtheedge. In [30] J.Roskind. QUIC:Multiplexedstreamtransport
IMC,2007. overUDP. https://docs.google.com/
[15] J.Glowacki. Datacompressionproxy. https: document/d/1RNHkx_
//chrome.google.com/webstore/ VvKWyWg6Lr8SZ-saqsQx7rFV-ev2jRFUoVD34/
detail/data-compression-proxy/ edit .
ajfiodhbiellfpcjjedhmmmpeeaebmep. [31] N.Rudrappa. DefeatSSLCertificateValidation
[16] Google. Datacompressionproxy. forGoogleAndroidApplications. Technical
https://developer.chrome.com/ report,McAfee,2013.
multidevice/data-compression. [32] A.Sivaraman,R.Netravali,andK.J.Winstein.
[17] Google. SpeedIndex. https: CodelShell.
//sites.google.com/a/webpagetest. https://github.com/ravinet/
org/docs/using-webpagetest/ mahimahi/releases/tag/old/codel.
metrics/speed-index. [33] A.Sivaraman,R.Netravali,andK.J.Winstein.
[18] Google. WebPagetestbatchprocessingAPIs. MPShell. https:
https: //github.com/ravinet/mahimahi/
12
428 2015 USENIX Annual Technical Conference USENIX Association

| tree/old/mpshell_scripted. |          |     | https://dvcs.w3.org/hg/webperf/ |     |
| -------------------------- | -------- | --- | ------------------------------- | --- |
| [34] Telerik.              | Fiddler. |     | raw-file/tip/specs/             |     |
http://www.telerik.com/fiddler. NavigationTiming/Overview.html.
[35] Telerik. Fiddlerdocumentation. [39] G.White,J.-F.Mule,andD.Rice. Analysisof
http://docs.telerik.com/fiddler/
SPDYandTCPinitcwnd.
| Configure-Fiddler/Tasks/ |     |     | http://tools.ietf.org/html/           |     |
| ------------------------ | --- | --- | ------------------------------------- | --- |
| TrustFiddlerRootCert.    |     |     | draft-white-httpbis-spdy-analysis-00. |     |
[36] V.Vasiliev,R.Netravali,K.J.Winstein,and [40] K.Winstein,A.Sivaraman,andH.Balakrishnan.
A.Sivaraman. YoutubeShell. https: Stochasticforecastsachievehighthroughputand
//github.com/vasilvv/mahimahi. lowdelayovercellularnetworks. InNSDI,2013.
[37] X.S.Wang,A.Balasubramanian, [41] K.J.Winstein. (Your)greatideasfornetworked
| A.Krishnamurthy,andD.Wetherall. |              | Howspeedy | applications.                     | https: |
| ------------------------------- | ------------ | --------- | --------------------------------- | ------ |
| isSPDY?                         | InNSDI,2014. |           | //web.stanford.edu/class/cs344g/. |        |
[38] Z.WangandA.Jain. Navigationtiming.
13
USENIX Association   2015 USENIX Annual Technical Conference  429