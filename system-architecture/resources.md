# System architecture resources

## Books

| | Book | Level | Notes |
|---|---|---|---|
| ⭐💲 | *Designing Data-Intensive Applications* – Martin Kleppmann | Intermediate | The best single book for distributed systems |
| ⭐💲 | *Fundamentals of Software Architecture* – Mark Richards & Neal Ford | Beginner–intermediate | Architecture styles and trade-offs |
| 💲 | *Software Architecture: The Hard Parts* – Ford, Richards, Sadalage, Dehghani | Advanced | Trade-off analysis |
| ⭐🆓 | [Computer Systems: A Programmer's Perspective (CS:APP)](https://csapp.cs.cmu.edu/) | Intermediate | Free sample chapters, the core systems book |
| ⭐🆓 | [Operating Systems: Three Easy Pieces (OSTEP)](https://pages.cs.wisc.edu/~remzi/OSTEP/) | Intermediate | Free online, excellent |
| 🆓 | [High Performance Browser Networking – Ilya Grigorik](https://hpbn.co/) | Intermediate | Free online, TCP/HTTP/TLS |
| 💲 | *TCP/IP Illustrated, Vol. 1* – W. Richard Stevens | Advanced | Networking reference |
| 💲 | *Site Reliability Engineering* – Google | Intermediate | Free online at sre.google |
| 💲 | *The Linux Programming Interface* – Michael Kerrisk | Advanced | System calls in depth |
| 💲 | *Clean Architecture* – Robert C. Martin | Intermediate | Design principles |
| 💲 | *System Design Interview* – Alex Xu (vols. 1 & 2) | Beginner | Practical design interviews |
| 🆓 | [The Architecture of Open Source Applications](http://aosabook.org/) | Intermediate | Real systems explained by their authors |

## Courses and videos

- 🆓 [MIT 6.824 – Distributed Systems](https://pdos.csail.mit.edu/6.824/) ⭐
- 🆓 [CMU 15-213 – Introduction to Computer Systems](https://www.cs.cmu.edu/~213/)
- 🆓 [ByteByteGo](https://bytebytego.com/) – quick architecture explainers and diagrams
- 🆓 [Hussein Nasser – Backend Engineering (YouTube)](https://www.youtube.com/@hnasr) – networking, databases, backend
- 🆓 [Designing Data-Intensive Applications – author's resources](https://dataintensive.net/) – companion material for DDIA

## Interactive and free references

- 🆓 [roadmap.sh – Backend and System Design](https://roadmap.sh/) ⭐
- 🆓 [System Design Primer (GitHub)](https://github.com/donnemartin/system-design-primer) ⭐
- 🆓 [Julia Evans – zines and blog](https://jvns.ca/) – wonderful explanations of Linux, networking and tools
- 🆓 [Brendan Gregg – performance](https://www.brendangregg.com/) – observability and performance
- 🆓 [Linux man-pages](https://man7.org/linux/man-pages/)
- 🆓 [The Linux Kernel documentation](https://docs.kernel.org/)
- 🆓 [Architecture Decision Records (adr.github.io)](https://adr.github.io/)
- 🆓 [Google SRE book (free)](https://sre.google/books/)

## Papers

- Lamport, *Paxos Made Simple* (2001)
- Ongaro & Ousterhout, *In Search of an Understandable Consensus Algorithm (Raft)* (2014)
- DeCandia et al., *Dynamo: Amazon's Highly Available Key-value Store* (2007)
- Dean & Ghemawat, *MapReduce* (2004)
- Gilbert & Lynch, *Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-tolerant Web Services* (2002)

## Tools to try

| Area | Tool |
|------|------|
| Tracing | `strace`, `ltrace`, `perf`, `bpftrace` |
| Network | `tcpdump`, Wireshark, `curl -v`, `dig`, `ss` |
| Load testing | `wrk`, `k6` (https://k6.io), `hey` |
| Containers | Docker, Podman |
| Orchestration | Kubernetes (https://kubernetes.io/docs/tutorials/), k3s |
| IaC | Terraform (https://developer.hashicorp.com/terraform/tutorials) |
| Monitoring | Prometheus, Grafana, OpenTelemetry (https://opentelemetry.io) |
| Diagrams | Excalidraw (https://excalidraw.com), draw.io, Mermaid |
