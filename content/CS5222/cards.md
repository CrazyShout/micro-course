# CS5222 bilingual card source — editable master text

@@ N001 | 01-foundations | learn | N1:4-7
Q_EN: What is the Internet, viewed as infrastructure and as a service?
Q_ZH: 从基础设施和服务两个角度看，互联网是什么？
A_EN: As infrastructure, it is an interconnection of hosts, communication links and packet switches organized into networks. As a service, it provides communication to distributed applications through interfaces such as sockets. A web page is an application using the Internet; the Web and the Internet are not synonymous. The infrastructure view explains delivery, while the service view explains what applications can request.
A_ZH: 从基础设施看，互联网由主机、通信链路和分组交换设备构成，各网络彼此连接；从服务看，它通过套接字等接口，为分布式应用提供通信。网页是使用互联网的应用，Web 与互联网并非同义。基础设施视角解释如何传送，服务视角解释应用能请求什么。

@@ N002 | 01-foundations | learn | N1:4,11
Q_EN: What are an end system, an access network and the network core?
Q_ZH: 端系统、接入网和网络核心分别是什么？
A_EN: End systems, also called hosts, run applications: laptops, phones and servers are examples. An access network connects a host to its first router. The core contains interconnected routers and links that carry packets between networks. A client and a server are application roles of hosts; a router's central role is forwarding traffic toward another link.
A_ZH: 端系统也叫主机，运行应用，例如电脑、手机和服务器。接入网把主机连接到其第一个路由器。网络核心由互联路由器和链路组成，负责跨网络传输分组。客户端与服务器是主机上的应用角色；路由器的核心职责是把流量转发到下一条链路。

@@ N003 | 01-foundations | learn | N1:8-9
Q_EN: What is a protocol?
Q_ZH: 什么是协议？
A_EN: A protocol specifies message formats, message order and actions taken when messages are sent, received or when other events occur. A simple request–response exchange needs both sides to agree on the request format and the meaning of the reply. Two devices having a physical connection is insufficient if they interpret exchanged bits differently.
A_ZH: 协议规定消息格式、消息顺序，以及发送、接收消息或其他事件发生时采取的动作。简单的请求—响应通信，也需要双方约定请求格式与应答含义。两个设备即使物理相连，若对交换比特的解释不同，也不能据此保证有效通信。

@@ N004 | 01-foundations | learn | N1:6-9
Q_EN: What are RFCs and the IETF, and how do they relate to protocols?
Q_ZH: RFC 和 IETF 是什么？它们与协议有什么关系？
A_EN: The IETF develops Internet technical specifications through an open standards process. RFCs are documents in the Request for Comments series; many describe protocols, but not every RFC is an Internet Standard. A protocol defines behavior, while its specification documents that behavior so independent implementations can interoperate.
A_ZH: IETF 通过开放的标准过程制定互联网技术规范。RFC 是 Request for Comments 文档系列，其中很多描述协议，但并非每份 RFC 都是互联网标准。协议规定行为，规范文档描述这些行为，使独立实现可以互操作。

@@ N005 | 01-foundations | learn | N1:12-16
Q_EN: What distinguishes residential, enterprise and mobile access networks?
Q_ZH: 家庭、企业和移动接入网络主要怎样区分？
A_EN: They connect users in different settings using different media and sharing arrangements. Residential access may use DSL, cable or fiber; enterprise access often combines Ethernet and Wi-Fi; mobile access uses cellular radio. Ask which physical medium is used, whether capacity is shared, and where the first router is. A quoted access rate is not a guarantee of end-to-end application throughput.
A_ZH: 它们为不同场景的用户提供接入，介质与共享方式不同。家庭可用 DSL、有线电视网或光纤；企业常组合以太网与 Wi-Fi；移动接入使用蜂窝无线。分析时应问：用什么介质、容量是否共享、第一个路由器在哪。标称接入速率不保证端到端应用吞吐量。

@@ N006 | 01-foundations | learn | N1:13
Q_EN: How does DSL share a telephone line between voice and data?
Q_ZH: DSL 如何在电话线上同时传语音和数据？
A_EN: DSL uses different frequency bands for voice and data over the local telephone copper pair. A modem handles the signal conversion, and provider equipment aggregates subscriber traffic. The subscriber's local loop is a dedicated physical pair, but that does not imply an exclusively reserved end-to-end Internet path. Upstream and downstream capacities may differ.
A_ZH: DSL 在本地铜质电话双绞线上，使用不同频段承载语音和数据。调制解调器处理信号转换，运营商设备汇聚用户流量。用户本地环路可是一对独用线缆，但不代表整个互联网路径都被独占预留。上行和下行容量也可能不同。

@@ N007 | 01-foundations | learn | N1:14
Q_EN: What functions can a home network device combine?
Q_ZH: 家庭网络设备可能把哪些功能合在一起？
A_EN: A home gateway may combine routing, an Ethernet switch, a Wi-Fi access point, NAT and firewall functions. These remain different logical functions even when housed in one box. Wi-Fi provides a local wireless connection; routing connects networks; NAT translates addresses; a firewall applies traffic rules. Losing Internet access does not necessarily mean the local Wi-Fi radio has failed.
A_ZH: 家庭网关可能在一个盒子里集成路由、以太网交换、Wi-Fi 接入点、NAT 和防火墙。它们仍是不同逻辑功能。Wi-Fi 提供本地无线连接，路由连接网络，NAT 转换地址，防火墙应用流量规则。无法访问互联网，不一定意味着本地 Wi-Fi 无线连接坏了。

@@ N008 | 01-foundations | learn | N1:15-16
Q_EN: How do Ethernet, Wi-Fi and cellular access differ at an introductory level?
Q_ZH: 入门层面，Ethernet、Wi-Fi 和蜂窝接入有何不同？
A_EN: Ethernet commonly uses wired local links and switches. Wi-Fi connects devices by radio to a local access point over a shared wireless medium. Cellular networks provide wider-area mobile radio access through operator infrastructure. All can carry Internet traffic, but their physical sharing, coverage and mobility characteristics differ. The lecture's example speeds are illustrative and may be dated.
A_ZH: 以太网通常使用有线局域链路与交换机；Wi-Fi 通过共享无线介质把设备接入本地接入点；蜂窝网络通过运营商基础设施提供更大范围的移动无线接入。三者都能承载互联网流量，但共享方式、覆盖与移动性不同。课件中的速率示例用于说明概念，可能已有年代性。

@@ N009 | 01-foundations | learn | N1:17-19
Q_EN: What are guided and unguided transmission media?
Q_ZH: 什么是导引型和非导引型传输介质？
A_EN: Guided media confine signals to a physical path, such as twisted pair, coaxial cable or optical fiber. Unguided media carry signals through space, such as radio. Fiber carries light; copper carries electrical signals. Distance, attenuation, interference, deployment cost and capacity all influence the choice. A medium determines physical constraints, while higher layers provide additional communication behavior.
A_ZH: 导引介质把信号约束在物理路径内，例如双绞线、同轴电缆和光纤；非导引介质让信号在空间传播，例如无线电。光纤传光信号，铜线传电信号。距离、衰减、干扰、部署成本和容量都会影响选择。介质决定物理约束，更高层提供额外通信行为。

@@ N010 | 01-foundations | learn | N1:17-19
Q_EN: What is the difference between transmission rate and propagation speed?
Q_ZH: 传输速率和传播速度有什么区别？
A_EN: Transmission rate $R$ is how many bits enter the link each second, measured in bit/s. Propagation speed $s$ is how fast the signal moves through the medium, measured in m/s. Increasing bandwidth can reduce the time to put a packet onto a link without making its first bit travel physically faster. Keep their units separate.
A_ZH: 传输速率 $R$ 是每秒有多少比特被放入链路，单位 bit/s；传播速度 $s$ 是信号在介质中移动的速度，单位 m/s。增加带宽可以缩短把整个分组送上链路的时间，却不一定让第一个比特在物理介质中跑得更快。必须区分两者单位。

@@ N011 | 01-foundations | worked | N1:17-19,46
Q_EN: Why can satellite communication have substantial delay even with a high bit rate?
Q_ZH: 为什么卫星通信即使比特率很高，也可能有较大时延？
A_EN: Propagation delay depends on path distance divided by signal speed, $d/s$. A long path to a satellite and back can dominate delay even if serialization is fast. Lower orbits shorten that path but introduce other system tradeoffs. High throughput and low latency are separate properties; one does not imply the other.
A_ZH: 传播时延取决于路径长度除以信号速度，即 $d/s$。即使串行化很快，往返卫星的长路径仍可能主导时延。较低轨道缩短路径，但带来其他系统权衡。高吞吐量与低时延是不同性质，不能互相推出。

@@ N012 | 01-foundations | check | N1:4-19
Q_EN: Describe the path of a laptop's web request using the terms host, access network, router and server.
Q_ZH: 用主机、接入网、路由器和服务器描述笔记本发送网页请求的路径。
A_EN: The laptop is a host running a browser. Its access network, perhaps Wi-Fi plus a home gateway, connects it to a first router. Routers forward packets through interconnected networks toward a server host. The server application sends a response back. This logical description does not require knowing the exact route, which may differ for the return direction.
A_ZH: 笔记本是运行浏览器的主机；它通过 Wi-Fi 和家庭网关等接入网连接到第一个路由器。路由器经互联网络把分组转发到服务器主机，服务器应用再发送响应。这个逻辑描述不要求知道具体路径，而且返回方向的路径可能不同。

@@ N013 | 02-switching | learn | N1:21-24
Q_EN: What is circuit switching?
Q_ZH: 什么是电路交换？
A_EN: A connection reserves resources along an end-to-end path before data transfer. Reserved capacity can provide a predictable transmission share, but idle periods may waste it. A setup delay may occur before sending the data. Distinguish a logical reserved circuit from a requirement for a completely separate physical wire for each call.
A_ZH: 电路交换在传送数据前，为连接沿端到端路径预留资源。预留容量能提供可预测的传输份额，但空闲期间可能浪费。数据发送前还可能有连接建立时延。逻辑上预留一条电路，并不意味着每个通话都必须使用完全独立的物理线缆。

@@ N014 | 02-switching | learn | N1:22-23
Q_EN: How do FDM and TDM divide a circuit-switched link?
Q_ZH: FDM 和 TDM 怎样划分电路交换链路？
A_EN: Frequency-division multiplexing allocates different frequency bands to different circuits. Time-division multiplexing allocates repeating time slots. With $k$ equal circuits and ideal total rate $R$, each gets an average rate $R/k$. In FDM the shares coexist in frequency; in TDM they alternate in time. Unused reserved shares may remain unavailable to other circuits.
A_ZH: 频分复用将不同频段分配给不同电路；时分复用分配周期性时隙。理想总速率为 $R$、均分给 $k$ 条电路时，每条平均获得 $R/k$。FDM 在频率上同时存在，TDM 在时间上轮流使用。未用的预留份额可能仍不能供其他电路使用。
MEDIA: chapter1-slide-23.png

@@ N015 | 02-switching | learn | N1:24-27
Q_EN: What is packet switching?
Q_ZH: 什么是分组交换？
A_EN: Applications' data are divided into packets that share links as needed. A packet is transmitted using the available link service rather than a permanent per-connection reserved share. Packets may wait in queues and may be dropped when buffers fill. This sharing is efficient for bursty traffic, but delay and loss depend on competing traffic.
A_ZH: 应用数据被拆成分组，按需要共享链路。分组利用链路传输服务，而不是每个连接永久占用预留份额。分组可能排队，缓冲区满时可能被丢弃。这种共享适合突发流量，但时延和丢包会受竞争流量影响。

@@ N016 | 02-switching | learn | N1:25-26
Q_EN: What does store-and-forward mean?
Q_ZH: 存储转发是什么意思？
A_EN: A switch must receive an entire packet before starting to transmit that packet on the next link. For one $L$-bit packet over two links of equal rate $R$, ignoring all other delays, the destination receives the complete packet after $2L/R$. The second link cannot begin sending this packet as soon as only its first bit reaches the switch.
A_ZH: 交换设备必须收齐一个分组，才能在下一条链路开始发送该分组。一个 $L$ 比特分组经过两条速率均为 $R$ 的链路，忽略其他时延，目的端收齐需 $2L/R$。不能仅在第一个比特到达交换设备时，就开始向下一链路发送这个分组。
MEDIA: chapter1-slide-26.png

@@ N017 | 02-switching | learn | N1:28
Q_EN: How do forwarding and routing differ?
Q_ZH: 转发与路由有什么区别？
A_EN: Forwarding is a local action: move an arriving packet to the appropriate outgoing interface using a forwarding table. Routing determines paths through the network and helps establish those tables. A road analogy is choosing the correct exit at one intersection versus planning the whole trip. Both are needed for end-to-end packet delivery.
A_ZH: 转发是局部动作：根据转发表，把到达的分组送到合适的输出接口。路由决定穿过网络的路径，并帮助建立这些表。道路类比中，转发像在一个路口选出口，路由像规划整段旅程。端到端分组传输需要两者协作。
MEDIA: chapter1-slide-28.png

@@ N018 | 02-switching | learn | N1:29-31
Q_EN: What is statistical multiplexing, and why can it serve more users than fixed reservation?
Q_ZH: 什么是统计复用？为什么它可能容纳比固定预留更多的用户？
A_EN: Statistical multiplexing shares capacity among users that happen to be active. If users are often idle and their bursts do not always coincide, many users can share a link with a low overload probability. It does not create extra physical capacity: simultaneous demand above $R$ still causes queueing or loss. Its benefit depends on traffic activity and dependence.
A_ZH: 统计复用把容量共享给当时活跃的用户。若用户经常空闲，且突发不总是同时发生，就能让更多用户共享链路，同时保持较低过载概率。它没有创造额外物理容量：总需求超过 $R$ 时仍会排队或丢包。收益取决于活跃程度及流量间的依赖关系。

