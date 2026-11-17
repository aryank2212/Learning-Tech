# Computer Networking

How devices talk to each other: from electrical signals on a cable to a web page loading. It covers the OSI and TCP/IP models, addressing and routing, reliable transport, application protocols, and network security.

## Prerequisites
Linux command line. Basic programming (Python or C) for the socket projects.

## Install
```bash
sudo pacman -S --needed wireshark-qt tcpdump nmap bind mtr iperf3 openbsd-netcat socat curl
```
- `bind` provides `dig` for DNS lookups.
- `mtr` combines ping and traceroute.
- `iperf3` measures bandwidth between two machines.
- `openbsd-netcat` gives you `nc`.

Simulators (no hardware needed):
- **Cisco Packet Tracer**, free through [Cisco Networking Academy](https://www.netacad.com/)
- **GNS3** — [gns3.com](https://www.gns3.com/), real router images
- **Mininet** — [mininet.org](http://mininet.org/), software-defined networks on Linux

Wireshark: capture on the `lo` interface while you run a local client and server. Filter with `tcp.port == 8080`.

> Only scan or test networks you own or have written permission to test. Scanning other people's networks is illegal in many countries.

## Weekly rhythm
- Two theory sections a week, then one capture or lab exercise.
- Every week, explain one protocol aloud, from memory, as if teaching it.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, courses, RFCs, tools

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- Networking stays abstract until you capture packets. Start with Wireshark on your own traffic; it's the fastest way to learn.
- The layers matter more than individual protocols. Once you see how TCP sits on IP, other protocols become variations.
- Only test networks you own. It's easy to cross that line by accident.
