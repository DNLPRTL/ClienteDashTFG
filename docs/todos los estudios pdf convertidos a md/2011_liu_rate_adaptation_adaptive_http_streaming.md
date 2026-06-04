Rate Adaptation for Adaptive HTTP Streaming
Chenghao Liu Imed Bouazizi Moncef Gabbouj
Department of Signal Processing, Nokia Research Center Department of Signal Processing,
Tampere University of Technology Tampere, Finland Tampere University of Technology
Tampere, Finland +358 5 0486 0855 Tampere, Finland
+358 5 0934 9231
imed.bouazizi@nokia.com
+358 3 3115 3967
chenghao.liu@tut.fi moncef.gabbouj@tut.fi
ABSTRACT 1. INTRODUCTION
Recently, HTTP has been widely used for the delivery of real-
The current Internet is a best effort network; therefore, the
time multimedia content over the Internet, such as in video
network resources are characterized with varying available end-
streaming applications. To combat the varying network resources
to-end bandwidth. In order to improve the user experience of
of the Internet, rate adaptation is used to adapt the transmission
multimedia streaming services, rate adaptation is used to prevent
rate to the varying network capacity. A key research problem of
the client buffer from under-flowing and to achieve maximum
rate adaptation is to identify network congestion early enough and
possible playback quality. Rate adaptation may be performed at
to probe the spare network capacity. In adaptive HTTP streaming,
the sender, the receiver, or both. If the rate adaptation is
this problem becomes challenging because of the difficulties in
performed by the server, it is categorized as sender-driven rate
differentiating between the short-term throughput variations,
adaptation. The proposed algorithms in [6] and [7] can be
incurred by the TCP congestion control, and the throughput
categorized as a class of sender-driven rate adaptation. In [6], a
changes due to more persistent bandwidth changes.
rate adaptation algorithm over TCP is proposed which estimates
In this paper, we propose a novel rate adaptation algorithm for the network bandwidth and client buffer occupancy using implicit
adaptive HTTP streaming that detects bandwidth changes using a feedback information built in the TCP congestion control. In [7],
smoothed HTTP throughput measured based on the segment fetch the authors propose an adaptive streaming algorithm for streaming
time (SFT). The smoothed HTTP throughput instead of the of scalable video over UDP based on client buffer feedback.
instantaneous TCP transmission rate is used to determine if the When streaming adaptation is performed by the client, it is
bitrate of the current media matches the end-to-end network classified as receiver-driven rate adaptation. One typical technique
bandwidth capacity. Based on the smoothed throughput of this class is the receiver-driven layered multicast (RLM) [9]. In
measurement, this paper presents a receiver-driven rate adaptation RLM, the server uses scalable video coding techniques to produce
method for HTTP/TCP streaming that deploys a step-wise a set of layered bit streams and transmit each layer of the bit
increase/ aggressive decrease method to switch up/down between stream to a different multicast group. The receiver periodically
the different representations of the content that are encoded at joins multicast groups to probe the spare network capacity until it
different bitrates. Our rate adaptation method does not require any detects congestion. When multiple receivers observe packet loss,
transport layer information such as round trip time (RTT) and they conclude the network undergoes a congestion situation.
packet loss rates which are available at the TCP layer. Simulation However, the packet loss based congestion detection may not
results show that the proposed rate adaptation algorithm quickly differentiate between losses due to congestion and link layer
adapts to match the end-to-end network capacity and also induced loss. To solve this problem, paper [8] proposes a multi-
effectively controls buffer underflow and overflow. buffer based congestion control for multicast streaming of
scalable video which uses the media time in the client buffer to
Categories and Subject Descriptors
detect congestion even before packet loss happens. However, the
D.3.3 [Computer-Communication Networks]: Network rate adaptation methods presented in [7], [8] and [9] are designed
Protocols – Application (multimedia streaming). for multimedia streaming over UDP. The authors in [6] discuss
the sender-driven adaptive streaming over TCP. Given that
General Terms
HTTP/TCP [1] is used for multimedia streaming, the sender is
Algorithms, Measurement, Standardization. expected to be an HTTP server or a web cache, thus typically not
keeping information about the receiver’s connection state.
Keywords
Furthermore the sender-driven rate adaptation method has
Adaptive HTTP streaming, multimedia streaming over TCP, rate limitation in supporting the large-scale multimedia delivery since
adaptation, 3GPP PSS, TCP congestion control. it will dramatically increase the burden on the web server or
cache. Hence, it is expected that the rate adaptation in adaptive
HTTP streaming will solely be receiver-driven. In this paper we
Permission to make digital or hard copies of all or part of this work for examine the problem of receiver-driven rate adaptation for the
personal or classroom use is granted without fee provided that copies are application of the adaptive HTTP streaming.
not made or distributed for profit or commercial advantage and that
copies bear this notice and the full citation on the first page. To copy Researchers recently revisited the fundamental question about the
otherwise, or republish, to post on servers or to redistribute to lists, suitability of HTTP/TCP for delay-critical applications such as
requires prior specific permission and/or a fee. multimedia streaming. The dominant usage of TCP is mainly
MMSys’11, February 23–25, 2011, San Jose, California, USA. attributable to the congestion avoidance algorithm, which has so
Copyright 2011 ACM 978-1-4503-0517-4/11/02...$10.00. far ensured the scalable growth of the Internet. However, the
169