@@ N019 | 02-switching | classroom | N1:29-30
Q_EN: A 1 Mbps link serves users needing 100 kbps when active. How many circuit-switched users fit?
Q_ZH: 1 Mbps 链路服务活跃时需要 100 kbps 的用户，电路交换能容纳多少用户？
A_EN: At most $1000/100=10$ users. Here 1 Mbps = 1,000 kbps, and each circuit reserves 100 kbps even while its user is idle. A low activity probability does not increase this fixed-reservation limit. Packet switching would instead require a separate model of simultaneous demand.
A_ZH: 最多 $1000/100=10$ 人。这里 1 Mbps = 1000 kbps，每条电路在用户空闲时也预留 100 kbps。活跃概率低不会提高这个固定预留上限。若讨论分组交换，则需另外建立同时需求的模型。
MEDIA: chapter1-slide-29.png

@@ N020 | 02-switching | classroom | N1:29-30
Q_EN: A 1 Mbps link serves 35 independent users, each needing 100 kbps when active and active with probability 0.1. How is the probability that demand exceeds capacity calculated?
Q_ZH: 1 Mbps 链路服务 35 个独立用户，每人活跃时需 100 kbps、活跃概率为 0.1。需求超过容量的概率如何计算？
A_EN: Assume independent activity, each with probability 0.1. Then $K\sim\operatorname{Binomial}(35,0.1)$ and $P(K>10)=\sum_{k=11}^{35}\binom{35}{k}0.1^k0.9^{35-k}\approx0.0004243$. The slide's “less than 0.0004” is a small numerical approximation error; the value is about 0.0424%. Independence is essential to this binomial calculation.
A_ZH: 假设各用户独立、活跃概率均为 0.1，则 $K\sim\operatorname{Binomial}(35,0.1)$，$P(K>10)=\sum_{k=11}^{35}\binom{35}{k}0.1^k0.9^{35-k}\approx0.0004243$。幻灯片所写“小于 0.0004”有轻微数值误差，实际约为 0.0424%。二项计算依赖用户独立这个前提。

@@ N021 | 02-switching | check | N1:29-31
Q_EN: Does low average load guarantee no queueing?
Q_ZH: 平均负载低是否保证完全不排队？
A_EN: No. Several users can transmit at the same time, creating a burst above the output rate even when average demand is low. A queue absorbs temporary excess, while a finite full buffer causes loss. Average utilization describes long-run load; burstiness and correlation affect short-term delay. State both the average and the traffic model when interpreting a result.
A_ZH: 不保证。即使平均需求低，多名用户同时发送也会形成超过输出速率的突发。队列吸收临时超额流量，有限缓冲区满时则丢包。平均利用率描述长期负载，突发性与相关性影响短期时延。解释结果时，应同时说明均值和流量模型。

@@ N022 | 02-switching | learn | N1:34-42
Q_EN: Why is the Internet called a network of networks?
Q_ZH: 为什么互联网被称为“网络的网络”？
A_EN: Access ISPs connect end users, and those networks interconnect through transit providers, peering links, Internet exchange points and other arrangements. A full mesh of $N$ access networks would require order $N^2$ pairwise links, which scales poorly. Hierarchical and direct interconnection arrangements allow reachability without every network connecting directly to every other network.
A_ZH: 接入 ISP 连接终端用户，这些网络再通过转接运营商、对等互联、互联网交换点等方式互连。若 $N$ 个接入网两两直接连接，需要数量级为 $N^2$ 的链路，扩展性差。层次连接与直接互联相结合，可在无需全部两两直连时实现可达性。
MEDIA: chapter1-slide-42.png

@@ N023 | 02-switching | learn | N1:37-42
Q_EN: What are transit, peering and an Internet exchange point (IXP)?
Q_ZH: Transit、peering 和互联网交换点 IXP 分别是什么？
A_EN: Transit is a customer–provider arrangement that offers connectivity through another network. Peering is an agreement for networks to exchange relevant traffic directly; its commercial terms vary. An IXP provides infrastructure where multiple networks can interconnect. These are organizational and economic relationships as well as technical ones, so the Internet is not a single centrally owned network.
A_ZH: Transit 是通过其他网络获得连接的客户—提供商安排；peering 是网络间直接交换约定流量的互联关系，商业条款并不总相同；IXP 提供多网互连的设施。它们既是技术关系，也是组织与经济关系，因此互联网不是由一个中心统一拥有的单一网络。

@@ N024 | 02-switching | learn | N1:41-42
Q_EN: Why do large content providers build their own networks?
Q_ZH: 大型内容提供商为什么建设自己的网络？
A_EN: They can connect data centers and bring content closer to users, gaining more control over performance and interconnection costs. Some traffic can bypass traditional transit hierarchies through direct connections. This changes paths and bottlenecks but does not remove the need for access networks. The lecture's named companies and ISP examples illustrate roles, rather than a current exhaustive market map.
A_ZH: 自建网络可连接数据中心、让内容更靠近用户，并更好地控制性能与互联成本。部分流量通过直连绕过传统转接层级。这改变路径和瓶颈，但不消除接入网的作用。课件中的公司与 ISP 名称用于说明角色，不是当前市场的完整名单。

@@ N025 | 03-performance | learn | N1:44-46
Q_EN: What are the four components of nodal delay?
Q_ZH: 节点时延的四个组成部分是什么？
A_EN: $d_{nodal}=d_{proc}+d_{queue}+d_{trans}+d_{prop}$. Processing inspects headers and performs local work; queueing waits for the output link; transmission puts all packet bits onto the link; propagation moves bits through the medium. Different terms depend on different quantities, so identify the bottleneck before trying to reduce delay.
A_ZH: $d_{nodal}=d_{proc}+d_{queue}+d_{trans}+d_{prop}$。处理时延用于检查首部等本地操作；排队时延是等待输出链路；传输时延是把分组全部比特送上链路；传播时延是比特在介质中移动。各项依赖的量不同，降低时延前应先找主导项。
MEDIA: chapter1-slide-45.png

@@ N026 | 03-performance | learn | N1:25,46
Q_EN: How do I calculate transmission delay?
Q_ZH: 怎样计算传输时延？
A_EN: $d_{trans}=L/R$, where $L$ is packet length in bits and $R$ is link rate in bit/s. Convert bytes to bits first: 1 byte = 8 bits. A 1,500-byte packet over a 2 Mbps link takes $12000/(2\times10^6)=0.006$ s = 6 ms to serialize. This is not yet the full end-to-end delay.
A_ZH: $d_{trans}=L/R$，$L$ 用比特，$R$ 用 bit/s。先把字节乘 8 转为比特。1,500 字节分组经过 2 Mbps 链路的串行化时间为 $12000/(2\times10^6)=0.006$ 秒，即 6 毫秒。这还不是完整端到端时延。

@@ N027 | 03-performance | learn | N1:46
Q_EN: How do I calculate propagation delay?
Q_ZH: 怎样计算传播时延？
A_EN: $d_{prop}=d/s$, with distance $d$ in meters and propagation speed $s$ in meters per second. A 1,000 km link at $2\times10^8$ m/s gives $10^6/(2\times10^8)=0.005$ s = 5 ms. Packet length and link bit rate do not appear in this term. Use total traveled path length, not an unrelated geographic distance.
A_ZH: $d_{prop}=d/s$，距离 $d$ 用米、传播速度 $s$ 用米/秒。1,000 千米链路、速度 $2\times10^8$ 米/秒时，传播时延为 $10^6/(2\times10^8)=0.005$ 秒，即 5 毫秒。这一项不含分组长度和比特率，应使用真实传播路径长度。
MEDIA: chapter1-slide-46.png

@@ N028 | 03-performance | worked | N1:45-46
Q_EN: A 1,500-byte packet crosses one 2 Mbps, 1,000 km link at $2\times10^8$ m/s. When does its last bit arrive?
Q_ZH: 1,500 字节分组经过一条 2 Mbps、1,000 千米、传播速度 $2\times10^8$ 米/秒的链路，最后一比特何时到达？
A_EN: Starting when transmission begins and ignoring processing/queueing, serialization is 6 ms and propagation is 5 ms. The last bit arrives after $6+5=11$ ms. The first bit arrives after about 5 ms. “First bit arrives” and “whole packet arrives” are different completion events, so state which one the question asks for.
A_ZH: 从开始发送计时，忽略处理和排队，串行化 6 毫秒、传播 5 毫秒，所以最后一比特在 $6+5=11$ 毫秒后到达。第一比特约在 5 毫秒后到达。“第一比特到达”和“整个分组到齐”是不同完成事件，解题前须明确目标。

@@ N029 | 03-performance | learn | N1:25-27,45-46
Q_EN: One packet of L bits follows N store-and-forward links. Link i has rate R_i bit/s, length d_i m and propagation speed s_i m/s. How do you combine these with processing and queueing delays to find its complete arrival time?
Q_ZH: L 比特分组经过 N 条存储转发链路。第 i 条链路速率为 R_i 比特/秒，长度为 d_i 米，传播速度为 s_i 米/秒。怎样加上传输、传播、处理与排队时延，求整个分组到达所需的时间？
A_EN: Use $D=\sum_{i=1}^N(L/R_i+d_i/s_i)+\sum_v(d_{proc,v}+d_{queue,v})$ seconds. The first sum counts every link; v indexes nodes with included processing or queueing, also in seconds. Count source/destination processing only if specified. A simple N-link path has N−1 intermediate routers. This is one packet, not a packet train.
A_ZH: 总时间为 $D=\sum_{i=1}^N(L/R_i+d_i/s_i)+\sum_v(d_{proc,v}+d_{queue,v})$ 秒。第一项逐链路计数；v 遍历题设纳入处理或排队的节点，其时延也以秒计。源端、目的端处理仅在题设要求时加入。简单路径的 N 条链路有 N−1 个中间路由器。本式针对单个分组。

@@ N030 | 03-performance | learn | N1:26;HT1:1b
Q_EN: Why does pipelining make multiple-packet completion faster than sending each packet end to end separately?
Q_ZH: 为什么流水线比逐个分组完全走到终点后再发下一个更快？
A_EN: While packet 1 uses link 2, link 1 can send packet 2. For P packets of L bits crossing N links, each at R bit/s, completion takes $D=(N+P-1)L/R$ seconds. The first packet needs $NL/R$; each later packet adds $L/R$. This model assumes store-and-forward, continuous sending, and no propagation, processing, queueing or cross traffic.
A_ZH: 分组 1 使用链路 2 时，链路 1 可发分组 2。P 个分组每个 L 比特，经过 N 条速率均为 R 比特/秒的链路，总完成时间为 $D=(N+P-1)L/R$ 秒。首个分组需 $NL/R$，此后每个再增加 $L/R$。模型假设存储转发、连续发送，并忽略传播、处理、排队与交叉流量。

@@ N031 | 03-performance | classroom | N1:47
Q_EN: In the caravan analogy, ten cars require 12 s each at a tollbooth and travel 100 km at 100 km/h. When has the last car reached the next booth?
Q_ZH: 车队类比中，10 辆车每辆过收费站需 12 秒，再以 100 千米/小时行驶 100 千米，最后一辆何时到下站？
A_EN: Serial service for all cars takes $10\times12=120$ s = 2 min. The last car then travels for 60 min, giving 62 min from the start of the first service. The analogy separates putting the whole packet onto the link from propagation. Earlier cars can already be traveling while later cars are still being served.
A_ZH: 全部车辆依次接受服务需 $10\times12=120$ 秒，即 2 分钟。最后一辆再行驶 60 分钟，因此从第一辆开始服务计时，共 62 分钟。这个类比区分把整个分组送上链路和传播。后面车辆还在收费时，前面的车辆已经可以行驶。
MEDIA: chapter1-slide-47.png

@@ N032 | 03-performance | classroom | N1:48
Q_EN: Ten cars queue at a tollbooth at time zero. Service takes one minute per car, then each travels 100 km at 1,000 km/h. Can the first car reach the next booth before the last leaves the first booth?
Q_ZH: 十辆车在零时刻排队过收费站，每车服务一分钟，随后以 1,000 千米/小时行驶 100 千米。第一辆能否在最后一辆离开首站前到达下站？
A_EN: Travel takes 6 min. The first car leaves at 1 min and arrives at 7 min, while the tenth leaves at 10 min. Yes: the first arrives before the last leaves. The tenth arrives at 16 min. Likewise, the first bit of a packet can reach the next node before the last bit has entered the link.
A_ZH: 行驶需 6 分钟。第一辆在第 1 分钟离开、第 7 分钟到达，第十辆则在第 10 分钟才离开。因此可以。第十辆在第 16 分钟到达。类似地，一个分组的第一比特可能在最后一比特进入链路前，就已到达下一节点。
MEDIA: chapter1-slide-48.png

@@ N033 | 03-performance | learn | N1:49
Q_EN: What is traffic intensity $La/R$?
Q_ZH: 什么是流量强度 $La/R$？
A_EN: Let $L$ be average packet length in bits, $a$ the average arrival rate in packets/s, and $R$ the service rate in bit/s. Then $\rho=La/R$ compares mean incoming work with capacity. Values near 1 leave little spare capacity for bursts. $\rho<1$ is a basic stability condition in common ideal queue models, not a guarantee of zero waiting.
A_ZH: 设 $L$ 为平均分组比特数，$a$ 为平均到达率（分组/秒），$R$ 为服务速率（比特/秒），则 $\rho=La/R$ 比较平均输入工作量与容量。接近 1 时，留给突发的余量很小。在常见理想队列模型中，$\rho<1$ 是基本稳定条件，不保证等待时间为零。
MEDIA: chapter1-slide-49.png

