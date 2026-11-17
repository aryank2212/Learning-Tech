# Computer architecture resources

## Books
| | Book | Notes |
|---|---|---|
| ⭐💲 | *Computer Architecture: A Quantitative Approach* — Hennessy & Patterson | The standard reference; read the current edition |
| ⭐💲 | *Computer Organization and Design: RISC-V Edition* — Patterson & Hennessy | The best first book; uses RISC-V throughout |
| 💲 | *Digital Design and Computer Architecture: RISC-V Edition* — Harris & Harris | Gates to CPU in one book |
| 💲 | *The RISC-V Reader: An Open Architecture Atlas* — Patterson & Waterman | Short, practical introduction to RISC-V |
| 💲 | *Computer Systems: A Programmer's Perspective* — Bryant & O'Hallaron | Also listed in [C](../languages/c/README.md) and [system architecture](../system-architecture/resources.md) |

## Courses and lectures
- ⭐🆓 [CS61C — Great Ideas in Computer Architecture (Berkeley)](https://cs61c.org/) — free materials, with RISC-V labs
- 🆓 [MIT 6.823 — Computer System Architecture (OCW)](https://ocw.mit.edu/courses/6-823-computer-system-architecture-fall-2005/)
- 🆓 Onur Mutlu's lectures (ETH Zürich, CMU 18-447) — search "Onur Mutlu computer architecture" on YouTube
- 🆓 Nand2Tetris, final chapters (see [digital electronics](../digital-electronics/resources.md))

## Simulators and tools
- [Spike (RISC-V ISA simulator)](https://github.com/riscv-software-src/riscv-isa-sim)
- [Venus (RISC-V in the browser)](https://venus.cs61c.org/)
- [gem5](https://www.gem5.org/) — full-system simulation for research
- [ChampSim](https://github.com/ChampSim/ChampSim) — cache and branch-prediction simulator
- [Compiler Explorer](https://godbolt.org/) — read the assembly your compiler produces
- [uops.info](https://uops.info/) — instruction latency and throughput measurements
- [Agner Fog's optimisation manuals](https://www.agner.org/optimize/) — detailed measurements and techniques
- [Linux perf wiki](https://perfwiki.github.io/main/)

## Papers
- Tomasulo, *An Efficient Algorithm for Exploiting Multiple Arithmetic Units* (IBM Journal, 1967)
- Jouppi, *Improving Direct-Mapped Cache Performance by the Addition of a Small Fully-Associative Cache and Prefetch Buffers* (ISCA 1990)
- Smith & Sohi, *The Microarchitecture of Superscalar Processors* (Proceedings of the IEEE, 1995)
- Hennessy & Patterson, *A New Golden Age for Computer Architecture* (CACM, 2019) — where the field is going and why

## Research
See [research/directions.md](../research/directions.md#computer-architecture) for open questions.
