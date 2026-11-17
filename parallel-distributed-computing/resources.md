# Parallel & distributed computing resources

## Books
| | Book | Notes |
|---|---|---|
| ⭐💲 | *The Art of Multiprocessor Programming* — Herlihy & Shavit | The standard text on concurrent data structures |
| ⭐🆓 | *Is Parallel Programming Hard, And, If So, What Can You Do About It?* — Paul McKenney | [Free online](https://mirrors.edge.kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.html) |
| 💲 | *Introduction to Parallel Computing* — Grama, Gupta, Karypis, Kumar | Broad and practical |
| 💲 | *Using OpenMP* — Chapman, Jost, van der Pas | The OpenMP reference in book form |
| 💲 | *Using MPI* — Gropp, Lusk, Skjellum | The MPI reference in book form |
| 🆓 | *Distributed Systems* (3rd ed) — van Steen & Tanenbaum | [Free online](https://www.distributed-systems.net/index.php/books/ds3/) |
| 💲 | *Designing Data-Intensive Applications* — Martin Kleppmann | See [system architecture](../system-architecture/resources.md) |

## Tutorials and documentation
- ⭐🆓 [LLNL MPI tutorial](https://hpc-tutorials.llnl.gov/mpi/)
- ⭐🆓 [LLNL OpenMP tutorial](https://hpc-tutorials.llnl.gov/openmp/)
- 🆓 [OpenMP specifications and resources](https://www.openmp.org/)
- 🆓 [Open MPI documentation](https://www.open-mpi.org/)
- 🆓 [hwloc](https://www.open-mpi.org/projects/hwloc/) — hardware topology
- 🆓 [Dask documentation](https://docs.dask.org/)
- 🆓 [Ray documentation](https://docs.ray.io/)
- 🆓 [Raft consensus](https://raft.github.io/) — the paper, an interactive visualisation, and implementations
- 🆓 [Jepsen](https://jepsen.io/) — analyses of how real distributed databases fail

## Courses and lectures
- 🆓 Stanford and Berkeley parallel-computing course materials — search "CS 149 parallel computing" and "CS 267 applications of parallel computers"
- 🆓 [NVIDIA Deep Learning Institute](https://www.nvidia.com/en-us/training/) — GPU parallel programming (see [CUDA](../languages/cuda/README.md))

## Tools
- [TLA+](https://lamport.azurewebsites.net/tla/tla.html) — specify and model-check distributed algorithms
- [OpenCL](https://www.khronos.org/opencl/) — standard for heterogeneous parallel programming
- [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/) — running parallel services at scale

## Classic papers
- Amdahl, *Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities* (1967)
- Gustafson, *Reevaluating Amdahl's Law* (CACM, 1988)
- Lamport, *Time, Clocks, and the Ordering of Events in a Distributed System* (CACM, 1978)
- Herlihy & Wing, *Linearizability: A Correctness Condition for Concurrent Objects* (TOPLAS, 1990)
- Lamport, *The Part-Time Parliament* (TOCS, 1998) — Paxos
- Dean & Ghemawat, *MapReduce: Simplified Data Processing on Large Clusters* (OSDI, 2004)

## Research
See [research/directions.md](../research/directions.md#parallel-and-distributed-computing) for open questions.