@@ N034 | 03-performance | worked | N1:49
Q_EN: Packets average 1,000 bytes, arrive at 100 packets/s, and use a 1 Mbps link. What is traffic intensity?
Q_ZH: 平均分组 1,000 字节、每秒到达 100 个、链路 1 Mbps，流量强度是多少？
A_EN: Convert length to 8,000 bits. Offered work is $8000\times100=800000$ bit/s, so $\rho=0.8$. The link is loaded to 80% on average. This does not mean every packet waits for exactly 20% of its transmission time; a waiting-time calculation needs additional assumptions about arrival and service variability.
A_ZH: 长度先转成 8,000 比特，输入工作量为 $8000\times100=800000$ 比特/秒，因此 $\rho=0.8$，即平均负载 80%。这不意味着每个分组都等待其传输时间的 20%；计算等待时间还需要到达和服务波动等额外假设。

@@ N035 | 03-performance | learn | N1:49,52
Q_EN: What happens as load approaches or exceeds capacity, and how does a finite buffer change the story?
Q_ZH: 负载接近或超过容量时会怎样？有限缓冲区有什么影响？
A_EN: In common random-arrival models with unlimited buffering, mean queueing delay can grow sharply as load approaches capacity, and sustained overload prevents a stable finite backlog. Real buffers are finite: they fill and then drop packets rather than storing an infinite queue. Thus low loss and low delay are different goals, and extra buffering does not increase link capacity.
A_ZH: 常见随机到达、无限缓冲模型中，负载接近容量时平均排队时延可能急剧增加，持续过载则无法保持有限稳定积压。真实缓冲区有限，会在装满后丢包，而不是形成无限队列。因此低丢包与低时延是不同目标，增加缓冲区不会增加链路容量。

@@ N036 | 03-performance | learn | N1:50-52
Q_EN: What does traceroute measure, and why are its hop values not one-way link delays?
Q_ZH: traceroute 测什么？为什么每跳数值不是单向链路时延？
A_EN: Traceroute uses probes with increasing hop limits and observes replies from successive routers. Each displayed time is a round-trip measurement from the source to a responding hop and back, including processing and potentially different return paths. An asterisk means no reply was received before timeout; it does not by itself prove that ordinary forwarded traffic was lost.
A_ZH: Traceroute 用逐步增加跳数限制的探测包，观察沿途路由器回复。每个时间是源端到该回复节点再返回的往返测量，含处理影响，返回路径也可能不同。星号表示超时前没有收到回复，不能仅凭它断定普通转发流量发生了丢失。

@@ N037 | 03-performance | learn | N1:53-54
Q_EN: What is throughput, and how does a bottleneck limit it?
Q_ZH: 什么是吞吐量？瓶颈怎样限制它？
A_EN: Throughput is the delivered data rate, measured over an instant or interval. In an ideal single-flow path with link rates $R_1,\ldots,R_N$ and no other limiting factors, sustained throughput cannot exceed $\min_i R_i$. Increasing an already faster non-bottleneck link may not improve the transfer. Actual application throughput can also be reduced by overhead, sharing and protocol behavior.
A_ZH: 吞吐量是实际交付数据的速率，可按瞬时或某段时间测量。理想单流路径的链路速率为 $R_1,\ldots,R_N$，无其他限制时，持续吞吐量不超过 $\min_i R_i$。提升已经较快的非瓶颈链路可能无效。协议开销、共享和协议行为也会降低实际应用吞吐量。
MEDIA: chapter1-slide-54.png

@@ N038 | 03-performance | classroom | N1:55
Q_EN: Ten flows share a core link of rate $R$. What is each flow's ideal throughput if its server and client links have rates $R_s$ and $R_c$?
Q_ZH: 10 条流共享速率 $R$ 的核心链路，单流服务器和客户端链路速率为 $R_s$、$R_c$，理想吞吐量是多少？
A_EN: Under the slide's equal-sharing assumption, each flow is limited by $\min(R_s,R_c,R/10)$. For $R_s=20$ Mbps, $R_c=10$ Mbps and $R=50$ Mbps, the result is 5 Mbps. $R/10$ is an assumed fair share, not a universal promise: inactive flows, competing paths and allocation policies can change it.
A_ZH: 在幻灯片的均分假设下，每条流受 $\min(R_s,R_c,R/10)$ 限制。例如 $R_s=20$ Mbps、$R_c=10$ Mbps、$R=50$ Mbps，则为 5 Mbps。$R/10$ 是假设的公平份额，不是普遍保证；流是否活跃、其他路径和分配策略都可能改变结果。
MEDIA: chapter1-slide-55.png

@@ N039 | 03-performance | check | N1:45-55
Q_EN: Can a high-throughput path still feel slow for an interactive application?
Q_ZH: 高吞吐量路径为什么仍可能让交互应用感觉很慢？
A_EN: Yes. A path may transfer large files quickly once data are flowing but have a large propagation delay or queueing delay before responses arrive. Interactive tasks often depend on round-trip time and delay variation, while bulk transfers emphasize sustained throughput. Describe latency, throughput and loss separately when diagnosing a network problem.
A_ZH: 数据开始流动后，路径可能很快传完大文件，但响应到达前仍有很大的传播或排队时延。交互任务经常依赖往返时间和时延波动，批量传输更重视持续吞吐量。诊断网络问题时，应分别描述时延、吞吐量与丢包。

@@ N040 | 03-performance | check | N1:25-55
Q_EN: What checklist prevents common network calculation mistakes?
Q_ZH: 哪些检查能避免常见网络计算错误？
A_EN: Draw the path; count links and routers; convert bytes to bits and kilometers to meters; name the completion event; list ignored delays; decide whether forwarding is store-and-forward; and distinguish one packet from a packet train. Finish with units and a plausibility check. For example, increasing distance should affect propagation, while increasing packet size should affect serialization.
A_ZH: 先画路径，数清链路与路由器，把字节转比特、千米转米，明确完成事件，列出忽略的时延，确认是否存储转发，并区分单分组与分组流水线。最后写单位并检查合理性。例如距离增加应影响传播，分组变大应影响串行化。

@@ N041 | 04-layering | learn | N1:57-61
Q_EN: Why organize networking functions into layers?
Q_ZH: 为什么把网络功能组织成不同层？
A_EN: Layering divides a complex system into modules with defined services and interfaces. A layer uses the service below and offers a service above, so implementations can change without redesigning everything when interfaces remain compatible. The cost can include overhead and duplicated functions. A layer name identifies a responsibility, not necessarily a separate physical device.
A_ZH: 分层把复杂系统拆成具有明确服务和接口的模块。每层使用下层服务、向上层提供服务；接口兼容时，可改变实现而不重做整个系统。代价可能包括额外开销和功能重复。层的名字表示职责，并不一定对应独立物理设备。

@@ N042 | 04-layering | learn | N1:61
Q_EN: Name the five Internet protocol layers from top to bottom and their main roles.
Q_ZH: 自上而下列出互联网五层，并说明主要职责。
A_EN: Application supports application protocols; transport provides process-to-process communication; network delivers packets across interconnected networks; link transfers frames across a local link; physical transmits signals representing bits. Remember the order: application, transport, network, link, physical. For example, HTTP, TCP, IP, Ethernet and its physical signaling fit these respective roles in one common stack.
A_ZH: 应用层支持应用协议；传输层提供进程间通信；网络层跨互联网络传递分组；链路层在本地链路上传帧；物理层传递表示比特的信号。顺序是应用、传输、网络、链路、物理。常见协议栈中的 HTTP、TCP、IP、Ethernet 及其物理信号可对应这些职责。
MEDIA: chapter1-slide-61.png

@@ N043 | 04-layering | learn | N1:62
Q_EN: How does the seven-layer OSI model relate to the lecture's five-layer stack?
Q_ZH: OSI 七层模型与课堂五层模型怎样对应？
A_EN: OSI includes application, presentation, session, transport, network, data link and physical layers. The five-layer Internet model does not show separate presentation and session layers; their functions may be handled by applications or libraries when needed. The two models are ways of organizing responsibilities, not evidence that Internet software can never perform presentation or session functions.
A_ZH: OSI 包含应用、表示、会话、传输、网络、数据链路和物理层。互联网五层模型不单列表示与会话层，必要功能可由应用或库实现。两种模型是职责划分方式，并不意味着互联网软件不能进行表示处理或会话管理。

@@ N044 | 04-layering | learn | N1:63-65
Q_EN: What is encapsulation, and what happens at the receiver?
Q_ZH: 什么是封装？接收端会发生什么？
A_EN: A layer treats upper-layer data as payload and adds its own control information, usually a header and sometimes a trailer. An application message becomes a transport segment, an IP datagram and a link frame, then bits. The receiver interprets and removes corresponding control information as data move upward. Headers belong to specific layers and answer different questions.
A_ZH: 一层把上层数据当载荷，加入本层控制信息，通常是首部，有时还包括尾部。应用消息依次形成传输层报文段、IP 数据报和链路帧，最后变成比特。接收端向上传递时解释并去掉相应控制信息。不同层首部负责回答不同问题。
MEDIA: chapter1-slide-64.png

@@ N045 | 04-layering | learn | N1:64-65
Q_EN: Which layers do hosts, routers and ordinary link-layer switches usually process?
Q_ZH: 主机、路由器和普通链路层交换机通常处理哪些层？
A_EN: Hosts implement the full stack for their applications. An ordinary router forwards using network-layer information and also processes the link/physical layers on each interface. A basic link-layer switch forwards frames using link-layer information. This is the introductory model; devices can have extra functions. Do not assume every router runs the destination's HTTP application.
A_ZH: 主机为应用实现完整协议栈。普通路由器依据网络层信息转发，也处理各接口的链路层与物理层。基本链路层交换机依据链路层信息转发帧。这是入门模型，实际设备可有额外功能。不能假定每个路由器都运行目的端的 HTTP 应用。

@@ N046 | 04-layering | worked | N1:63-65
Q_EN: If an application has 1,000 bytes and three layers each add a 20-byte header, what fraction of the final size is payload?
Q_ZH: 应用数据 1,000 字节，三层各加 20 字节首部，最终数据中载荷占比是多少？
A_EN: Total size is $1000+3\times20=1060$ bytes, so payload efficiency is $1000/1060\approx94.34\%$. This simplified example ignores trailers, framing gaps and retransmissions. If $R$ is the wire bit rate, application goodput can be below $R$ even without congestion because control information also uses capacity.
A_ZH: 总大小为 $1000+3\times20=1060$ 字节，载荷效率为 $1000/1060\approx94.34\%$。简化例子忽略尾部、帧间隔和重传。即使没有拥塞，应用有效吞吐量仍可能低于线速 $R$，因为控制信息也占容量。

@@ N047 | 04-layering | learn | N1:67-68
Q_EN: What are malware, a virus, a worm and a botnet in the lecture's security overview?
Q_ZH: 在课堂安全概览中，恶意软件、病毒、蠕虫和僵尸网络是什么？
A_EN: Malware is software with harmful behavior. The lecture distinguishes viruses that spread through infected objects and execution from worms that can spread automatically through vulnerable systems. A botnet is a group of compromised machines controlled together, potentially used to generate abusive traffic. These are conceptual threat categories; focus on entry points, propagation and defense rather than memorizing one historical example.
A_ZH: 恶意软件指具有有害行为的软件。课件区分通过受感染对象及其执行传播的病毒，以及可利用脆弱系统自动传播的蠕虫。僵尸网络是被统一控制的一组失陷机器，可能用于产生恶意流量。学习时关注入口、传播与防护，而不只背一个历史例子。

@@ N048 | 04-layering | learn | N1:69
Q_EN: What is denial of service, and how does distributed denial of service differ?
Q_ZH: 什么是拒绝服务？分布式拒绝服务有何不同？
A_EN: Denial of service makes a resource unavailable or less usable to legitimate users by exhausting capacity or other resources. A distributed attack uses many sources, making simple single-source filtering less effective. The resource may be bandwidth, connection state or server computation. More link capacity alone may not solve an application-computation bottleneck.
A_ZH: 拒绝服务通过耗尽容量或其他资源，使合法用户无法或难以使用服务。分布式攻击来自多个源，使简单封禁单一来源不够有效。受耗尽的资源可能是带宽、连接状态或服务器计算。若瓶颈在应用计算，仅增加链路容量未必解决问题。

@@ N049 | 04-layering | learn | N1:70-71
Q_EN: How do packet sniffing and IP spoofing differ?
Q_ZH: 分组嗅探与 IP 伪造有什么区别？
A_EN: Sniffing observes or records traffic visible to an interface. IP spoofing sends a packet with a false source IP address. Sniffing threatens confidentiality when readable sensitive data are exposed; spoofing undermines assumptions based only on a claimed source address. Encryption and authentication address different parts of these risks; a source IP field alone is not proof of identity.
A_ZH: 嗅探是观察或记录接口可见的流量；IP 伪造是发送带虚假源 IP 的分组。若敏感数据以可读形式暴露，嗅探威胁机密性；伪造则破坏仅凭声明的源地址建立的信任。加密与认证分别应对不同问题，源 IP 字段本身不是身份证明。

@@ N050 | 04-layering | learn | N1:73-77
Q_EN: What is the useful conceptual timeline of Internet history in Chapter 1?
Q_ZH: 第 1 章互联网历史中，值得掌握的概念主线是什么？
A_EN: Packet-switching research preceded early ARPANET deployment; internetworking connected heterogeneous networks; TCP/IP adoption supported a common architecture; the Web helped popularize Internet applications; broadband, mobile access and content-provider networks expanded usage. Use the timeline to explain architectural evolution. Device counts and market examples labeled with old years are historical data, not current statistics.
A_ZH: 分组交换研究先于早期 ARPANET 部署；网络互联把异构网络连起来；TCP/IP 的采用支持共同架构；Web 推动互联网应用普及；宽带、移动接入和内容商网络继续扩大使用。应借时间线理解架构演化。带旧年份的设备数量与市场例子属于历史数据，不是当前统计。

