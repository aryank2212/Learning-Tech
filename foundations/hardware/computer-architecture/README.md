# Computer Architecture

How a processor is organised so that it runs instructions quickly: instruction set design, pipelining, the memory hierarchy, branch prediction, parallel execution inside one core, multiprocessors and accelerators. It sits between digital electronics (gates and flip-flops) and the operating-system and compiler subjects (which run on top of it).

## Prerequisites
- [Digital electronics](../digital-electronics/README.md), phases 1–6 (or equivalent: combinational and sequential logic, ALUs, registers)
- C at Level 2 or better, and the ability to read simple assembly
- Basic [operating systems](../../../systems/kernels/operating-systems/README.md) ideas: processes, virtual memory

## Install
```bash
sudo pacman -S --needed qemu-full gcc binutils gdb valgrind perf hwloc numactl
```
- `qemu-full` includes RISC-V system emulation, so you can boot a RISC-V program without owning RISC-V hardware.
- `valgrind --tool=cachegrind ./program` reports cache hits and misses.
- `perf stat ./program` reports instructions per cycle, cache misses and branch mispredictions.
- `hwloc` provides `lstopo`, which draws your CPU's cores, caches and NUMA nodes.

Simulators and tools:
- **Spike** (the RISC-V reference simulator): [github.com/riscv-isa-sim](https://github.com/riscv-software-src/riscv-isa-sim)
- **Venus** (browser-based RISC-V simulator from Berkeley CS61C): [venus.cs61c.org](https://venus.cs61c.org/)
- **gem5** (research-grade system simulator): [gem5.org](https://www.gem5.org/). Build it from source by following its documentation.
- **ChampSim** (cache and branch-predictor simulator): [github.com/ChampSim](https://github.com/ChampSim/ChampSim)

Look at your own machine's counters before reading the theory: `perf stat -e cycles,instructions,cache-misses,branch-misses ls -R /usr > /dev/null`.

## Weekly rhythm
- One concept a week, then one measurement on real hardware with `perf`.
- Keep a notebook of predictions: "I think this loop will be slow because…". Then check.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, courses, simulators, papers

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- This is where performance stops being guesswork. Learn to read perf output and you'll write faster code for the rest of your career.
- Don't skip the cache material. Most real slowdowns I've seen come from memory, not computation.
- Measure on your own machine. Textbook numbers are a starting point, not a result.
