# Parallel & Distributed Computing

Running work on many cores and many machines at once: shared-memory threads, message passing, GPUs, data-parallel frameworks, and the hard parts of distributed systems (failures, clocks, consistency and consensus). It connects the [CUDA](../languages/cuda/README.md) and [computer architecture](../computer-architecture/README.md) sections with [system architecture](../system-architecture/README.md) and [big data](../predictive-big-data-analytics/README.md).

## Prerequisites
- C or C++ at Level 2 or better (for OpenMP and MPI)
- [Operating systems](../operating-systems/README.md) phases 1–3 (processes, threads, locks)
- [Computer networking](../computer-networking/README.md) basics (sockets, latency)

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