@@ N051 | 04-layering | check | N1:74
Q_EN: What do best effort, autonomy and decentralized control mean in the Internet's design principles?
Q_ZH: 互联网设计原则中的尽力而为、自治和分散控制是什么意思？
A_EN: Best effort means the basic network delivery service does not promise successful delivery or a fixed delay. Autonomy lets interconnected networks retain their internal organization. Decentralized control avoids requiring one central controller for every routing decision. Higher layers can add functions such as reliable delivery, but that does not turn the underlying best-effort service into a guaranteed-delay network.
A_ZH: 尽力而为表示基础网络交付服务不承诺一定送达或固定时延；自治允许互联网络保留内部组织方式；分散控制避免每次路由决策都依赖一个中央控制者。更高层可以增加可靠交付等功能，但这并不使底层尽力而为网络自动具有保证时延。

@@ N052 | 05-applications | learn | N2:4-5
Q_EN: Where do network applications run, and why does that matter for developing a new application?
Q_ZH: 网络应用运行在哪里？这对开发新应用有什么意义？
A_EN: Application programs mainly run on end systems and exchange messages using network services. In the usual Internet model, creating a new application does not require installing its application logic in every core router. This separation supports rapid application development. The application must still work within the reliability, delay and throughput properties of its transport and network services.
A_ZH: 应用程序主要运行在端系统上，使用网络服务交换消息。通常创建新互联网应用，不需要把应用逻辑安装到所有核心路由器。这种分离支持快速开发。应用仍须适应传输与网络服务提供的可靠性、时延和吞吐量条件。

@@ N053 | 05-applications | learn | N2:6
Q_EN: What characterizes a client–server architecture?
Q_ZH: 客户端—服务器架构有什么特征？
A_EN: A server provides a service and is typically continuously reachable at a known address; clients initiate requests and may connect intermittently. Clients usually communicate through the server rather than directly with every other client. Centralization simplifies service management but can create capacity and availability challenges. Large services may distribute the server role across many machines.
A_ZH: 服务器提供服务，通常持续在线并具有已知可达地址；客户端发起请求，可能间歇连接。客户端通常通过服务器通信，而不与所有其他客户端直连。集中化方便管理，但带来容量与可用性挑战。大型服务可用多台机器共同承担服务器角色。
MEDIA: chapter2-slide-6.png

@@ N054 | 05-applications | learn | N2:7
Q_EN: What characterizes a peer-to-peer architecture?
Q_ZH: 点对点 P2P 架构有什么特征？
A_EN: Peers communicate directly and may both request and provide service. As peers join, they can add demand and service capacity, creating potential self-scalability. Peers may be intermittently connected or change addresses, complicating discovery, coordination and security. P2P is an application architecture; it does not mean packets avoid Internet routers.
A_ZH: 对等节点直接通信，既可请求服务，也可提供服务。节点加入时同时增加需求与服务能力，因此具有潜在自扩展性。但节点可能间歇在线或地址变化，使发现、协调与安全更复杂。P2P 是应用架构，不代表分组不经过互联网路由器。
MEDIA: chapter2-slide-7.png

@@ N055 | 05-applications | check | N2:6-8
Q_EN: Can the same machine be both a client and a server?
Q_ZH: 同一台机器能同时是客户端和服务器吗？
A_EN: Yes. Client and server describe process roles in an interaction, not permanent hardware categories. A machine may request one service while providing another; P2P peers commonly perform both roles. In a given exchange, the initiating process is conventionally the client and the process waiting to respond is the server.
A_ZH: 可以。客户端与服务器描述交互中的进程角色，不是固定硬件类别。一台机器可一边请求某服务，一边提供另一服务；P2P 节点常兼任两者。在某次交互中，主动发起的进程通常称客户端，等待并响应的进程称服务器。

@@ N056 | 05-applications | learn | N2:8-10
Q_EN: What is a process, and how do processes on different hosts communicate?
Q_ZH: 什么是进程？不同主机上的进程怎样通信？
A_EN: A process is a running program. Processes on one host can use operating-system interprocess communication; processes on different hosts exchange messages across the network. The application defines message meaning, while transport and lower layers carry the data. A network application can involve many communicating processes rather than one program on one machine.
A_ZH: 进程是运行中的程序。同机进程可使用操作系统的进程间通信，不同主机的进程通过网络交换消息。应用定义消息含义，传输及更低层负责承载数据。网络应用可由多个通信进程组成，而不是一台机器上的单个程序。

@@ N057 | 05-applications | learn | N2:9-10
Q_EN: What is a socket?
Q_ZH: 什么是套接字 socket？
A_EN: A socket is an application-facing interface to transport communication, often described as a door between a process and the network service. The application writes data to and reads data from it through an API. It can choose some transport settings, but it does not directly control every router's queue or route. A socket is a software abstraction, not a physical network cable.
A_ZH: 套接字是应用访问传输通信的接口，常被比作进程与网络服务之间的门。应用通过 API 向它写数据、从它读数据。应用可选择部分传输设置，但不能直接控制所有路由器的队列与路径。套接字是软件抽象，不是物理网线。
MEDIA: chapter2-slide-9.png

@@ N058 | 05-applications | learn | N2:11
Q_EN: Why is an IP address alone insufficient to identify an application process?
Q_ZH: 为什么只有 IP 地址不足以识别应用进程？
A_EN: A host can run many network processes. An IP address identifies the network endpoint at the host/interface level; a transport port helps identify the intended application endpoint. The transport protocol also matters, so TCP port 53 and UDP port 53 are distinct endpoints. A port number is not the same as a process ID or a physical connector.
A_ZH: 一台主机可以运行很多网络进程。IP 地址在主机/接口层面定位网络端点，传输端口帮助识别目标应用端点。还需考虑传输协议，因此 TCP 的 53 端口和 UDP 的 53 端口是不同端点。端口号不是进程 ID，也不是物理插口。

@@ N059 | 05-applications | learn | N2:12
Q_EN: What must an application-layer protocol define?
Q_ZH: 应用层协议需要规定什么？
A_EN: It defines message types, syntax, semantics and rules for when messages are sent and how to respond. Syntax describes fields and formatting; semantics explains their meaning. An open specification allows independent interoperable implementations, while a proprietary protocol may have restricted documentation or control. An application's user interface is broader than its network protocol.
A_ZH: 它规定消息类型、语法、语义，以及何时发送和怎样响应。语法描述字段与格式，语义解释字段含义。开放规范便于独立实现互操作，私有协议的文档或控制可能受限制。应用的用户界面比网络协议本身涵盖更多内容。

@@ N060 | 05-applications | learn | N2:13-14
Q_EN: What four transport-service requirements should an application designer consider?
Q_ZH: 应用设计者应考虑哪四类传输服务需求？
A_EN: Reliability or data integrity, throughput, timing and security. File transfer usually needs every byte correct; interactive audio values low delay and can tolerate some loss. Some applications need a minimum useful rate, while elastic applications can adapt to available throughput. “Can tolerate some loss” does not mean loss is always harmless or unlimited.
A_ZH: 四类需求是可靠性/数据完整性、吞吐量、时间性与安全性。文件传输通常要求每个字节正确；交互音频重视低时延，能容忍部分丢失。有的应用需要最低可用速率，弹性应用则可适应可用吞吐量。“能容忍一些丢失”不表示丢失总是无害或可无限增加。
MEDIA: chapter2-slide-14.png

@@ N061 | 05-applications | learn | N2:15
Q_EN: What does TCP provide, and what does it not promise?
Q_ZH: TCP 提供什么？又不承诺什么？
A_EN: TCP provides a connection-oriented, reliable ordered byte-stream service, with flow control and congestion control. It does not guarantee a minimum throughput, a maximum delay or built-in encryption. Reliability is implemented through protocol behavior such as acknowledgment and retransmission; it does not imply the underlying IP network never loses packets or that every connection can survive every failure.
A_ZH: TCP 提供面向连接、可靠有序的字节流服务，并有流量控制和拥塞控制。它不保证最低吞吐量、最大时延，也不自带加密。可靠性通过确认、重传等协议行为实现，不代表底层 IP 从不丢包，也不代表连接能在任何故障中持续成功。

@@ N062 | 05-applications | learn | N2:15
Q_EN: What is the difference between flow control and congestion control?
Q_ZH: 流量控制与拥塞控制有什么区别？
A_EN: Flow control protects a receiver from data arriving faster than it can handle. Congestion control protects the network from excessive offered traffic. A slow receiving application and an overloaded router are different bottlenecks. TCP has both mechanisms. The current Canvas application-layer introduction covers their service roles; Extra Resources adds the historical rwnd/cwnd and congestion-control algorithms.
A_ZH: 流量控制防止接收方来不及处理到达的数据；拥塞控制防止网络承受过量流量。接收应用过慢与路由器过载是不同瓶颈，TCP 同时具有两类机制。当前 Canvas 应用层入门介绍其服务职责；Extra Resources 已补充往年的 rwnd/cwnd 与拥塞控制算法。

@@ N063 | 05-applications | learn | N2:15
Q_EN: What does UDP provide?
Q_ZH: UDP 提供什么？
A_EN: UDP provides a connectionless datagram service with limited transport machinery. It does not provide TCP-style reliable ordered delivery, flow control or congestion control by itself. Applications can add needed behavior above UDP. Choosing UDP does not create a guarantee of low latency or high throughput; network delay and application design still matter.
A_ZH: UDP 提供无连接的数据报服务，传输机制较少。它本身不提供 TCP 式的可靠有序交付、流量控制和拥塞控制，应用可以在其上补充所需行为。选择 UDP 并不会自动保证低时延或高吞吐量，网络状态与应用设计仍然重要。

@@ N064 | 05-applications | check | N2:13-16
Q_EN: Does “real-time application” automatically mean “use UDP”?
Q_ZH: “实时应用”是否就等于“必须用 UDP”？
A_EN: No. Start with requirements: delay budget, loss tolerance, message ordering, deployment support and whether the application adds recovery. UDP avoids some TCP mechanisms but also leaves more responsibility to the application. Some real-time services use transports built above UDP; others can use TCP in suitable conditions. The lecture table is a set of examples, not an absolute design law.
A_ZH: 不等于。应先看时延预算、丢失容忍、消息顺序、部署支持，以及应用是否自己恢复丢失。UDP 少了一些 TCP 机制，同时也把更多责任留给应用。有的实时服务使用 UDP 上构建的传输，有的在合适条件下使用 TCP。课堂表格是示例，不是绝对设计定律。

@@ N065 | 05-applications | learn | N2:15-17
Q_EN: Does using TCP make application data confidential?
Q_ZH: 使用 TCP 是否就能保证应用数据保密？
A_EN: No. TCP reliability and ordering do not encrypt application bytes. A secure application commonly adds a cryptographic protocol such as TLS, which can provide confidentiality, integrity and peer authentication under its security assumptions. The lecture uses the historical term SSL; current designs should be understood in terms of TLS. The detailed TLS version distinction is covered in the extension cards.
A_ZH: 不能。TCP 的可靠与有序不等于对应用字节加密。安全应用通常再使用 TLS 等密码协议，在相应安全假设下提供机密性、完整性与对端认证。课件使用了历史名称 SSL；理解现代设计时应对应到 TLS。版本区别见扩展卡。

@@ N066 | 06-http | learn | N2:19
Q_EN: What is a web page made of in the lecture's HTTP model?
Q_ZH: 在课堂 HTTP 模型中，一个网页由什么组成？
A_EN: A page usually includes a base HTML object that references other objects such as images, scripts or style sheets. Each object can be addressed by a URL. Fetching the base HTML is therefore not always enough to finish displaying the page. The browser may need to request additional objects, possibly from different servers.
A_ZH: 网页通常包括基础 HTML 对象，它引用图片、脚本或样式表等其他对象，各对象可通过 URL 定位。因此取到 HTML 并不一定代表网页已完整显示，浏览器还可能从同一或不同服务器请求额外对象。

@@ N067 | 06-http | learn | N2:19
Q_EN: In a URL, what roles do the scheme, host and path play?
Q_ZH: URL 中的 scheme、host 和 path 分别起什么作用？
A_EN: In `https://example.org/course/image.png`, `https` selects the access scheme, `example.org` names the host, and `/course/image.png` identifies a resource path in that service. A host name is not the same thing as an IP address. A URL identifies a resource; it does not imply the entire resource is contained in one network packet.
A_ZH: 在 `https://example.org/course/image.png` 中，`https` 指定访问方案，`example.org` 是主机名，`/course/image.png` 是服务中的资源路径。主机名不等同于 IP 地址。URL 标识资源，不代表整个资源能放进一个网络分组。

@@ N068 | 06-http | learn | N2:20-21
Q_EN: How does the introductory HTTP request–response exchange work?
Q_ZH: 入门 HTTP 请求—响应交换如何工作？
A_EN: A browser acts as an HTTP client and sends a request for a resource; a web server sends an HTTP response containing status information and possibly the requested representation. The lecture introduces this through a TCP connection and conventional HTTP port 80. The application messages and the transport connection are different layers of the exchange.
A_ZH: 浏览器作为 HTTP 客户端请求资源，Web 服务器发送 HTTP 响应，其中包含状态信息，也可能包含请求资源的表示。课件通过 TCP 连接和传统 HTTP 的 80 端口引入这个过程。应用消息与承载它的传输连接属于不同层面。
MEDIA: chapter2-slide-20.png

@@ N069 | 06-http | learn | N2:22
Q_EN: What does “HTTP is stateless” mean?
Q_ZH: “HTTP 无状态”是什么意思？
A_EN: In the lecture's basic model, the protocol does not require the server to remember a history of prior requests to interpret every new request. It does not mean a server stores no files, a TCP connection has no state, or a website cannot implement login sessions. Applications can add state-management mechanisms above the basic request–response semantics.
A_ZH: 在课堂基本模型中，协议不要求服务器必须记住之前请求的历史，才能解释每个新请求。这不等于服务器不保存文件、TCP 连接没有状态，或网站不能实现登录会话。应用可在基本请求—响应语义之上增加状态管理机制。

