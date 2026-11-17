# System Architecture

How computers, networks and large software systems work together, and how to design them. This area ties the rest of the repo together: a Rust or C program is a piece of a system, and a web app is a system of browsers, servers, databases and queues.

## Three layers you should understand

```
1. Computer systems   CPU, memory, OS, processes, threads, file systems
2. Networking         TCP/IP, HTTP, DNS, TLS, load balancers
3. Distributed design services, databases, queues, caches, scaling, failure
```

Learn bottom-up when you can, but you can also design at the top and dig down when something breaks.

## Install / practical setup

No special install. You need:

- A Linux machine (this one works)
- `sudo pacman -S --needed strace ltrace perf htop iotop wireshark-qt tcpdump bind curl` (for tracing, profiling, network and load tests)
- `wrk` for load tests is in the AUR (`yay -S wrk`), not the official repos. `bind` provides `dig`.
- A free account on a cloud provider for the deployment projects (AWS, Google Cloud or Azure free tiers), or Docker on your machine:

```bash
sudo pacman -S docker docker-compose
sudo systemctl enable --now docker
sudo usermod -aG docker $USER      # log out and back in
docker run hello-world
```

## Sections in this folder

- [syllabus.md](syllabus.md) – topics in order, with projects
- [resources.md](resources.md) – books, courses, papers, tools

## Architecture patterns, briefly
- **API gateway:** one entry point that routes, authenticates and rate-limits requests.
- **Backend for frontend (BFF):** one backend per client type, such as web or mobile.
- **Circuit breaker:** stop calling a failing service for a while, then retry carefully.
- **Bulkhead:** isolate resources so one failing part can't drain the rest.
- **Sidecar:** a helper process beside a service, for logging, TLS or retries.
- **Strangler fig:** replace a legacy system piece by piece, behind a facade.
- **Saga:** a series of local transactions, each with a compensating action, instead of one distributed transaction.
- **Outbox:** write events to the same database as the data change, then publish them reliably.
- **CQRS:** separate models for writes and reads.
- **Event sourcing:** store every change as an event, and rebuild state by replaying the log.
- **Change data capture (CDC):** stream database changes to other systems.

## Design document template
1. Context and goal
2. Requirements: functional, and non-functional (latency, availability, cost)
3. Capacity estimates: requests per second, storage, bandwidth
4. API and data model
5. High-level diagram
6. Deep dive on the hardest part
7. Trade-offs and alternatives considered
8. Failure modes, and how you would detect them
9. Monitoring and rollout plan

## Engineering blogs worth reading
- [Netflix Tech Blog](https://netflixtechblog.com/)
- [Uber Engineering](https://www.uber.com/blog/engineering/)
- [Cloudflare Blog](https://blog.cloudflare.com/)
- [Dropbox Tech Blog](https://dropbox.tech/)
- [Stripe Engineering](https://stripe.com/blog/engineering)
- [High Scalability](http://highscalability.com/) — architecture case studies

## Related sections
[Computer networking](../../networks/computer-networking/README.md) · [Operating systems](../../kernels/operating-systems/README.md) · [Data & big data](../../../data/analytics/predictive-big-data-analytics/README.md) · [Cryptography](../../../security/cryptography/cryptography/README.md)

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- System design interviews reward memorised diagrams. Real design rewards writing down trade-offs and failure modes. Practise the second.
- Read engineering blogs from companies that have hit real scale. Their postmortems teach more than theoretical patterns.
- Don't reach for microservices by default. A well-built monolith is often the right answer for longer than people expect.