congestion avoidance algorithm of TCP results in a saw-tooth since buffer underflows cause playback interruptions and
shaped instantaneous transmission rate. Additionally, the extreme overflows result in bandwidth waste. Third, the rate adaptation
reliability of TCP results in excessive transmission delays and algorithm should be equipped with good convergence property
delay jitter due to retransmissions and in-order delivery. As a and prevent hopping between neighbor media representations,
result, it was widely accepted that TCP is not adequate for especially when the available end-to-end bandwidth lies within
multimedia streaming applications, which are delay sensitive but the bitrate range of two adjacent representations. Fourth, the
to some extent loss tolerant. Despite this common understanding, media segment duration needs to be set appropriately in order to
a dominant share of multimedia traffic is being delivered using minimize the HTTP overhead, thus minimizing the delay
TCP nowadays. HTTP/TCP is easy to configure and is typically introduced by HTTP request processing and transmission and
granted traversal of firewalls and network address translators, maximizing the adaptation speed.
which makes it attractive for multimedia streaming applications.
In this paper, we propose a receiver-driven rate adaptation
Recent studies reveal that the instantaneous transmission rate algorithm for adaptive HTTP streaming. For deciding switch-up
variation of TCP called short-term throughput can be smoothed or switch-down operations between different representations, a
out by receiver-side buffering. In [5], the authors propose that the smoothed HTTP/TCP throughput measurement method is
receiver side buffer can be used to smooth out the variation effect presented that compares the segment fetch time with the media
of TCP transmission rate. Furthermore, paper [4] discusses the playback time contained in that segment shortly media segment
receiver buffer requirement and presents an analytic expression of duration. A typical media segment contains 5-10 seconds which is
the minimum receiver buffer size to achieve the desired video sufficiently long to smooth short-term variations in the TCP
quality. These research results show that interruption-free throughput. For probing the spare network capacity a step-wise
multimedia streaming over TCP can be achieved under the switch-up method is used to switch to a higher representation.
assumption that the network resources are not dynamically Upon detecting network congestion, an aggressive switch down
changing. Most of the current media streaming over web shortly method is deployed to prevent playback interruptions. Possible
called web streaming uses a similar approach, so called switch up and switch down operations are assessed each time after
progressive download, to provide streaming services. In the receiving a media segment. In order to save network bandwidth
current web streaming, such as provided by popular video portals, and memory resources for the users, a method for determining the
a set of pre-defined quality levels of a video clip is offered to the idle time between two consecutive GET requests for media
users for manual a-priori selection. Each level represents a segments is deployed, thus limiting the maximum amount of
specific definition and bitrate, and is henceforth called a media pre-fetching.
representation. If the bitrate of the selected representation turns
The rest of this paper is organized as follows. Section 2 describes
out to be higher than the available end-to-end bandwidth, then the
the adaptive HTTP streaming system. The proposed rate
user will most probably experience playback interruptions and re-
adaptation method for HTTP streaming is presented in section 3.
buffering events due to buffer underflows. Otherwise, if the
Section 4 and 5 show the simulation results and conclusion.
bitrate of the representation is lower than the available network
bandwidth, then the user will consume the content at a sub- 2. ADAPTIVE HTTP STREAMING
optimal quality. Moreover, as the bandwidth capacity is higher
SYSTEM
than the representation bitrate, the client will be downloading the
content at a faster pace, which could result in bandwidth waste if
In this section, we give an overview of the system specified in the
the user decides to stop watching the content (e.g. when zapping).
3GPP PSS Adaptive HTTP streaming solution [12] shortly
To solve the problems in the current web streaming, the 3GPP denoted as 3GPP adaptive HTTP streaming.
group recently standardized the adaptive HTTP streaming solution
as part of Packet-switched Streaming Service (PSS) [12].
Adaptive HTTP streaming in 3GPP PSS follows a strategy of
sequential requesting and receiving of small media chunks of the
multimedia content, so-called media segments. 3GPP PSS
adaptive HTTP streaming further enables the client to request
media segments from different representations to react to varying
network resources. Each representation consists of multiple media
segments containing certain duration of media data and encoded
at a specific bitrate [13]. The research problems in the adaptive Figure 1. Adaptive HTTP streaming system
HTTP streaming include the following aspects in addition to the
Figure 1 shows a 3GPP adaptive HTTP streaming system. As
common rate adaptation in media streaming. First, the rate
mentioned in the introduction, adaptive HTTP streaming operates
adaptation method must deploy a metric to identify if the bitrate
as a set of sequential HTTP requests and responses.
of a specific representation matches the available end-to-end
bandwidth or not. This metric is expected to distinguish between The server can be a standard web server with the functionality to
throughput changes due to network bandwidth variations and create media presentations as specified in 3GPP adaptive HTTP
those attributable to the congestion control and avoidance streaming. Creating media presentations may be done offline
algorithm in TCP. To achieve efficient rate adaptation, the metric (static mode) or upon request (dynamic mode). In the static mode,
should identify any mismatch between the representation bitrate the media presentation description (MPD) and representations are
and the available end-to-end bandwidth quick enough in order to already created before starting any adaptive HTTP streaming
react promptly and reach the optimum representation level sessions. In the dynamic mode, the server creates the media
quickly. Second, the rate adaptation algorithm has to manage the segments based on the received HTTP GET requests [12].
client buffer in order to prevent buffer underflows and overflows,
170