@@ N071 | 07-exercises | classroom | NT1:1;NT1S:3;HT1:1a
Q_EN: Tutorial 1 (2026A) Q1a: one L-bit packet crosses two store-and-forward links of rates $R_1,R_2$ bit/s. Ignore all other delays. From the start of transmission, how long until its last bit reaches the destination?
Q_ZH: 本学期 Tutorial 1 Q1a：L 比特分组经过两条存储转发链路，速率为 $R_1,R_2$ 比特/秒。忽略其他时延，从开始发送到最后一比特到达目的地需多久？
A_EN: The switch first receives all $L$ bits in $L/R_1$, then sends them in $L/R_2$. Total time is $D=L/R_1+L/R_2$. Do not replace this by $L/\min(R_1,R_2)$: the bottleneck rate describes sustained throughput, while this question asks for the first complete packet's latency.
A_ZH: 交换设备先用 $L/R_1$ 收齐，再用 $L/R_2$ 发完，总时间为 $D=L/R_1+L/R_2$。不能替换为 $L/\min(R_1,R_2)$：瓶颈速率描述持续吞吐量，这里问的是首个完整分组的时延。


@@ N072 | 07-exercises | classroom | NT1:1;NT1S:4;NQA:3;HT1:1b
Q_EN: Tutorial 1 (2026A) Q1b: three packets, each L bits, are sent back-to-back across two store-and-forward links, each of rate R bit/s. Ignore all other delays. From the start of transmission, how long until all three arrive completely?
Q_ZH: 本学期 Tutorial 1 Q1b：三个分组各 L 比特，连续发送，经过两条速率均为 R 比特/秒的存储转发链路。忽略其他时延，从开始发送到三个分组全部到齐需多久？
A_EN: Let $t=L/R$. During successive intervals, link 1 sends packets 1, 2 and 3; link 2 sends them one interval later. Arrival times are $2t,3t,4t$, so completion is $4L/R$. Summing $2L/R$ separately for all three gives $6L/R$ and incorrectly forbids pipelining.
A_ZH: 令 $t=L/R$。链路 1 依次发送分组 1、2、3；链路 2 比它晚一个时间段依次发送。到达时刻为 $2t,3t,4t$，所以完成需 $4L/R$。把三次 $2L/R$ 相加得到 $6L/R$，错误地禁止了流水线重叠。


@@ N073 | 07-exercises | classroom | NT1:2;NT1S:6;HT1:2a
Q_EN: Tutorial 1 (2026A) Q2a: a square A–B–C–D–A has four circuits on each edge. What is the maximum number of simultaneous connections if endpoints are unrestricted?
Q_ZH: 本学期 Tutorial 1 Q2a：方环 A–B–C–D–A 每条边有 4 条电路，端点不受限时最多多少个同时连接？
A_EN: Use four one-edge connections on each of the four edges, giving $4\times4=16$ connections. This achieves the upper bound because every connection consumes at least one edge circuit and there are 16 total. Connections between opposite corners consume two edges and would use more of the same finite resources per connection.
A_ZH: 每条边放 4 个只走一条边的连接，四条边共 $4\times4=16$ 个。这达到上界，因为每个连接至少消耗一条边上的电路，总共只有 16 个边电路资源。对角顶点之间的连接需走两条边，每个连接消耗更多资源。
MEDIA_FRONT: square-circuits-teaching.png

@@ N074 | 07-exercises | classroom | NT1:2;NT1S:6;HT1:2b
Q_EN: A square network A–B–C–D–A has four circuits on every edge. What is the maximum number of simultaneous connections from A to opposite corner C?
Q_ZH: 方环网络 A–B–C–D–A 的每条边有四条电路。从 A 到对角 C 最多能同时建立多少个连接？
A_EN: There are two edge-disjoint two-hop paths: A–B–C and A–D–C. Each supports four connections, so eight are feasible. The two edges leaving A together have only eight circuits, giving an upper bound of eight. Showing both a construction and a bound proves the maximum.
A_ZH: 有两条边不重合的两跳路径：A–B–C 与 A–D–C，每条支持 4 个，因此可实现 8 个。A 发出的两条边合计也只有 8 条电路，构成上界。既给出可行安排又给出上界，就证明了最大值。
MEDIA_FRONT: square-circuits-teaching.png

@@ N075 | 07-exercises | classroom | NT1:2;NT1S:7;HT1:2c
Q_EN: A square A–B–C–D–A has four circuits per edge. Can it simultaneously carry four A–C and four B–D connections?
Q_ZH: 方环 A–B–C–D–A 每条边 4 条电路，能否同时承载 4 个 A–C 连接和 4 个 B–D 连接？
A_EN: Yes. Split A–C traffic as two via B and two via D. Split B–D traffic as two via A and two via C. Each edge then carries exactly four connections, within its capacity. Routing all connections for a pair along one side can falsely make the demand look infeasible; count use on each individual edge.
A_ZH: 可以。A–C 中 2 个经 B、2 个经 D；B–D 中 2 个经 A、2 个经 C。这样每条边恰好承载 4 个连接，不超容量。若把某对端点全部流量压在同一侧，可能误判不可行；应逐边统计占用。
MEDIA_FRONT: square-circuits-teaching.png

@@ N076 | 07-exercises | classroom | NT1:2-3;NT1S:9;HT1:3
Q_EN: Tutorial 1 (2026A) Q3: send 160,000 bits on a 1.536 Mbps link divided into 12 equal FDM circuits; setup takes 600 ms. Find total time.
Q_ZH: 本学期 Tutorial 1 Q3：1.536 Mbps 链路均分为 12 条 FDM 电路，发送 160,000 比特，建立连接需 600 毫秒，总时间是多少？
A_EN: Each circuit gets $1.536\times10^6/12=128000$ bit/s. Data transmission takes $160000/128000=1.25$ s. Add setup: $D=0.6+1.25=1.85$ s, under the question's ignored propagation and other delays. Using the full 1.536 Mbps for one reserved circuit would overestimate its available rate.
A_ZH: 每条电路速率为 $1.536\times10^6/12=128000$ 比特/秒，数据发送需 $160000/128000=1.25$ 秒。加建立时间，总共 $D=0.6+1.25=1.85$ 秒，这里按题意忽略传播等时延。若对单条电路使用全链路 1.536 Mbps，就高估了可用速率。


@@ N077 | 07-exercises | classroom | NT1:3;NT1S:10;HT1:4a-4b
Q_EN: Tutorial 1 (2026A) Q4: a 3 Mbps link serves users needing 150 kbps while active, with activity probability 0.1. How many circuits fit, and what is one user's activity probability?
Q_ZH: 本学期 Tutorial 1 Q4：3 Mbps 链路、每人活跃时需 150 kbps、活跃概率 0.1，最多多少条电路？单人活跃概率是多少？
A_EN: Fixed circuits fit $3000/150=20$ users. A given user's activity probability is the stated 0.1. These answer different questions: the first is a resource-reservation bound, the second a traffic-model parameter. Multiplying 20 by 10 does not establish a guaranteed 200-user capacity under packet switching.
A_ZH: 固定电路可容纳 $3000/150=20$ 人。某个用户的活跃概率就是给定的 0.1。两者回答不同问题：前者是资源预留上界，后者是流量模型参数。把 20 乘 10 并不能证明分组交换保证支持 200 人。


@@ N078 | 07-exercises | classroom | NT1:3;NT1S:10;HT1:4c
Q_EN: With 120 independent users each active with probability 0.1, what is the probability exactly $n$ are active?
Q_ZH: 120 个独立用户每人以 0.1 概率活跃，恰有 $n$ 人活跃的概率是多少？
A_EN: $P(K=n)=\binom{120}{n}(0.1)^n(0.9)^{120-n}$ for $n=0,\ldots,120$. The combination counts which users are active; the other terms give the probability of one such pattern. Expected active users are $E[K]=120\times0.1=12$. An overload probability requires summing the tail above capacity, not substituting the mean.
A_ZH: $P(K=n)=\binom{120}{n}(0.1)^n(0.9)^{120-n}$，其中 $n=0,\ldots,120$。组合数统计哪些用户活跃，其余项表示一种具体组合的概率。期望活跃人数为 $E[K]=120\times0.1=12$。过载概率要对超过容量的尾部求和，不能用均值直接代替。


@@ N079 | 07-exercises | classroom | NT2:1;HT2:1
Q_EN: Tutorial 2 (2026A) Q1: voice is encoded at 128 kbps into 64-byte packets, sent at 4 Mbps with 8 ms propagation. Measured from the start of packetization, when can playback of the first encoded bit start if the receiver waits for the complete packet?
Q_ZH: 本学期 Tutorial 2 Q1：语音以 128 kbps 编码，组成 64 字节分组，以 4 Mbps 发送，传播 8 毫秒。若接收端等完整分组到齐后播放，最早编码的比特从开始组包到可播放需多久？
A_EN: Packetization needs $512/128000=4$ ms; transmission needs $512/(4\times10^6)=0.128$ ms; propagation is 8 ms. Total is 12.128 ms under the whole-packet playback model. The phrase “a bit” is ambiguous: the earliest encoded bit waits about the full packetization interval, while a typical bit's average assembly wait is about half, 2 ms.
A_ZH: 组包需 $512/128000=4$ 毫秒，发送需 $512/(4\times10^6)=0.128$ 毫秒，传播为 8 毫秒。按完整分组到达后播放的模型，总共 12.128 毫秒。原题“某个比特”略有歧义：最早编码的比特约等待完整组包时间，而任意典型比特的平均组包等待约为一半，即 2 毫秒。


@@ N080 | 07-exercises | classroom | NT2:1;HT2:2a
Q_EN: Tutorial 2 (2026A) Q2a: an L-bit packet crosses three links and two store-and-forward routers. Link i has rate R_i bit/s, length d_i m and propagation speed s_i m/s. Each router adds d_proc seconds; queueing and endpoint processing are zero. Find complete-packet delay.
Q_ZH: 本学期 Tutorial 2 Q2a：L 比特分组经过三条链路和两个存储转发路由器。第 i 条链路速率 R_i 比特/秒，长度 d_i 米，传播速度 s_i 米/秒。每路由器处理 d_proc 秒，排队和端点处理为零。求整个分组到齐的时延。
A_EN: $D=\sum_{i=1}^{3}(L/R_i+d_i/s_i)+2d_{proc}$. There are three serialization terms because each link transmits the whole packet, three propagation terms, and two router-processing terms. If the problem adds source or destination processing, include those separately; do not infer them when the stated model excludes them.
A_ZH: $D=\sum_{i=1}^{3}(L/R_i+d_i/s_i)+2d_{proc}$。三条链路各发完整分组，因此有三个串行化项、三个传播项，以及两个路由处理项。若题目另加源端或目的端处理，应单独计入；模型未要求时不要自行添加。


@@ N081 | 07-exercises | classroom | NT2:1;HT2:2b
Q_EN: One packet crosses three store-and-forward links and two routers, with no queueing or endpoint processing. Use $L=1500$ bytes, each $R=2$ Mbps, $s=2.5\times10^8$ m/s, distances 5,000/4,000/1,000 km, and 3 ms processing per router. Find complete-packet delay.
Q_ZH: 一个分组经过三条存储转发链路和两个路由器，无排队与端点处理。分组 1500 字节，各链路 2 Mbps，传播速度 $2.5\times10^8$ 米/秒，距离为 5000/4000/1000 千米，每路由器处理 3 毫秒。求整个分组到齐的时延。
A_EN: Each serialization takes 6 ms, so three give 18 ms. Total distance is $10^7$ m, giving 40 ms propagation. Two routers add 6 ms. Total: $18+40+6=64$ ms. Keep all three components visible; the result is easy to miscalculate if kilometers, bytes and milliseconds are mixed without conversion.
A_ZH: 每条链路串行化 6 毫秒，三条共 18 毫秒。总距离 $10^7$ 米，传播共 40 毫秒；两个路由器再加 6 毫秒。总计 $18+40+6=64$ 毫秒。应保留分项，避免把千米、字节和毫秒不经换算直接混用。


@@ N082 | 07-exercises | classroom | NT2:2;HT2:3
Q_EN: A 1,500-byte packet crosses three 2 Mbps links with total propagation 40 ms. If routers forward each bit immediately with zero processing, what is the ideal delay?
Q_ZH: 1500 字节分组经过三条 2 Mbps 链路，总传播为 40 毫秒，路由器逐比特立即转发且处理为零，理想时延是多少？
A_EN: With all links at the same rate, serialization overlaps across links: count one $L/R=6$ ms plus total propagation of 40 ms. The result is 46 ms. This is the question's ideal cut-through model; actual forwarding may need enough header bits to choose an output, so do not apply the ideal formula to every real device without checking assumptions.
A_ZH: 各链路同速时，串行化在各链路间重叠，只计一次 $L/R=6$ 毫秒，再加总传播 40 毫秒，得 46 毫秒。这是题目的理想直通模型；真实转发可能先需要足够的首部比特来决定出口，不能无条件套用到所有设备。


@@ N083 | 07-exercises | classroom | NT2:2;HT2:4
Q_EN: A 2 Mbps output link is halfway through a 1,500-byte packet and has four more equal packets waiting. What is a newly arriving packet's queueing delay?
Q_ZH: 2 Mbps 输出链路已发送完一个 1500 字节分组的一半，队列中另有四个等长分组等待。新到分组需排队多久？
A_EN: One full serialization takes 6 ms. The new packet waits for half the current packet plus four queued packets: $(0.5+4)\times6=27$ ms, assuming FIFO and no priority changes. This is waiting until its own transmission starts; add another 6 ms if asked when its own serialization finishes.
A_ZH: 一个完整分组发送需 6 毫秒。新分组要等当前剩余半个与已排队的四个，所以 $(0.5+4)\times6=27$ 毫秒，假设先到先服务且无优先级变化。这里算到自身开始发送；若问自身发完，还要再加 6 毫秒。

