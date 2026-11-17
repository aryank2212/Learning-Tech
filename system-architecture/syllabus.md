# System architecture syllabus

Tick items in [progress/TRACKER.md](../progress/TRACKER.md).

## Phase 1 – How a computer runs your program
- [ ] Binary, bits, two's complement, floating point (IEEE 754)
- [ ] CPU: instruction cycle, registers, pipelines, branch prediction
- [ ] Memory hierarchy: registers → L1/L2/L3 → RAM → disk; cache lines
- [ ] Compilation, linking, loading, the ELF format
- [ ] Virtual memory, pages, page tables

🛠️ **Project:** write a benchmark that shows the cost of cache misses (array traversal in row vs column order).

## Phase 2 – Operating systems
- [ ] Processes vs threads, context switching
- [ ] Scheduling: round robin, priorities
- [ ] Synchronisation: mutexes, semaphores, deadlock
- [ ] System calls and the user/kernel boundary
- [ ] File systems and I/O: buffering, `read`/`write`, `epoll`

🛠️ **Project:** a small shell or a `strace`-style tracer that lists the system calls a program makes.

## Phase 3 – Networking
- [ ] The OSI model vs TCP/IP model
- [ ] IP addresses, subnets, routing, NAT
- [ ] TCP: handshake, reliability, congestion control
- [ ] UDP, when to use it
- [ ] DNS: how a name becomes an IP
- [ ] HTTP/1.1, HTTP/2, HTTP/3 (QUIC)
- [ ] TLS: certificates, encryption, HTTPS handshake

🛠️ **Project:** build a TCP chat server; use `tcpdump` or Wireshark to watch the packets.

## Phase 4 – Single-machine services
- [ ] Client–server model, request lifecycle
- [ ] Databases: indexes, transactions, ACID
- [ ] Caching: cache-aside, TTL, invalidation
- [ ] Concurrency in servers: thread-per-request vs event loop
- [ ] Logging, metrics, tracing

🛠️ **Project:** a REST API with Postgres and Redis cache; measure requests/sec with `wrk` before and after caching.

## Phase 5 – Distributed systems
- [ ] CAP theorem and consistency models (strong, eventual)
- [ ] Replication: leader–follower, multi-leader, leaderless
- [ ] Partitioning / sharding and consistent hashing
- [ ] Consensus basics: Raft and Paxos (the ideas)
- [ ] Message queues and event streams (Kafka, RabbitMQ, SQS)
- [ ] Idempotency, retries, exactly-once vs at-least-once

🛠️ **Project:** a job queue with workers, retries and dead-letter handling.

## Phase 6 – Architecture and design
- [ ] Monolith vs microservices vs modular monolith: trade-offs
- [ ] Load balancing, reverse proxies (nginx, Caddy)
- [ ] API design: REST, gRPC, GraphQL
- [ ] Rate limiting, circuit breakers, backpressure
- [ ] Architecture Decision Records (ADRs)
- [ ] Capacity estimation: QPS, storage, bandwidth

🛠️ **Project:** design a URL shortener, a chat app and a video streaming service on paper. Write each as an ADR.

## Phase 7 – Operations
- [ ] Containers with Docker; images, volumes, networks
- [ ] Orchestration with Kubernetes (concepts first)
- [ ] Infrastructure as code (Terraform)
- [ ] CI/CD pipelines (GitHub Actions)
- [ ] Observability: Prometheus, Grafana, OpenTelemetry
- [ ] Incident response and postmortems

🛠️ **Project:** containerise an app, add a CI pipeline that tests and deploys it, and add a Grafana dashboard.

## Phase 8 – Security basics
- [ ] Authentication vs authorisation, sessions, JWT, OAuth 2.0
- [ ] Hashing passwords (bcrypt, argon2), never plain text
- [ ] OWASP Top 10
- [ ] Secrets management; never commit keys
- [ ] Least privilege, network segmentation

🛠️ **Project:** run a deliberately vulnerable app (OWASP Juice Shop) and fix each issue you find.