The client may send a series of GET requests, each of which  slower rate adaptation behavior. Based on our observations, media
requests a media segment of a representation that is identified  segments of around 10 seconds are basically sufficient to smooth
through  a  unique  level  identifier  (ID).  In  adaptive  HTTP  out the varying instantaneous TCP transmission rate, and hence to
streaming, the client performs rate adaptation by identifying the  produce the smoothed HTTP/TCP throughput measurement.
representation that matches as closely as possible the end-to-end
|                     |           |           |       |             |      | The  advantage  | of        | using  | smoothed  | HTTP/TCP    | throughput   |
| ------------------- | --------- | --------- | ----- | ----------- | ---- | --------------- | --------- | ------ | --------- | ----------- | ------------ |
| network  capacity.  | In  3GPP  | adaptive  | HTTP  | streaming,  | the  |                 |           |        |           |             |              |
|                     |           |           |       |             |      | measurement     | compared  | to     | the  TCP  | throughput  | calculation  |
adaptation may take place each time before requesting a new
|     |     |     |     |     |     | equation  | in  paper  | [10]  is  | that  our  | method  | does  not  require  |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | --------- | ---------- | ------- | ------------------- |
media segment.
information from the transport layer (TCP layer). In order to use
3.  PROPOSED RATE ADAPTATION  the TCP throughput calculation equation, the packet loss rates and
round trip time (RTT) are required, however, such information is
ALGORITHM
not available at the application layer. By contrast our method only
needs to measure the segment fetch time. Therefore our method is
This section presents an advanced rate adaptation algorithm for
feasible for application layer end-to-end rate adaptation.
HTTP streaming. Our algorithm compares the segment fetch time
| with  the  media  | duration  contained  |     | in  the  segment  | to  | detect  |                                 |     |     |     |     |     |
| ----------------- | -------------------- | --- | ----------------- | --- | ------- | ------------------------------- | --- | --- | --- | --- | --- |
|                   |                      |     |                   |     |         | 3.2  Rate Adaptation Algorithm  |     |     |     |     |     |
congestion and probe the spare network capacity. An effective
In this section we present a rate adaptation algorithm based on the
rate adaptation algorithm is presented which adapts the bitrate by
|     |     |     |     |     |     | proposed  | smoothed  | HTTP/TCP  |     | throughput  | measurement  |
| --- | --- | --- | --- | --- | --- | --------- | --------- | --------- | --- | ----------- | ------------ |
switching up/down between different representations each time
presented in section 3.1. The smoothed HTTP/TCP throughput
after receiving a media segment and before sending the next
reveals the available network capacity and is suitable to be used as
request.
|     |     |     |     |     |     | a  metric  | of  detecting  | network  | congestion  |     | and  probing  spare  |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | -------- | ----------- | --- | -------------------- |
3.1  Smoothed HTTP/TCP Throughput  network resources. Fig. 2 shows the flowchart of the proposed rate
Measurement   adaptation algorithm for the adaptive HTTP streaming. The rate
adaptation algorithm determines the representation for fetching
It is well known that the instantaneous TCP transmission rate is
|     |     |     |     |     |     | the  next  | media  segment  |     | each  time  | after  | receiving  a  media  |
| --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | ----------- | ------ | -------------------- |
dynamically changing hence it is not feasible to measure the
segment.   The rate adaptation deploys a step-wise switch up and
network capacity using the instantaneous TCP transmission rate.
|     |     |     |     |     |     | aggressive  | switch-down  | method  |     | to  change  | the  consumed  |
| --- | --- | --- | --- | --- | --- | ----------- | ------------ | ------- | --- | ----------- | -------------- |
So instead, the client measures the segment fetch time, which
representation from different bitrates encoded representations.
covers a relatively long period of time, to determine if the bitrate
of the current representation matches the available end-to-end
Start
bandwidth capacity. The segment fetch time ((cid:1845)(cid:1832)(cid:1846)) denotes a
period of time from the time instant of sending a GET request for  receive
a segment
a media segment to the instant of receiving the last bit of the
| requested media segment.   |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
send GET next get
|                                                                    |     |     |     |     |     |                 |     | switch-up |     |     | switch-down |
| ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --------------- | --- | --------- | --- | --- | ----------- |
| In order to play media smoothly, the playing rate should be equal  |     |     |     |     |     | segment request |     |           |     |     |             |
to the receiving rate in terms of media time. Thus if the encoded  set representation level
representation level
media bitrate of the current representation matches the end-to-end  to next higher level
is determined with
average TCP throughput, then the segment fetch time should be  the first r to meet (4)
i
equal to the media segment duration. Otherwise, if the segment  sleep t (s)   t (s) > 0
|     |     |     |     |     |     |     | s   | s   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fetch time is larger than the media segment duration then it means
that the average TCP throughput is lower than the bitrate of the  Figure 2.  Flowchart of the proposed rate adaptation
current representation. Otherwise (if the segment fetch time is
algorithm of the adaptive HTTP streaming
lower than the media segment duration), it indicates that the
|     |     |     |     |     |     | The  switch  | up/switch  | down  | operations  |     | are  determined  as  |
| --- | --- | --- | --- | --- | --- | ------------ | ---------- | ----- | ----------- | --- | -------------------- |
average TCP throughput is higher than the bitrate of the current
follows:.Switch up:  takes place if inequality (2) is met and the
representation. The last situation can occur in HTTP streaming
buffered media time is larger than the predefined minimum.
because the TCP sender transmits the available data at the highest
possible  rate  provided  by  the  TCP  congestion  control  and  (cid:2020)(cid:3408)1(cid:3397)(cid:2013)                                            (2)
avoidance algorithm. Hence the ratio of media segment duration
to segment fetch time denoted as (cid:2020) is used as metric to detect  where (cid:2020) denotes the ratio of the media segment duration to the
congestion and probe the spare network capacity.   segment fetch time and (cid:2013) denotes a switch up factor. In (2), the
left term represents the metric to detect congestion and the right
(cid:3014)(cid:3020)(cid:3005)
(cid:2020)(cid:3404)                                                (1)  term  denotes  the  condition  to  switch  up  to  the  next  higher
(cid:3020)(cid:3007)(cid:3021)
representation level. For determining the switch-up factor, it can
| where (cid:1839)(cid:1845)(cid:1830)and (cid:1845)(cid:1832)(cid:1846) denote the media segment duration and the  |     |     |     |     |     | be set as   |     |     |     |     |     |
| ----------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
segment fetch time. The (cid:1845)(cid:1832)(cid:1846) measures how quickly the current
|     |     |     |     |     |     |     |     | (cid:3029)(cid:3293)(cid:3284)(cid:3126)(cid:3117) (cid:2879)(cid:3029)(cid:3293)(cid:3284),(cid:1482)(cid:1861)(cid:3404)(cid:4670)0,1,...,(cid:1840)(cid:3398)1(cid:4671)(cid:4669)              (3)  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- |
segment is fetched on average.   (cid:2013)(cid:3404)max (cid:4668)
(cid:3029)(cid:3293)(cid:3284)
| Then  the  smoothed                                                          | TCP  | throughput  | measurement  |     | can  be  |                   |                                                          |     |     |     |     |
| ---------------------------------------------------------------------------- | ---- | ----------- | ------------ | --- | -------- | ----------------- | -------------------------------------------------------- | --- | --- | --- | --- |
|                                                                              |      |             |              |     |          | where  (cid:1854) |  denotes the encoded media bitrate of representation i   |     |     |     |     |
| estimated by multiplying (cid:2020) with the media bitrate of the currently  |      |             |              |     |          |                   | (cid:3045)(cid:3284)                                     |     |     |     |     |
received segment. The receiver can obtain the encoded media  and (cid:1840) denotes the highest representation level.
| bitrate  of  each  | representation  | from  | the  Media  | Presentation  |     |     |     |     |     |     |     |
| ------------------ | --------------- | ----- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
As mentioned in section 3.1, the equation 2 is satisfied in the
Description (MPD). To produce the smoothed TCP throughput,
HTTP/TCP streaming scenario when the average TCP throughput
| the  media  segment  | duration  | shall  | be  selected  | appropriately.  |     |     |     |     |     |     |     |
| -------------------- | --------- | ------ | ------------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
for fetching a segment is higher than the encoded media bitrate of
| Typically  longer  | period  is  | capable  | of  producing  | smoother  |     |     |     |     |     |     |     |
| ------------------ | ----------- | -------- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
the fetched media segment. In case of a decision to switch up, the
throughput measurement. However the longer period will cause
171

