# Parallel & distributed computing syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md).

### Phase 1 – Why parallelism, and how to measure it
- [ ] Why clock speeds stopped rising
- [ ] Speedup and efficiency
- [ ] Amdahl's law and Gustafson's law
- [ ] Strong scaling vs weak scaling

🛠️ Project: a parallel sum on your machine. Plot speedup against threads, and compare it with Amdahl's prediction.

### Phase 2 – Threads and shared memory
- [ ] Race conditions
- [ ] Mutexes, atomics, and what they cost
- [ ] Memory ordering (concepts)

🛠️ Project: a parallel histogram in three versions: one lock, atomics, and per-thread buffers. Benchmark all three.

### Phase 3 – OpenMP
- [ ] `parallel for`, reductions and data sharing
- [ ] Scheduling: static, dynamic, guided
- [ ] Tasks and nested parallelism

🛠️ Project: parallelise a Mandelbrot renderer. Measure speedup at 1, 2, 4 and 8 threads.

### Phase 4 – Parallel patterns
- [ ] Map, reduce, scan
- [ ] Stencil computations
- [ ] Divide and conquer
- [ ] Pipelines and work stealing (concepts)

🛠️ Project: a parallel prefix sum (scan) with OpenMP, checked against the sequential result.

### Phase 5 – Message passing with MPI
- [ ] Processes, communicators, ranks
- [ ] Point-to-point and collective operations
- [ ] Avoiding deadlock
- [ ] Non-blocking communication

🛠️ Project: a heat-equation solver across processes, with halo exchange between neighbours.

### Phase 6 – GPUs and OpenCL
- [ ] SIMT execution and the GPU memory hierarchy (see [CUDA](../../../languages/gpu/cuda/README.md))
- [ ] Streams and overlapping copies with compute
- [ ] OpenCL concepts: platforms, devices, kernels

🛠️ Project: a reduction written in OpenMP and in CUDA. Compare the designs and the speed.

### Phase 7 – Memory systems at scale
- [ ] Cache coherence and false sharing (see [computer architecture](../../../foundations/hardware/computer-architecture/README.md))
- [ ] NUMA: local and remote memory
- [ ] Lock-free data structures, at a basic level

🛠️ Project: measure local and remote memory bandwidth with `numactl`, and explain the difference.

### Phase 8 – Foundations of distributed systems
- [ ] Failures: crash, omission, Byzantine
- [ ] Timeouts and unreliable networks
- [ ] Lamport clocks and vector clocks
- [ ] Linearisability and other consistency models

🛠️ Project: implement Lamport logical clocks in a simulator of three message-passing processes.

### Phase 9 – Data-parallel frameworks
- [ ] The MapReduce model
- [ ] Task graphs in Dask and Ray
- [ ] Spark in practice (see [big data](../../../data/analytics/predictive-big-data-analytics/README.md))

🛠️ Project: word count on a large text corpus, with Dask or Spark. Measure speedup on 1, 2 and 4 workers.

### Phase 10 – Replication and consensus
- [ ] Replicated state machines
- [ ] Quorums
- [ ] Leader election and Raft (see [system architecture](../../architecture/system-architecture/resources.md))
- [ ] Checkpointing and recovery

🛠️ Project: a Raft-style leader election simulation with random node failures. Measure how long elections take.

### Phase 11 – Testing and verifying distributed systems
- [ ] Fault injection and chaos testing
- [ ] Model checking with TLA+ (concepts)
- [ ] What Jepsen-style tests reveal

🛠️ Project: inject network partitions into your Phase 10 simulation and report what breaks.

### Phase 12 – Performance engineering at scale
- [ ] Profiling parallel programs
- [ ] Load balancing and granularity
- [ ] Overlapping communication and computation

🛠️ Project: find and fix a load imbalance in one of your parallel programs. Show the before and after timelines.

### Capstone
- [ ] A parallel application running on at least two processes across machines, or as separate containers

🛠️ Project: a scaling report with strong and weak scaling plots and an honest discussion of where the speedup stops.
