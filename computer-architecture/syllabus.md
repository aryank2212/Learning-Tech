# Computer architecture syllabus

Tick items in [progress/TRACKER.md](../progress/TRACKER.md).

### Phase 1 – Instruction set architecture (ISA)
- [ ] What an ISA is: the contract between software and hardware
- [ ] RISC vs CISC; load–store design
- [ ] Registers, addressing modes, calling conventions
- [ ] Reading RISC-V assembly

🛠️ Project: write a function in RISC-V assembly (sum an array, find a maximum) and run it in Venus or Spike.

### Phase 2 – The single-cycle datapath
- [ ] The five steps: fetch, decode, execute, memory, write-back
- [ ] Control signals and the ALU
- [ ] Program counter, branches and jumps

🛠️ Project: a single-cycle RISC-V subset CPU, in Verilog or in Logisim, that runs a loop.

### Phase 3 – Pipelining
- [ ] The five-stage pipeline and its throughput gain
- [ ] Hazards: data, control and structural
- [ ] Forwarding and stalls
- [ ] Cycles per instruction (CPI) and why it matters

🛠️ Project: add forwarding and hazard detection to your pipelined CPU. Measure the CPI before and after on the same program.

### Phase 4 – The memory hierarchy and caches
- [ ] SRAM vs DRAM; the latency gap
- [ ] Temporal and spatial locality
- [ ] Direct-mapped and set-associative caches
- [ ] Replacement policies (LRU and approximations)
- [ ] Write-through vs write-back; average memory access time (AMAT)

🛠️ Project: a cache simulator in C or Python. Feed it address traces and report hit rates for several cache sizes.

### Phase 5 – Virtual memory in hardware
- [ ] Page tables, the TLB, page walks
- [ ] Page faults and their cost (see [operating systems](../operating-systems/README.md))

🛠️ Project: use `perf` to count TLB misses for a strided array walk. Increase the stride until the misses dominate.

### Phase 6 – Branch prediction
- [ ] The cost of a misprediction in a deep pipeline
- [ ] Static prediction; bimodal (two-bit counters)
- [ ] Two-level and global-history predictors; TAGE (concept)

🛠️ Project: a two-bit saturating-counter predictor, simulated on a recorded branch trace. Report accuracy.

### Phase 7 – Instruction-level parallelism
- [ ] Superscalar issue
- [ ] Out-of-order execution; register renaming
- [ ] Tomasulo's algorithm and the reorder buffer
- [ ] Speculation and its security consequences (concept)

🛠️ Project: a small out-of-order scheduler simulator that shows how long a dependency chain limits throughput.

### Phase 8 – Data-level parallelism (SIMD)
- [ ] SSE and AVX vector registers
- [ ] Intrinsics and auto-vectorisation
- [ ] When vectorisation fails: aliasing, branches, unaligned data

🛠️ Project: a dot product in plain C, then with AVX2 intrinsics. Compare with `-O3` auto-vectorisation.

### Phase 9 – Multiprocessors and cache coherence
- [ ] Shared memory and cache coherence (MESI)
- [ ] Memory consistency models (sequential consistency, relaxed models)
- [ ] False sharing

🛠️ Project: show false sharing with two threads updating neighbouring counters. Fix it with padding and measure the difference.

### Phase 10 – GPUs and accelerators
- [ ] SIMT: warps, divergence and occupancy
- [ ] GPU memory hierarchy (link to [CUDA](../languages/cuda/README.md))
- [ ] Domain-specific accelerators (TPUs, NPUs), at a conceptual level

🛠️ Project: a tiled matrix multiply on the GPU. Use Nsight Compute to find its limiting resource.

### Phase 11 – Performance engineering
- [ ] Amdahl's law and the roofline model
- [ ] Profiling: `perf`, cachegrind, sampling profilers
- [ ] Benchmarking method: warm-up, repetition, variance

🛠️ Project: place two kernels on a roofline plot for your own CPU. Explain which one is memory-bound.

### Phase 12 – Capstone
- [ ] Extend a simulator (a cache, a predictor, or your pipelined CPU) with one new feature

🛠️ Project: write a performance report with at least three workloads and clear before-and-after numbers.