rate adaptation algorithm selects the next higher representation HTTP streaming server and client. To simulate the varying delays
level. The reason for using a conservative step-wise switch-up and bandwidths an exponential traffic generator (Exp_G) and
strategy is to prevent playback interruptions that might occur in receiver (Exp_R) are used as background traffic with the average
case of aggressive switch-up operations. During the step-wise “on” time of 500ms, average “off” time of 500ms and the average
switch-up, the buffered media time is allowed to accumulate to a sending rate during “on” times is set as 1000 Kbits/s during the
safety level in order to prevent buffer underflows that might be “on” period hence the overall bitrate of the exponential traffic
incurred by sudden bandwidth drops. So the initial buffering time, during whole period is equal to 500 Kbits/s. Both web server and
spent to reach the protection level of buffered media, is reduced exponential traffic generator start operation at time 0s and end at
significantly, which improves the user experience. 1200s. In addition to background traffic a constant bitrate traffic
generator (CBR_G) and receiver (CBR_R) are added at time400s
Switch down: It will be performed if inequality (4) is met.
to 800s which is used as competitive traffic at the bottleneck
(cid:2020)(cid:3407)(cid:2011) (4) bandwidth between node 0 and the proxy. In Fig.3 the bandwidth
(cid:3031)
(Mbits/s) and delay (ms) are given for each link. For media data,
where (cid:2020) represents the ratio of media segment duration to segment 10 sets of representations are provided to perform the rate
fetch time which is used as the rate adaptation metric and (cid:2011) (cid:3031) adaptation wherein the bitrates vary from 100Kbits/s to
denotes switch down threshold. In case of congestion, the segment 1000Kbits/s with a step of 100Kbits/s and representation level 0 to
fetch time is typically much higher than the media segment 9 respectively. In the simulation, we set the (cid:1839)(cid:1845)(cid:1830), (cid:1872) , , and (cid:2011)
(cid:3040)(cid:3036)(cid:3041) (cid:3031)
duration. Hence, inequality (4) enables to detect network to 10s, 9s and 0.67.
congestion before the media buffer is drained and switches down
to a suitable representation as discussed in the following. In the
case that (4) fails to detect slight mismatches between the media Server Client
bitrates and the network capacity, the buffered media time may 10MB, 10MB,
2ms
gradually decrease. Hence, buffered media time can be compared 2ms
with a pre-calculated minimum, which is used as a 10MB, 2MB, 10MB,
complementary switch-down condition to prevent client buffer CBR_S 2ms Node0 2ms Proxy 2ms CBR_R
underflows.
In the switch down, an aggressive switch down will be performed. 10MB, 10MB,
The selected representation level is determined to be the first 2ms 2ms
Exp_S Exp_R
representation (in descending order) with level (cid:1870) to meet
(cid:3036)
(cid:1854) (cid:3407) (cid:2020)(cid:1854) (5)
(cid:3045)(cid:3284) (cid:3030) Figure. 3. Network topology
where (cid:1854) (cid:3045)(cid:3284) denotes the encoded media bitrate of the representation To the best of our knowledge, we haven’t found a receiver-driven
(cid:1870) (cid:3036) , (cid:2020) denote the ratio of media segment duration to segment fetch rate adaptation algorithm for HTTP streaming and only few
time and (cid:1854) (cid:3030) denotes the bitrate of current representation. research works have been conducted in the field of client buffer
requirement for media streaming over TCP [4] [5] and TCP-
The idle time calculation algorithm is deployed before sending the
based multimedia streaming performance analysis [11]. Hence,
next GET request, in order to prevent client buffer overflow. The
we evaluated the efficiency of the proposed method based on the
rate adaptation algorithm will wait a certain period of time after
aspect of rate adaptation accuracy and rate adaptation speed as
determining the representation level of the next segment and
follows. To identify the impact of the different variations of the
before sending the next request if the buffered media time in the
bottleneck bandwidths on the proposed rate adaptation algorithm,
client buffer is large enough to cover the maximum draining of
we vary the bitrates of competitive traffic source, i.e. the CBR
buffered media time during fetching the segment. When the
traffic generator, from 400 Kbits/s to 1400 Kbits/s at steps of 200
average TCP throughput drops from the bitrate of the current
Kbits/s, hence 6 sets of simulation were ran. For evaluating the
presentation to the bitrate of the lowest representation, the
accuracy, we analyzed the representation level statistics together
maximum amount of buffered media time will be drained. So the
with the buffered media times after the representation first reaches
idle time between determining representation level and sending
a stable stage to identify how accurately the rate adaptation
the next request is set as (cid:1872) if the inequality (6) is met
(cid:3046) algorithm approaches to the network capacity and if it is capable
(cid:1872) (cid:3404)(cid:1872) (cid:3398)(cid:1872) (cid:3398)
(cid:3029)(cid:3278)
(cid:1839)(cid:1845)(cid:1830)(cid:3408)0 (6)
to converge to a stable representation level. If the optimum
(cid:3046) (cid:3040) (cid:3040)(cid:3036)(cid:3041) (cid:3029)(cid:3288)(cid:3284)(cid:3289) representation level is n, then reaching representation level n-1 or
where (cid:1872) , (cid:1872) and (cid:1872) denote the idle time in seconds, the n+1 is considered as reaching the stable stage. The rate adaptation
(cid:3046) (cid:3040) (cid:3040)(cid:3036)(cid:3041)
buffered media time, the predefined minimum buffered media speed is represented as the time spent to reach the stable
representation level starting from the instant of changing the
time respectively and (cid:1854) and (cid:1854) denote the current
(cid:3030) (cid:3040)(cid:3036)(cid:3041)
bottleneck bandwidth.
representation bitrate and the minimum representation bitrate
respectively, and (cid:1839)(cid:1845)(cid:1830) denotes the media segment duration. The Fig. 4 shows the mean index of the consumed representations at
key advantage of the idle time method is to limit the maximum the different CBR traffic bitrates, wherein the x axis denotes the
amount of buffered media data; hence, saving network bandwidth CBR bitrates and y axis denotes the representation level. Here the
consumption and memory resources of the receiver. representation level changes from 0 and 9 corresponding to the
media bitrates of 100 Kbits/s to 1000 Kbits/s respectively. We
4. SIMULATION RESULTS
partitioned the whole simulation period into three different
We implemented the proposed rate adaptation algorithm for periods including 0-400s, 400s-800s and 800s-1200s representing
adaptive HTTP streaming in ns2 [2]. Fig. 3 shows the network the period before CBR traffic appearing, the period during CBR
topology used in the simulations. The server and client denote the traffic and after CBR traffic. The mean of representation level in
172

