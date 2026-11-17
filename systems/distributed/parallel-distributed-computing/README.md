# Parallel & Distributed Computing

Running work on many cores and many machines at once: shared-memory threads, message passing, GPUs, data-parallel frameworks, and the hard parts of distributed systems (failures, clocks, consistency and consensus). It connects the [CUDA](../../../languages/gpu/cuda/README.md) and [computer architecture](../../../foundations/hardware/computer-architecture/README.md) sections with [system architecture](../../architecture/system-architecture/README.md) and [big data](../../../data/analytics/predictive-big-data-analytics/README.md).

## Prerequisites
- C or C++ at Level 2 or better (for OpenMP and MPI)
- [Operating systems](../../kernels/operating-systems/README.md) phases 1–3 (processes, threads, locks)
- [Computer networking](../../networks/computer-networking/README.md) basics (sockets, latency)

## Install
```bash
sudo pacman -S --needed gcc openmpi hwloc numactl pocl opencl-headers clinfo
```
- **OpenMP** comes with `gcc`. Compile with `gcc -fopenmp`.
- **Open MPI** runs parallel processes, on one machine or several: `mpirun -np 4 ./program`.
- **hwloc** shows the machine's topology. **numactl** controls memory placement on multi-socket machines.
- **pocl** provides OpenCL on the CPU, so you can run OpenCL code without a GPU. **clinfo** lists the OpenCL platforms on your machine.

Python tools, when you move to big data:
```bash
mkdir -p ~/parallel-lab && cd ~/parallel-lab
uv init parallel-lab && cd parallel-lab
uv add dask ray
```

Check your core count: `nproc` and `lscpu`. Then write your scaling plots against it.

## Weekly rhythm
- Each week: one pattern, implemented in two ways (for example, threads and processes), then measured.
- Every timing gets a graph of speedup against the number of cores.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, tutorials, tools, papers

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- Parallel code is easy to make slower. Measure speedup at several core counts before you celebrate.
- Distributed systems are mostly about failure. Start by asking what happens when a machine dies at the worst moment.
- Read Lamport's papers slowly. They're short, and their ideas underpin much of the field.
