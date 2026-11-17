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
- `sudo pacman -S --needed strace ltrace perf htop iotop wireshark-qt tcpdump dnsutils curl wrk` (for tracing, profiling, network and load tests)
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