0-400 is constantly equal to 8.51 for all CBR bitrates since CBR media data at the highest transmission rate allowed by the TCP
traffic is not added until 400s. In the period of 400-800s, the congestion and flow control algorithms. If the rate adaptation
mean of the representation level drops along with the increase of operates in a lower than optimal representation level, then the
CBR bitrates. It shows that the rate adaptation effectively switches buffered media time will increase and vice versa. So the lower
down to the lower representation level to match the media bitrates STD in the buffered media time demonstrates more accurate rate
to the sharable end-to-end bandwidth. In the period of 800-1200s, adaptation. In the period 0s-400s, the STD and mean of buffered
when the CBR traffic disappears, the mean of representation level media time are constant and equal to 9.9s and 65.5s. Fig. 6 shows
remains relatively constant with the different CBR bitrates and that the maximum STD for the buffered media time is lower than
always higher than 8.5. This observation reveals that the 9.18s and 12.92s in the periods 400-800s and 800-1200s
performance of the rate adaptation is independent of the change in respectively. In Fig. 7, the minimum mean of the buffered media
the bandwidth. time is higher than 54s and 90s respectively in the periods 400-
800s and 800-1200s respectively. As demonstrated in the
simulation results, the STDs for the buffered media time are
relatively small compared to the mean of the buffered media time.
10 When the CBR traffic is added to compete on the bottleneck
bandwidth, it is important to identify that the rate adaptation
8
algorithm acts appropriately to prevent buffer underflows. In all of
6 the simulation results the minimum buffered media time is higher
than 36s, hence ensuring that playback interruptions do not
4
happen.
2
0
400 600 800 1000 1200 1400
Figure. 4. Mean of representation levels with CBR bitrates in
different time periods
In order to show the convergence property of the proposed rate
adaptation method after reaching the stable state, the standard
deviation (STD) of the representations level at the stable state is
depicted in Fig 5. The x and y axes are set similarly to Fig. 4. In
the period 0-400s, the STD of the representation level is
constantly equal to 0.26. In the period 800-1200s the STD is
below 0.26 and during the period 400-800s the STD is below 0.7 Figure. 6. STD of buffered media time with different CBR
except 0.99 for the CBR bitrate of 1000 Kbits/s. bitrates in different time periods
Figure. 5. STD of representation level with different CBR Figure. 7. Mean of buffered media time with different CBR
bitrates in different time periods bitrates in different time periods
In adaptive HTTP streaming, the optimum media bitrates can’t The rate adaptation speed is another important factor to evaluate
simply be estimated as the fair share of the end-to-tend bottleneck the behavior of the rate adaptation algorithm. Fig. 8 shows the rate
bandwidth, since the supported media bitrates for interruption free adaptation speed with different competition CBR bitrates in the
streaming is also affected by the round trip time (RTT) and packet different time periods. In the period of 0-400 (s) it takes 44s to
loss rates. To analyze how accurately the rate adaptation switch-up to representation 8 from representation 0. The other
algorithm matches the selected representation bandwidth to the switch-up period 800-1200 (s) shows that the rate adaptation
optimal level, the STD and the mean of the buffered media time at speed varies with the amount of competitive traffic between a
different CBR bitrates in different time periods are reported in minimum of lower than 1s and a maximum of 41s. As shown in
Fig. 6 and Fig. 7 respectively. Here, the x axis denotes the CBR the period of 400-800 (s), the mean of switch-down speeds are
bitrates and the y axis denotes the buffered media time around 30.3s and without showing any correlation with the
respectively. In HTTP streaming, the server sends the requested amount of competitive traffic at the bottleneck. The convergence
level
noitatneserpeR
Mean of 400‐800
representaiton level
800‐1200
CBR bitrates (Kbits/s)
1.2
1
0.8
0.6
0.4
0.2
0
400 600 800 1000 1200 1400
level
noitatneserpeR
14
12
10
8
6
4
2
0
400 600 800 1000 1200 1400
400‐800 STD of representaiton level
800‐1200
CBR bitrates(Kbits/s)
)s(
emit
aidem
dereffuB
400‐800
STDof buffered media time
800‐1200
CBR bitrates (Kbits/s)
120
110
100
90
80
70
60
50
40
400 600 800 1000 1200 1400
)s(
emit
aidem
dereffuB
400‐800
Mean of buffered media time
800‐1200
CBR bitrates (Kbits/s)
173

time in down switching remains within the amount of buffered 7. REFERENCES
media time, thus avoiding any buffer underflows. It is worthwhile
[1] Fielding, R., Getty, J., Mogul, J., Frystyk, H., Masinter, L.,
to note that the major part of the delay is attributable to waiting
Leach, P., Lee, T. Berners. 1999. Hypertext transfer protocol
for the current media segment fetching to finish, which takes
-- HTTP/1.1, RFC 2616. June 1999.
significantly longer when the available bandwidth drops.
[2] Information Sciences Institute, The University of Southern
California. 2006. The Network Simulator - ns-2. (13 July
2006).
60 [3] Kim, T. and Ammar, M. H.. 2006. Receiver buffer
50 requirement for video streaming over TCP. SPIE VCIP 2006
(San Jose, CA, Jan. 2006).
40
[4] Kim, T., Avadhanam, N., Subramanian, S. 2006.
30
Dimensioning receiver buffer requirement for unidirectional
20 VBR video streaming over TCP. ICIP 2006 (Atlanta, USA,
10 Oct. 2006).
0 [5] Krasic, C., Li, K. and Walpole, J. 2001. The Case for
Streaming Multimedia with TCP. In Proceedings of IDMS
400 600 800 1000 1200 1400
(Lancaster. UK, September 2001).
[6] Lam, L.S, Lee, Jack YB, Liew, S.C, Wang W. 2004. A
transparent rate adaptation algorithm for streaming video
Figure. 8. Rate adaptation speed with different CBR bitrates
over the internet. In 18th International conference on
in different time periods
advanced information networking and applications (Fukuoka,
5. CONCLUSION Japan, March 2004).
[7] Liu, C., Bouazizi, I., Gabbouj, M. 2010. Advanced rate
In this paper, we propose a novel method for detecting congestion,
adaptation for unicast streaming of scalable video. IEEE
probing spare network capacity, and measuring the smoothed
International Conference on Communications 2010 (ICC
HTTP/TCP throughput for rate adaptation in adaptive HTTP
2010) (Cape Town, South Africa. May 2010).
streaming. The advantage of the proposed smoothed HTTP/TCP
throughput measurement compared to the TCP throughput [8] Liu, C., Bouazizi, I., Gabbouj, M. 2010. Multi-buffer based
calculation equation used in TCP friendly rate control (TFRC) is congestion control for multicast streaming of scalable video.
that our method does not require the transport layer information 2010 IEEE International Conference on Multimedia & Expo
such as packets loss rates and round trip time (RTT) to be (ICME 2010) (Singapore, July 19-23, 2010).
available at the application layer. Hence, the proposed metric and [9] McCanne, S., Jacobson, V., and Vetterli, M. 1996. Receiver-
smoothed TCP throughput measurement method can be used at driven layered multicast. In the Proceedings of
the application layer. Upon detecting streaming that the media SIGCOMM'96. ACM Stanford, (CA, Aug. 1996), 117–130.
bitrate does not match the current end-to-end network capacity, an
[10] Padhye,J., Firoiu, V., Towsley, D. and Kurose, J. 2000.
algorithm for conservative step-wise up switching and aggressive
Modeling TCP Reno performance: a simple model and its
down switching of representations is presented using the
empirical validation. IEEE/ACM Transactions on
smoothed TCP throughput measurement. In addition an idle time
Networking, vol. 8, no. 2, pp. 133-145, April 2000.
calculation method is used to prevent client buffer overflow and
by consequence saving network bandwidth and memory resource [11] Wang, B., Kurose, J., Shenoy, P., and Towsley, D. 2004.
at the client. Simulation results show that the proposed metric Multimedia streaming via TCP: An analytic performance
efficiently detects the congestion and probes the spare network study. In Proceedings of ACM Multimedia (October 2004),
capacity. And the smooth TCP throughput measurement method 908 - 915. http://doi.acm.org/10.1145/1352012.1352020.
based rate adaptation method can quickly and accurately reach to
[12] 3GPP TS 26.234. 2009. Transparent End-To-End Packet-
the optimum bitrate level.
Switched Streaming Service (PSS): protocols and codecs.
(Release9).http://www.3gpp.org/ftp/Specs/archive/26_series/
6. Acknowledgment 26.234/.
[13] 3GPP SP-090710. 2010. Adaptive HTTP Streaming in PSS.
This work was supported by the Academy of Finland, (application
(Sophia-Antipolis, France, Jan. 2010. )
number 129657, Finnish Programme for Centres of Excellence in
http://www.3gpp.org/ftp/Specs/html-info/26234-CRs.htm.
Research 2006-2011).
)s(
emit
tnepS
400‐800
Rate adaptation speed
800‐1200
CBR bitrates (Kbits/s)
174