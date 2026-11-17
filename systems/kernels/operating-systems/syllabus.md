# Operating systems syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md).

### Phase 1 – What an OS does; processes
- [ ] Roles: abstraction, resource management, protection
- [ ] System calls and the user/kernel boundary
- [ ] Process states; process control block
- [ ] `fork`, `exec`, `wait`; orphans and zombies
- [ ] Context switching

🛠️ Project: a shell with pipes, redirection and job control (C).

### Phase 2 – CPU scheduling
- [ ] FIFO, shortest job first, round robin
- [ ] Multi-level feedback queue (MLFQ)
- [ ] Lottery and stride scheduling
- [ ] Linux's Completely Fair Scheduler (CFS) idea
- [ ] Real-time scheduling: rate-monotonic, earliest deadline first

🛠️ Project: a scheduler simulator (Python) that reports turnaround and response times.

### Phase 3 – Threads and concurrency
- [ ] Threads vs processes; POSIX threads (`pthread`)
- [ ] Race conditions and critical sections
- [ ] Mutexes, semaphores, condition variables, monitors
- [ ] Deadlock: the four conditions and the banker's algorithm
- [ ] Classic problems: readers–writers, dining philosophers

🛠️ Project: a thread-safe bounded buffer, plus a demo that deliberately deadlocks and then fixes it.

### Phase 4 – Memory management
- [ ] Address spaces; base-and-bounds; segmentation
- [ ] Paging, multi-level page tables, the TLB
- [ ] Page replacement: FIFO, LRU, Clock, optimal
- [ ] Thrashing and the working-set model
- [ ] Demand paging and copy-on-write

🛠️ Project: a custom `malloc` with free lists, first/best fit and coalescing.

### Phase 5 – File systems and storage
- [ ] Files, directories, inodes
- [ ] Crash consistency and journaling
- [ ] `fsck` and why it exists
- [ ] Block layer, I/O scheduling, SSD basics

🛠️ Project: a toy file system on top of FUSE (`libfuse`), or an inode-based disk image tool.

### Phase 6 – I/O and devices
- [ ] Interrupts, polling, and DMA
- [ ] Blocking vs non-blocking I/O
- [ ] `select`, `poll`, `epoll`; a first look at `io_uring`

🛠️ Project: an event-driven echo server with `epoll`.

### Phase 7 – Virtualisation and containers
- [ ] Virtual machines and hypervisors
- [ ] Namespaces (PID, mount, network, user)
- [ ] cgroups v2 for limiting CPU and memory
- [ ] How Docker combines these ideas

🛠️ Project: a mini container using `unshare` and cgroups v2 by hand.

### Phase 8 – Security and protection
- [ ] Privilege levels, permissions, capabilities
- [ ] ASLR, stack canaries, non-executable memory
- [ ] Sandboxing with `seccomp`

🛠️ Project: run a program under a `seccomp` filter that blocks network calls.

### Phase 9 – Kernel programming
- [ ] Loadable kernel modules (`insmod`, `rmmod`)
- [ ] Kernel debugging: `dmesg`, ftrace, perf
- [ ] eBPF and `bpftrace`

🛠️ Project: a `bpftrace` script that logs every process started, or a tiny kernel module (only in a VM).

### Phase 10 – Build your own OS (capstone)
- [ ] Work through xv6 labs, or follow Writing an OS in Rust
- [ ] Add a system call, or boot a kernel in QEMU that prints to the screen

🛠️ Project: add a new system call to xv6 and write a user program that calls it.