@@ N084 | 07-exercises | classroom | NT2:2;HT2:4
Q_EN: Generalize queueing delay when $x$ bits of the current $L$-bit packet have already been sent and $n$ full packets are waiting.
Q_ZH: 当前 $L$ 比特分组已有 $x$ 比特发出，另有 $n$ 个完整分组等待，如何写新到分组的排队时延？
A_EN: Remaining work ahead is $(L-x)+nL$ bits, so $d_{queue}=((L-x)+nL)/R$ under FIFO. Do not include the arriving packet's own $L$ bits in queueing delay. If there is no packet in service, the residual term is zero; if packet lengths differ, sum the actual queued lengths rather than using $nL$.
A_ZH: 前面剩余工作量为 $(L-x)+nL$ 比特，因此 FIFO 下 $d_{queue}=((L-x)+nL)/R$。排队时延不包含新到分组自身的 $L$ 比特。若没有分组正在发送，残余项为零；若各分组长度不同，应累加实际长度，而不是用 $nL$。


@@ N085 | 07-exercises | classroom | NT2:3;HT2:5;N1:50-51
Q_EN: Why can a later traceroute hop show a smaller RTT than an earlier hop?
Q_ZH: 为什么 traceroute 中后面一跳的 RTT 可能比前面一跳更小？
A_EN: The probes are separate measurements, not one packet being timed cumulatively at every hop. Router reply scheduling, queueing, probe timing and return paths can differ. Therefore subtracting adjacent RTTs is not a reliable direct estimate of one link's propagation delay. Examine repeated measurements and the measurement mechanism before drawing a network-performance conclusion.
A_ZH: 各跳探测是不同测量，不是同一个分组沿途累积计时。路由器回复调度、排队、探测时刻与返回路径可能不同。因此相邻 RTT 相减不能可靠地直接估计某条链路传播时延。下结论前应看重复测量及其测量机制。


@@ N086 | 08-extension | extension | N1:46,53-55
Q_EN: What is the bandwidth–delay product, and why is its delay definition important?
Q_ZH: 什么是带宽时延积？为什么要说明采用哪种时延？
A_EN: Multiplying rate by a duration gives bits. $R\,d_{prop}$ estimates bits physically in flight along a continuously filled one-way link. $R\,RTT$ is useful when reasoning about data outstanding over a round trip. For 100 Mbps and 20 ms RTT, the latter is 2 Mbit, or 250 kB. Do not silently interchange one-way propagation delay and RTT.
A_ZH: 速率乘时间得到比特数。$R\,d_{prop}$ 估计连续填满的单向链路上正在传播的比特数；$R\,RTT$ 则用于理解一个往返期间可保持未确认的数据量。100 Mbps、RTT 为 20 毫秒时，后者为 2 Mbit，即 250 kB。不能悄悄把单向传播时延与 RTT 互换。

@@ N087 | 08-extension | extension | N2:21;H3:1-2
Q_EN: Is “HTTP always runs over TCP” correct for modern HTTP?
Q_ZH: “HTTP 永远运行在 TCP 上”对现代 HTTP 正确吗？
A_EN: No. The lecture's introductory model uses TCP, which is appropriate for conventional HTTP/1.1 and HTTP/2. HTTP/3 maps HTTP semantics onto QUIC, which runs over UDP. Therefore keep HTTP's application semantics separate from the transport mapping. In an exam question explicitly using the lecture's TCP model, solve under that stated model rather than silently replacing it with HTTP/3.
A_ZH: 不正确。课堂入门模型使用 TCP，适合传统 HTTP/1.1 和 HTTP/2；HTTP/3 将 HTTP 语义映射到运行在 UDP 上的 QUIC。因此应区分应用语义与传输映射。若试题明确采用课堂 TCP 模型，就按题设解，不应自行替换为 HTTP/3。

@@ N088 | 08-extension | extension | N2:17;TLS:1
Q_EN: How should I interpret the lecture's term SSL today?
Q_ZH: 今天应该怎样理解课件中的 SSL 这个名称？
A_EN: SSL is the historical protocol family preceding TLS. Modern secure-transport discussions should specify TLS and its version, such as TLS 1.3. TLS aims to protect communication against eavesdropping and tampering and to authenticate peers under the chosen configuration. “Uses TLS” does not prove an application has no other security bugs. Keep this terminology update separate from the lecture's basic transport-service comparison.
A_ZH: SSL 是 TLS 之前的历史协议族，讨论现代安全传输时应明确 TLS 及版本，例如 TLS 1.3。TLS 旨在防窃听、防篡改，并按配置认证对端。“使用 TLS”不代表应用没有其他安全漏洞。本卡是术语更新，与课堂基础传输服务比较分开理解。

@@ N093 | 08-extension | extension | N1:21-31,45-55
Q_EN: Give a one-minute English comparison of circuit switching and packet switching.
Q_ZH: 用一分钟英语比较电路交换与分组交换。
A_EN: “Circuit switching reserves resources for a connection, providing a predictable share but potentially wasting capacity during idle periods. Packet switching shares links among packets on demand, which suits bursty traffic through statistical multiplexing. However, simultaneous demand can create queues and loss. The choice trades reservation and predictability against efficient sharing; transmission rate, delay and traffic assumptions must be stated.” This is oral practice, not a confirmed QE question.
A_ZH: “电路交换为连接预留资源，提供可预测份额，但空闲期间可能浪费容量。分组交换按需共享链路，通过统计复用适应突发流量，但同时需求过高会产生排队和丢失。两者权衡的是预留与可预测性，以及共享效率；分析时必须说明速率、时延与流量假设。”这是口头表达训练，不是已确认 QE 考题。

@@ N094 | 08-extension | extension | N1:45-55;N2:13-15
Q_EN: A video call has enough average bandwidth but pauses unpredictably. What should I investigate before buying a faster access plan?
Q_ZH: 视频通话平均带宽足够，却不定时卡顿，升级接入套餐前应先分析什么？
A_EN: Measure delay variation, packet loss, queueing under competing traffic and local access stability; also inspect application and device load. More access bandwidth helps only if that link's capacity is the limiting factor. A remote bottleneck, bursty queue or overloaded application can persist after an upgrade. This is an AI-added diagnostic exercise applying the course's delay/throughput distinction, not a measured diagnosis of your network.
A_ZH: 先测时延波动、丢包、竞争流量下的排队和本地接入稳定性，同时检查应用与设备负载。只有接入链路容量构成瓶颈时，增加带宽才对症。远端瓶颈、突发队列或应用过载可能在升级后继续存在。这是应用时延/吞吐量区别的扩展练习，不是对你当前网络的实测诊断。

@@ N095 | 09-ch1-qa | classroom | NQA:2
Q_EN: Chapter 1 Q&A: which is not an end-system network-edge device? A PC, B smartphone, C server, D router.
Q_ZH: 第 1 章 Q&A：按端系统与核心网络的分类，哪个不属于端系统边缘设备？A 电脑，B 手机，C 服务器，D 路由器。
A_EN: D, router. PCs, phones and servers run endpoint applications; the router's role is forwarding traffic between links. A server remains an end system even when it serves many users. A home router can be physically at an access boundary, so interpret “edge device” using this question's end-system/core distinction rather than every possible industry use of the phrase.
A_ZH: 选 D。电脑、手机和服务器运行端点应用，路由器负责链路间转发。服务器即使服务很多用户，仍是端系统。家庭路由器在物理上可位于接入边界，因此本题应按端系统与核心网络的课堂分类理解“边缘设备”，而非混用所有行业定义。

@@ N096 | 09-ch1-qa | classroom | NQA:4;N1:45-49
Q_EN: Chapter 1 Q&A: which delay changes with congestion in the basic model? A processing, B queueing, C transmission, D propagation.
Q_ZH: 第 1 章 Q&A：在基础模型中，哪项时延随拥塞变化？A 处理，B 排队，C 传输，D 传播。
A_EN: B, queueing delay. With packet length $L$, link rate $R$, distance and propagation speed fixed, $L/R$ and $d/s$ stay fixed while competing packets increase the wait for service. The question models processing as a separate fixed cost. State these assumptions rather than claiming that congestion can never interact with any other real-system behavior.
A_ZH: 选 B。固定分组长度 $L$、链路速率 $R$、距离与传播速度时，$L/R$ 和 $d/s$ 不变，而竞争分组会增加等待服务的时间。本题把处理时间作为独立固定开销。应说明这些假设，而非断言真实系统中拥塞永远不影响任何其他行为。

@@ N097 | 09-ch1-qa | classroom | NQA:5
Q_EN: Chapter 1 Q&A: a 100 Mbps modem feeds a 54 Mbps Wi-Fi router. After upgrading Wi-Fi to 1 Gbps, what ideal end-to-end throughput is possible? A 100 Mbps, B 54 Mbps, C 154 Mbps, D 1 Gbps.
Q_ZH: 第 1 章 Q&A：100 Mbps 调制解调器接 54 Mbps Wi-Fi 路由器，将 Wi-Fi 升为 1 Gbps 后，理想端到端吞吐量是多少？A 100 Mbps，B 54 Mbps，C 154 Mbps，D 1 Gbps。
A_EN: A, 100 Mbps, from $\min(100,1000)$ Mbps. Before the upgrade the ideal bottleneck was 54 Mbps; afterward it is the modem's 100 Mbps link. Rates on serial links do not add. This is an ideal capacity calculation; wireless sharing, protocol overhead and other path bottlenecks can reduce measured throughput.
A_ZH: 选 A，理想值为 $\min(100,1000)=100$ Mbps。升级前瓶颈是 54 Mbps Wi-Fi，升级后是 100 Mbps 调制解调器链路。串行链路速率不能相加。这是理想容量计算，实际吞吐量还可能受无线共享、协议开销和其他路径瓶颈影响。

@@ N098 | 09-ch1-qa | classroom | NQA:6;N1:61-65
Q_EN: Chapter 1 Q&A: which statement about transport is correct? A Always reliable; B Layer 4; C Provides service to the network layer; D Adds a header and sends upward to applications.
Q_ZH: Chapter 1 Q&A：关于传输层哪项正确？A 总是可靠；B 第 4 层；C 为网络层提供服务；D 加首部后向上传给应用。
A_EN: Only option B, Layer 4, is correct under bottom-up numbering. UDP shows transport is not always reliable. Transport provides service to the application layer above and uses the network layer below. During sending, it adds its header to application data and passes a segment downward to the network layer. Receiving reverses that direction and removes the relevant header.
A_ZH: 按自下而上的编号，只有 B“第 4 层”正确。UDP 表明传输服务并非总可靠。传输层向上面的应用层提供服务，使用下面的网络层。发送时给应用数据加传输首部，再把报文段交给网络层；接收时反向处理并移除相应首部。

@@ N099 | 07-exercises | classroom | NT2:3
Q_EN: Consider this illustrative traceroute row: `4  203.0.113.1  10.2 ms  *  11.0 ms`. It uses hop number, responding IP, then three probe results. What do the fields and the asterisk mean? Can you conclude ordinary forwarded packets are being lost?
Q_ZH: 观察这条教学用 traceroute 行：`4  203.0.113.1  10.2 ms  *  11.0 ms`。格式为跳号、回复 IP、三次探测结果。各字段和星号表示什么？能据此断定普通转发分组丢失吗？
A_EN: A typical row contains hop number, round-trip times for several probes (often three), and the responding router's name or IP address; exact display order varies by system. An asterisk means no reply arrived before that probe's timeout. It can reflect filtering or reply rate-limiting, so it is not by itself proof that the router drops ordinary forwarded traffic. RTTs include a return trip.
A_ZH: 典型一行包括跳号、数次探测的往返时间（常见三次），以及回复路由器的名称或 IP；不同系统的列顺序可能不同。星号表示该次探测超时未收到回复，可能来自过滤或回复限速，不能单独证明路由器丢弃普通转发流量。RTT 包含返回路程。

@@ N100 | 10-http2 | learn | N2B:1-3,6
Q_EN: How do non-persistent and persistent HTTP connections differ in the lecture model?
Q_ZH: 课堂模型中，非持久和持久 HTTP 连接有什么区别？
A_EN: Non-persistent HTTP uses a separate TCP connection for each object. Persistent HTTP reuses a TCP connection for multiple request–response exchanges between the same endpoints. Reuse can save repeated setup delay and operating-system work. This chapter analyzes the classic HTTP-over-TCP model; persistence is distinct from running several connections in parallel.
A_ZH: 非持久 HTTP 为每个对象单独建立 TCP 连接；持久 HTTP 在相同端点间复用一个 TCP 连接来完成多个请求—响应。复用可节省重复建立连接的时延和系统工作。本章分析传统 HTTP-over-TCP 模型，持久连接与同时开启多个并行连接是不同概念。

@@ N101 | 10-http2 | learn | N2B:4
Q_EN: Why does fetching one object with non-persistent HTTP take approximately $2RTT+L/R$?
Q_ZH: 为什么非持久 HTTP 获取一个对象约需 $2RTT+L/R$？
A_EN: One RTT establishes the TCP connection. A second RTT covers sending the request and receiving the start of the response. Then $L/R$ accounts for serializing the object. The model neglects DNS, request size, server processing, loss and TCP startup effects. RTT already includes round-trip propagation, so do not add the same propagation twice.
A_ZH: 第一个 RTT 用于建立 TCP 连接，第二个 RTT 用于发出请求并收到响应开头，再用 $L/R$ 计算对象串行化。模型忽略 DNS、请求大小、服务器处理、丢包与 TCP 启动效应。RTT 已包含往返传播，不能重复加同一传播时间。
MEDIA: chapter2-part2-slide-4.png

@@ N102 | 10-http2 | worked | N2B:4-5
Q_EN: RTT is 40 ms, an object is 100 kB, and throughput is 10 Mbps. Estimate the first fetch and a later sequential fetch on the same persistent connection.
Q_ZH: RTT 为 40 毫秒，对象为 100 kB、吞吐量为 10 Mbps，估算首次获取和同一持久连接上后续顺序获取的时间。
A_EN: Using decimal kB, transmission takes $100000\times8/10^7=80$ ms. A first fetch requiring setup takes $2(40)+80=160$ ms. A later request after the previous response completes takes $40+80=120$ ms. These ideal estimates omit DNS, TLS, processing and TCP dynamics, as in the lecture's timing model.
A_ZH: 按十进制 kB，传输需 $100000\times8/10^7=80$ 毫秒。需要建连的首次获取为 $2(40)+80=160$ 毫秒；前一响应完成后，再顺序发送的后续请求为 $40+80=120$ 毫秒。按课堂时序模型，这里忽略 DNS、TLS、处理和 TCP 动态过程。

