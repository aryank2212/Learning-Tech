# Computer networking syllabus

Tick items in [progress/TRACKER.md](../progress/TRACKER.md).

### Phase 1 – Foundations
- [ ] LAN, WAN, the Internet; topologies
- [ ] Packet switching vs circuit switching
- [ ] Delays: transmission, propagation, queueing, processing
- [ ] Throughput, bandwidth, latency
- [ ] OSI model vs TCP/IP model; encapsulation

🛠️ Project: `ping` and `traceroute` three servers on different continents, and explain each hop's delay.

### Phase 2 – Physical and link layer
- [ ] Signals and encoding; Ethernet frames
- [ ] MAC addresses, ARP
- [ ] Switches and MAC learning tables
- [ ] VLANs; Wi-Fi (802.11) basics

🛠️ Project: capture ARP and Ethernet frames in Wireshark and label every field.

### Phase 3 – Network layer (IP)
- [ ] IPv4 header; addressing classes and CIDR
- [ ] Subnetting by hand, in binary
- [ ] NAT, DHCP, ICMP
- [ ] IPv6 basics; fragmentation

🛠️ Project: write a subnet calculator in Python and design an address plan for a three-office company.

### Phase 4 – Routing
- [ ] Forwarding vs routing; routing tables (`ip route`)
- [ ] Distance-vector routing (RIP) and Bellman–Ford
- [ ] Link-state routing (OSPF) and Dijkstra
- [ ] BGP: path-vector routing between autonomous systems

🛠️ Project: simulate link-state routing on a six-router topology.

### Phase 5 – Transport layer
- [ ] UDP; when to choose it
- [ ] TCP: three-way handshake, sequence and ACK numbers
- [ ] Flow control (sliding window)
- [ ] Congestion control: slow start, AIMD, CUBIC, BBR
- [ ] Retransmission timers

🛠️ Project: watch the congestion window during a large transfer (`ss -ti` and iperf3), and plot it.

### Phase 6 – Application layer
- [ ] DNS: record types, recursive vs authoritative resolution, caching
- [ ] HTTP/1.1, HTTP/2, HTTP/3 (QUIC)
- [ ] Email protocols: SMTP, IMAP
- [ ] WebSockets

🛠️ Project: write a tiny HTTP server using raw sockets, then a DNS lookup tool with `dnspython`.

### Phase 7 – Network programming
- [ ] Sockets API for TCP and UDP
- [ ] Blocking vs non-blocking I/O; `select`, `epoll`
- [ ] Multiplexing many clients
- [ ] TLS on top of sockets

🛠️ Project: a multi-room chat server (see Beej's guide for the pattern).

### Phase 8 – Network security
- [ ] Firewalls with `nftables`
- [ ] TLS certificates and trust
- [ ] VPNs with WireGuard
- [ ] DDoS basics: understand the mechanics and defences, never attack

🛠️ Project: a WireGuard tunnel between your host and a VM, with an `nftables` policy that allows only the ports you need.

### Phase 9 – Cloud and software-defined networking
- [ ] Control plane vs data plane; OpenFlow
- [ ] Virtual private clouds: public and private subnets, route tables
- [ ] Load balancers, CDNs, service meshes

🛠️ Project: design a VPC for a web app with a database. Draw it, then write the route tables.

### Phase 10 – Certification (optional)
- [ ] CompTIA Network+ (Professor Messer's free videos)
- [ ] Cisco CCNA through Networking Academy

## Capstone
Build a small network: two subnets, a router, a firewall and a web server, in GNS3, Mininet or a set of VMs. Capture the traffic, and write up what each packet does.