@@ N103 | 10-http2 | worked | N2B:2-6
Q_EN: A base HTML page references ten images from one server. Ignoring object transmission, compare serial non-persistent HTTP with sequential persistent HTTP.
Q_ZH: 一个基础 HTML 引用同一服务器的十张图片，忽略对象传输时间，比较串行非持久 HTTP 与顺序持久 HTTP。
A_EN: There are eleven objects. Serial non-persistent access needs $11\times2RTT=22RTT$. Sequential persistent access needs one setup RTT plus one request–response RTT per object, giving $12RTT$. The image URLs become known after the base HTML arrives. The persistent calculation here does not assume pipelining or HTTP/2 multiplexing.
A_ZH: 共十一个对象。串行非持久方式需 $11\times2RTT=22RTT$；顺序持久方式需一次建连 RTT，加每个对象一次请求—响应 RTT，共 $12RTT$。图片 URL 在基础 HTML 到达后才知道。此处持久连接计算没有假设流水线或 HTTP/2 多路复用。

@@ N104 | 10-http2 | learn | N2B:5-7
Q_EN: How do connection reuse, concurrent connections and pipelined requests differ?
Q_ZH: 连接复用、并发连接与流水线请求怎样区分？
A_EN: Reuse keeps one connection for later requests. Concurrent connections use several connections at once. Pipelining sends additional requests on one connection before earlier responses finish. Each changes the timing assumptions differently. The slides' example of four to six parallel browser connections is historical context, not a permanent rule for every browser or HTTP version.
A_ZH: 复用是保留一个连接供后续请求使用；并发连接是同时使用多个连接；流水线是在一个连接上、不等前一响应结束就继续发请求。三者改变时序的方式不同。幻灯片中浏览器并行四至六条连接属于历史示例，不是所有浏览器或 HTTP 版本的固定规则。
MEDIA: chapter2-part2-slide-5.png

@@ N105 | 10-http2 | worked | N2B:2-7
Q_EN: In an ideal non-persistent model with five parallel connections and ten tiny images, how many RTTs are needed including the base HTML?
Q_ZH: 理想非持久模型中，用五条并行连接获取十张很小的图片，连同基础 HTML 一共需要多少 RTT？
A_EN: Fetch the HTML first in $2RTT$. The ten images form two groups of five, with each parallel group taking $2RTT$. Total is $2+2\times2=6RTT$. Assume negligible transmission, no DNS/TLS/processing delays, and independent connections that can start together. With substantial object sizes and a shared bottleneck, parallel transfers compete for the same capacity.
A_ZH: 先用 $2RTT$ 获取 HTML。十张图分两组、每组五张并行，每组需 $2RTT$，合计 $2+2\times2=6RTT$。假设传输可忽略、无 DNS/TLS/处理时延，且连接可同时开始。对象较大且共享瓶颈时，并行传输仍会竞争相同容量。

@@ N106 | 10-http2 | learn | N2B:8-9
Q_EN: What information is in an HTTP/1.1 request line and its headers?
Q_ZH: HTTP/1.1 请求行与首部包含哪些信息？
A_EN: A request line such as `GET /index.html HTTP/1.1` gives method, request target and HTTP version. Header fields follow, such as `Host`, and an empty line ends the header section; a message body may follow when applicable. The lecture's readable text format is HTTP/1.x syntax. Do not assume HTTP/2 or HTTP/3 encodes every message as this same plain-text layout.
A_ZH: 例如 `GET /index.html HTTP/1.1` 给出方法、请求目标和 HTTP 版本，后面是 `Host` 等首部字段。空行结束首部区，适用时再跟消息体。课堂的可读文本格式是 HTTP/1.x 语法，不能假定 HTTP/2、HTTP/3 都按同样纯文本布局编码消息。
MEDIA: chapter2-part2-slide-9.png

@@ N107 | 10-http2 | learn | N2B:8-9
Q_EN: What is the basic distinction among GET, HEAD and POST?
Q_ZH: GET、HEAD 和 POST 的基本区别是什么？
A_EN: GET requests a resource representation. HEAD requests the corresponding response metadata without the representation body. POST asks the target resource to process supplied content according to that resource's semantics. The method is part of the request line; headers and body are separate components. Real behavior must follow the protocol and application definition rather than a vague “all requests download files” model.
A_ZH: GET 请求资源表示，HEAD 请求相应响应元数据但不返回表示主体，POST 请求目标资源按其语义处理提交内容。方法位于请求行，首部和消息体是独立组成部分。实际行为须按协议和应用定义理解，不能笼统认为所有请求都是下载文件。

@@ N108 | 10-http2 | learn | N2B:10-13
Q_EN: What four components implement the lecture's cookie-based state example?
Q_ZH: 课堂基于 Cookie 维持状态的例子由哪四部分组成？
A_EN: The server sends a `Set-Cookie` response field, the browser stores cookie data, later requests carry a `Cookie` field, and the site maintains associated backend state. An identifier can link otherwise separate requests to a session or shopping cart. The cookie need not contain the whole cart or the user's password. HTTP's basic stateless semantics and application-level state can coexist.
A_ZH: 服务器响应的 `Set-Cookie` 字段、浏览器保存的 Cookie 数据、后续请求携带的 `Cookie` 字段，以及网站关联的后端状态，共同组成该例子。标识符可把独立请求关联到会话或购物车。Cookie 不必包含完整购物车或用户密码。HTTP 基础无状态语义与应用状态可以并存。
MEDIA: chapter2-part2-slide-12.png

@@ N109 | 10-http2 | learn | N2B:14-15
Q_EN: How does a web cache handle a hit and a miss?
Q_ZH: Web 缓存怎样处理命中与未命中？
A_EN: On a usable cache hit, the cache returns the stored object to the client. On a miss, it fetches from the origin server, returns the result, and may store an eligible response. The cache acts as server toward the client and client toward the origin. A stored copy is not automatically usable forever; freshness and protocol rules matter.
A_ZH: 命中可用缓存时，缓存直接把已存对象返回客户端；未命中时，先向源服务器获取，再返回结果，并可保存符合条件的响应。面对用户时它是服务器，面对源站时它是客户端。存有副本不代表永远可直接使用，仍要考虑新鲜度和协议规则。
MEDIA: chapter2-part2-slide-14.png

@@ N110 | 10-http2 | worked | N2B:14-15
Q_EN: In a simplified model, cache-hit delay is 10 ms, miss delay is 110 ms and hit probability is 0.4. What is mean response time?
Q_ZH: 简化模型中，缓存命中时延 10 毫秒、未命中 110 毫秒、命中概率 0.4，平均响应时间是多少？
A_EN: $E[T]=0.4(10)+0.6(110)=70$ ms. Define the miss delay as the entire miss path, including lookup, so that you do not count lookup twice. Caching can also reduce access-link traffic and queueing, but that additional network effect is not captured by fixed 10/110 ms delays. This is an added worked example applying the slide's cache mechanism.
A_ZH: $E[T]=0.4(10)+0.6(110)=70$ 毫秒。这里将未命中时延定义为包含查找在内的完整路径，避免重复计算查找。缓存还能减少接入链路流量与排队，但固定的 10/110 毫秒模型没有描述这种额外网络效应。本题是根据课件缓存机制补充的例题。

@@ N111 | 11-email | learn | N2B:17-18,21
Q_EN: What are the main components of Internet email in the lecture model?
Q_ZH: 课堂模型中，互联网电子邮件的主要组成是什么？
A_EN: A user agent lets a person compose and read mail. Mail servers maintain incoming mailboxes and outgoing queues. SMTP transfers messages between mail systems. Sending a message to a server and reading a stored message from a mailbox are separate operations, often using different protocols. A queue lets a server retain a message while waiting to deliver it.
A_ZH: 用户代理负责写信和读信；邮件服务器维护收件邮箱和发件队列；SMTP 在邮件系统间传递消息。向服务器发送邮件与从邮箱读取已存邮件是不同操作，往往使用不同协议。队列允许服务器在等待投递期间保留消息。
MEDIA: chapter2-part2-slide-17.png

@@ N112 | 11-email | learn | N2B:19-22
Q_EN: What transport, port and transfer phases does the basic server-to-server SMTP example use?
Q_ZH: 基础服务器间 SMTP 示例使用什么传输、端口和阶段？
A_EN: It uses TCP, with port 25 for server-to-server transfer, and proceeds through greeting, message transfer and connection closure. SMTP can reuse a connection for multiple messages to the same receiving server. A user's message-submission configuration can use a different port and security arrangement, so the example is not a universal mail-client configuration recipe.
A_ZH: 服务器间传递使用 TCP 的 25 端口，经历问候、消息传送、关闭连接。SMTP 可复用连接向同一接收服务器传多封邮件。用户提交邮件时可采用不同端口及安全配置，因此该示例不是所有邮件客户端的通用配置方法。

@@ N113 | 11-email | classroom | N2B:20
Q_EN: What do `MAIL FROM`, `RCPT TO`, `DATA` and the single-dot line mean in the SMTP transcript?
Q_ZH: SMTP 对话中的 `MAIL FROM`、`RCPT TO`、`DATA` 和单独一行的点分别表示什么？
A_EN: `MAIL FROM` identifies the envelope sender; `RCPT TO` names an envelope recipient. `DATA` begins transmission of the message after the server's appropriate reply. A line containing only a dot ends that data block in the illustrated protocol, and `QUIT` ends the session. Protocol replies carry status codes. These commands are distinct from the message's visible From/To headers.
A_ZH: `MAIL FROM` 指定信封发件人，`RCPT TO` 指定信封收件人；服务器给出相应回复后，`DATA` 开始传邮件内容。在示例协议中，单独一行的点结束该数据块，`QUIT` 结束会话。协议回复带有状态码。这些命令不同于邮件正文前可见的 From/To 首部。
MEDIA: chapter2-part2-slide-20.png

@@ N114 | 11-email | learn | N2B:20,23
Q_EN: How do an email's envelope, message headers and body differ?
Q_ZH: 邮件信封、消息首部和消息体有什么区别？
A_EN: The transport envelope guides mail delivery and is conveyed through SMTP commands. Message headers contain fields such as From, To and Subject; a blank line separates them from the body. A displayed header is not itself the SMTP delivery instruction. Separating these concepts helps explain why delivery recipients and visible header recipients need not always be identical.
A_ZH: 传输信封通过 SMTP 命令表达，用于指导邮件投递；消息首部包含 From、To、Subject 等字段；空行将首部与消息体分开。界面显示的首部本身不是 SMTP 投递指令。区分它们后，就能理解实际投递收件人与可见首部收件人不一定完全相同。

@@ N115 | 11-email | learn | N2B:22,24
Q_EN: Why is SMTP called push while the basic HTTP retrieval example is called pull?
Q_ZH: 为什么 SMTP 被称为 push，而基础 HTTP 获取被称为 pull？
A_EN: A sending mail server initiates delivery to a receiving mail server, pushing an available message. In the basic web example, a client requests a resource, pulling it from the server. These describe the application exchanges shown, not every possible use of HTTP. SMTP's delivery to the recipient's server is still separate from the recipient reading the message.
A_ZH: 发件服务器主动向收件服务器投递已有消息，因此称推送；基础 Web 示例由客户端请求资源，从服务器拉取。这描述的是所示应用交互，而非 HTTP 的所有可能用途。SMTP 把邮件送到收件服务器，仍不同于收件人实际阅读邮件。

@@ N116 | 11-email | learn | N2B:24-27
Q_EN: What are POP3's three phases and typical commands?
Q_ZH: POP3 有哪三个阶段？典型命令是什么？
A_EN: The basic example opens TCP port 110, then performs authorization, transaction and update. Authorization identifies the user; transaction commands include LIST to list messages, RETR to retrieve one and DELE to mark one for deletion. A normal QUIT transitions to update, where pending deletions are processed. Do not interpret downloading alone as an unavoidable server-side deletion.
A_ZH: 基础示例连接 TCP 110 端口，依次进入认证、事务和更新阶段。认证用于识别用户；事务命令中，LIST 列出邮件，RETR 取邮件，DELE 标记删除。正常 QUIT 进入更新阶段处理待删除项。不能把下载本身理解成一定会删除服务器邮件。

@@ N117 | 11-email | learn | N2B:27-28
Q_EN: How do POP3's download modes differ from IMAP's server-side organization?
Q_ZH: POP3 的下载模式与 IMAP 的服务器端组织有什么区别？
A_EN: A POP3 client can download and request deletion or download and keep messages. IMAP supports richer server-side mailbox state such as folders and message organization across sessions. The slide's “POP3 is stateless across sessions” is a simplified contrast about access-session state; it does not mean the server forgets stored messages or every persistent message identifier.
A_ZH: POP3 客户端可下载后请求删除，也可下载后保留邮件。IMAP 支持更丰富的跨会话服务器邮箱状态，例如文件夹和邮件组织。课件“POP3 跨会话无状态”是针对访问会话的简化对比，并不意味着服务器会忘记已存邮件或所有持久消息标识。
MEDIA: chapter2-part2-slide-28.png

@@ N118 | 11-email | learn | N2B:24,29
Q_EN: Which protocols carry browser-based webmail between browser and service, and between mail servers?
Q_ZH: Web 邮箱中，浏览器与服务端、邮件服务器之间分别使用什么协议？
A_EN: The browser communicates with the webmail service through HTTP, commonly secured as HTTPS. Mail servers still commonly exchange messages using SMTP. A browser interface therefore does not make SMTP disappear from the delivery path. POP3 and IMAP are mailbox-access protocols used by other client arrangements; they are not required between the browser and the web interface.
A_ZH: 浏览器通过 HTTP 与 Web 邮箱服务通信，通常以 HTTPS 保护；邮件服务器之间仍常使用 SMTP。采用浏览器界面并不会让 SMTP 从投递路径消失。POP3、IMAP 属于其他客户端安排下的邮箱访问协议，不要求浏览器到 Web 界面这一段必须使用它们。
MEDIA: chapter2-part2-slide-24.png

@@ N119 | 11-email | check | N2B:19-23;SMTPRFC:4.1.1.4
Q_EN: Does an SMTP success reply prove that the recipient has read the message?
Q_ZH: SMTP 返回成功，是否证明收件人已经读信？
A_EN: No. A successful acceptance reply concerns the receiving system's handling responsibility at that stage, not a human reading event. Messages can still pass through queues, later delivery steps and mailbox handling. Keep protocol acceptance, final mailbox delivery and user reading distinct. This is an extension of the lecture's command–response example.
A_ZH: 不能。成功接受回复描述该阶段接收系统的处理责任，并不是人类阅读事件。邮件还可能经过队列、后续投递和邮箱处理。协议接受、最终入箱与用户阅读应分开理解。本卡扩展了课堂命令—回复示例。

@@ N120 | 11-email | check | N2B:19,23;SMTPRFC:2.3.1
Q_EN: How should I interpret the slides' statement that SMTP mail is 7-bit ASCII?
Q_ZH: 怎样理解幻灯片中“SMTP 邮件是 7-bit ASCII”的说法？
A_EN: It describes the basic historical transfer model used for the example. Modern mail supports richer content through message encodings and negotiated SMTP extensions; the basic ASCII transcript is not evidence that today's email cannot carry other languages or attachments. Learn the distinction between transfer protocol and content representation. Do not silently change the assumptions of a question explicitly using the basic model.
A_ZH: 它描述例子采用的历史基础传输模型。现代邮件通过内容编码和协商的 SMTP 扩展支持更丰富内容，ASCII 对话示例不能证明今天的邮件无法携带其他语言或附件。应区分传输协议与内容表示；题目若明确采用基础模型，也不要自行替换其假设。

@@ N121 | 12-dns | learn | N2B:31-32
Q_EN: What two meanings of DNS should I distinguish?
Q_ZH: DNS 的哪两个含义需要区分？
A_EN: DNS is both a distributed naming database and an application-layer protocol used to query it. It supports name-to-address resolution, aliases, mail routing information and related records. Naming is essential to many Internet applications but does not belong to the network layer merely because it is important. A successful name lookup is one step before contacting the desired service.
A_ZH: DNS 既是分布式命名数据库，也是查询该数据库的应用层协议。它支持名称到地址解析、别名、邮件路由信息等记录。命名对很多互联网应用很重要，但重要并不意味着它属于网络层。成功解析名称只是联系目标服务前的一步。

@@ N122 | 12-dns | learn | N2B:33-36
Q_EN: Why does DNS use a distributed hierarchy rather than one central naming server?
Q_ZH: 为什么 DNS 使用分布式层次结构，而不是一个中央命名服务器？
A_EN: A single server would concentrate failure risk, query traffic, distance and administrative maintenance. Hierarchical delegation lets different organizations manage their own zones while higher levels point toward them. Replication and caching further reduce load and delay. The hierarchy organizes authority over names; it is not a requirement that every query visit every level.
A_ZH: 单服务器会集中故障风险、查询流量、距离开销和管理维护压力。层次委派让不同组织管理自己的区域，上级提供找到下级的线索；复制与缓存进一步降低负载和时延。层次结构组织的是名称管理权，不要求每次查询都访问所有层级。
MEDIA: chapter2-part2-slide-34.png

@@ N123 | 12-dns | learn | N2B:34-37
Q_EN: What are the roles of root, TLD, authoritative servers and a local resolver?
Q_ZH: 根服务器、TLD、权威服务器与本地解析器分别负责什么？
A_EN: Root servers provide top-level delegation information. TLD servers guide resolution within a top-level domain. Authoritative servers answer from the zones they manage. A local recursive resolver works on behalf of clients, follows referrals when needed and caches results. The local resolver is a service role beside the authority hierarchy, not an extra level beneath every authoritative server.
A_ZH: 根服务器提供顶级委派信息；TLD 服务器引导相应顶级域内的解析；权威服务器依据自己管理的区域回答；本地递归解析器代表客户端工作，必要时跟随转介并缓存结果。本地解析器是权威层次旁的服务角色，不是所有权威服务器下方又加一层。

@@ N124 | 12-dns | learn | N2B:38-40
Q_EN: How do recursive and iterative DNS queries differ in the lecture's typical pattern?
Q_ZH: 课堂典型模式中的递归与迭代 DNS 查询有什么区别？
A_EN: A recursive request asks the contacted resolver to complete resolution on the client's behalf. In an iterative exchange, a server may return a referral telling the requester whom to ask next. Typically the host asks its local resolver recursively, while the resolver follows root, TLD and authoritative referrals iteratively. The all-recursive diagram is an alternative model, not the usual role of public root servers.
A_ZH: 递归请求要求被联系的解析器代表客户端完成解析；迭代交互中，服务器可返回转介，告诉请求者接下来问谁。典型模式是主机递归询问本地解析器，本地解析器再迭代访问根、TLD 与权威链路。课件的全递归图是另一种模型，不是公共根服务器的通常职责。
MEDIA: chapter2-part2-slide-39.png

@@ N125 | 12-dns | classroom | N2B:38-39
Q_EN: In the illustrated cold-cache lookup with one root, one TLD and one authoritative exchange, why are there eight DNS messages?
Q_ZH: 所示冷缓存查询经历根、TLD、权威各一次交互，为什么一共八条 DNS 消息？
A_EN: The host sends one request to its local resolver and receives one response. The resolver makes three upstream request–response exchanges, adding six messages. Total: $2+3\times2=8$. Assume server addresses are already available and no retries, extra delegations or other lookups are needed. Cache hits can skip some or all upstream exchanges.
A_ZH: 主机向本地解析器发一次请求并收一次响应，共两条；解析器再进行三组上游请求—响应，增加六条，总共 $2+3\times2=8$。假设服务器地址已知，且无需重试、额外委派或其他查询。缓存命中可跳过部分或全部上游交互。
MEDIA_FRONT: chapter2-part2-slide-38.png

@@ N126 | 12-dns | worked | N2B:38-41
Q_EN: Host–resolver RTT is 2 ms; sequential resolver exchanges with root, TLD and authority take 20, 30 and 10 ms. What is the lookup delay?
Q_ZH: 主机—解析器 RTT 为 2 毫秒，解析器顺序访问根、TLD、权威的 RTT 为 20、30、10 毫秒，解析时延是多少？
A_EN: Neglecting processing and message transmission, total delay is $2+20+30+10=62$ ms. Count each complete request–response exchange once. If the resolver already has a usable final answer cached, the model reduces to the 2 ms host–resolver round trip. A different delegation chain or parallel work would require a different timing model.
A_ZH: 忽略处理和消息传输后，总时延为 $2+20+30+10=62$ 毫秒，每个完整请求—响应只计一次。若解析器已缓存可用最终答案，模型就只剩主机—解析器的 2 毫秒往返。委派链不同或存在并行工作时，需要调整时序模型。

@@ N127 | 12-dns | learn | N2B:41
Q_EN: What does DNS caching improve, and what can remain stale?
Q_ZH: DNS 缓存改善什么？什么内容可能变旧？
A_EN: A resolver can reuse an unexpired record to reduce lookup latency and upstream traffic. A cached answer need not come from an authoritative server in that exchange. If the authoritative record changes, other caches may keep older values until their allowed lifetime ends. Caching is a controlled reuse mechanism, not proof that all users see an update immediately.
A_ZH: 解析器复用未过期记录，可减少解析时延和上游流量。当次交互的缓存答案不一定直接来自权威服务器。权威记录变更后，其他缓存仍可能在允许的寿命内保留旧值。缓存是受控复用机制，不代表所有用户会立即看到更新。

@@ N128 | 12-dns | learn | N2B:42
Q_EN: What do A and NS DNS records contain?
Q_ZH: DNS 的 A 和 NS 记录分别包含什么？
A_EN: An A record associates a name with an IPv4 address. An NS record identifies an authoritative name server for a domain or zone, using that server's host name as its value. An NS value is therefore not itself the requested web server's address. Resolving the name-server host name may require address information as part of the delegation process.
A_ZH: A 记录把名称关联到 IPv4 地址；NS 记录用名字服务器的主机名作为值，标识域或区域的权威服务器。因此 NS 的值并不就是用户所求的 Web 服务器地址。委派解析时，还可能需要名字服务器主机名对应的地址信息。
MEDIA: chapter2-part2-slide-42.png

@@ N129 | 12-dns | learn | N2B:43
Q_EN: How do CNAME and MX records differ?
Q_ZH: CNAME 与 MX 记录有什么区别？
A_EN: CNAME maps an alias name to a canonical name. MX identifies a mail exchanger for a domain; its value names a mail server rather than directly storing that server's IP address. Address resolution of the named target is a further step. The same organization's web service and mail service can use different targets even when users recognize the same domain name.
A_ZH: CNAME 将别名映射到规范名称；MX 为域指定邮件交换服务器，其值是邮件服务器名称，而不是直接存该服务器 IP。还需要进一步解析目标名称的地址。同一组织的 Web 和邮件服务可以使用不同目标，即使用者看到的是相同域名。
MEDIA: chapter2-part2-slide-43.png

@@ N130 | 12-dns | worked | N2B:42-43
Q_EN: If `www.example.org` is a CNAME for `edge.example.net`, and that target has an A record, which record gives the final IPv4 address?
Q_ZH: 若 `www.example.org` 的 CNAME 指向 `edge.example.net`，后者有 A 记录，哪条记录提供最终 IPv4 地址？
A_EN: The target's A record supplies the IPv4 address. The CNAME supplies a name-to-name step, so treating the alias target string itself as an IP address is wrong. For mail to an example.org address, an MX lookup serves a different purpose: identifying the receiving mail exchanger. Record type determines how to interpret the value.
A_ZH: 目标的 A 记录提供 IPv4 地址；CNAME 只是名称到名称的一步，不能把别名目标字符串本身当 IP。发送到 example.org 的邮件时，MX 查询承担另一任务，即确定收件邮件交换服务器。记录类型决定如何解释记录值。

@@ N131 | 12-dns | worked | N2B:41
Q_EN: A DNS record was cached with TTL 300 s, 60 s ago. What lifetime remains in the basic countdown model?
Q_ZH: 一条 DNS 记录在 60 秒前以 TTL 300 秒进入缓存，按基础倒计时模型还剩多久？
A_EN: It has $300-60=240$ seconds remaining. After expiry, ordinary cache reuse requires refreshed information; a new lookup can also fail. TTL limits caching time, not the record's permanent existence at the authority. The lecture uses this model to explain why a DNS change need not become visible everywhere immediately.
A_ZH: 剩余 $300-60=240$ 秒。过期后，通常需更新信息才能继续复用缓存，新查询也可能失败。TTL 限制缓存时间，并不表示权威服务器上的记录届时永久消失。课件借此解释为何 DNS 变更不会立刻在所有地方可见。

@@ N132 | 12-dns | check | N2B:35,38-40;DNSRFC:4.3.1-4.3.2
Q_EN: Does a root DNS server normally resolve every queried host all the way to its final address?
Q_ZH: 根 DNS 服务器通常会亲自把每个主机名一直解析到最终地址吗？
A_EN: No. In the usual iterative hierarchy, it supplies a referral toward the relevant TLD. The recursive resolver continues the lookup. The slide's short prose on roots should be read alongside the later iterative-query diagram. Distinguish the resolver's job from an authoritative root server's job, and treat the slide's old server-instance count as historical rather than current.
A_ZH: 通常不会。典型迭代层次中，根服务器返回通往相应 TLD 的转介，由递归解析器继续查询。根服务器那页的简写应与后面的迭代图一起理解。要区分递归解析器和根权威服务器的职责，旧的服务器实例数量也应视作历史数据。

@@ N133 | 12-dns | check | N2B:41;N1:50-51
Q_EN: Is DNS TTL the same thing as the IP TTL used by traceroute?
Q_ZH: DNS TTL 与 traceroute 使用的 IP TTL 是一回事吗？
A_EN: No. DNS TTL is a cache lifetime, normally expressed in seconds. IPv4 TTL bounds a packet's forwarding lifetime and in ordinary routing is decremented at each hop; traceroute varies that hop limit to reveal routers. The shared name does not imply shared units or purpose. Expiring a DNS cache entry does not make an already transmitted IP packet expire.
A_ZH: 不是。DNS TTL 是缓存寿命，通常以秒计；IPv4 TTL 限制分组转发寿命，普通路由中每跳递减，traceroute 通过改变这个跳数限制发现路由器。同名不代表单位或用途相同。DNS 缓存到期不会让已经发出的 IP 分组因此过期。

@@ N134 | 12-dns | worked | N2B:4,38-41
Q_EN: A cold DNS lookup takes 62 ms. Then one HTTP object needs RTT 40 ms and 80 ms transmission on a new TCP connection. What is the combined ideal delay?
Q_ZH: 冷 DNS 查询需 62 毫秒，随后用新 TCP 连接取一个 HTTP 对象，RTT 40 毫秒、传输 80 毫秒，理想总时延是多少？
A_EN: Resolve the name first, then fetch the object: $62+2(40)+80=222$ ms. This combines separate application steps. Assume no TLS, processing, loss, extra DNS lookups or TCP startup penalty. With a usable DNS cache or an already established connection, remove only the corresponding cost rather than deleting all RTT terms.
A_ZH: 先解析名称，再取对象：$62+2(40)+80=222$ 毫秒。这把两个应用步骤组合起来。假设无 TLS、处理、丢失、额外 DNS 查询和 TCP 启动代价。若 DNS 缓存可用或连接已建立，应只去掉对应开销，而不是删掉所有 RTT 项。
