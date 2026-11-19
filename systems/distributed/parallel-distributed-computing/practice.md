# Practice: Parallel & Distributed Computing

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Compute Amdahl's speedup for a 90% parallel program on 4 and on 16 cores.
- [ ] Write an OpenMP loop that sums an array with a reduction.
- [ ] Explain a race condition with a short example.

## Level 2 — Medium (apply it)

- [ ] Write an MPI program that sums an array across four processes.
- [ ] Build a parallel histogram with per-thread buffers.
- [ ] Simulate Lamport clocks for three processes.

## Level 3 — Hard (build and explain)

- [ ] Simulate leader election with random failures, Raft-style.
- [ ] Run word count with Dask on 1 GB of text and report the scaling.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. State Amdahl's law.

   <details><summary>Show answer</summary>

   Speedup ≤ 1 / ((1 − p) + p / N), where p is the parallel fraction and N is the number of processors.

   </details>

2. What is a race condition?

   <details><summary>Show answer</summary>

   A bug where the result depends on the timing of unsynchronised accesses to shared data.

   </details>

3. What does `MPI_Allreduce` do?

   <details><summary>Show answer</summary>

   It combines values from all ranks (for example, a sum) and gives the result to every rank.

   </details>

4. What is a Lamport clock?

   <details><summary>Show answer</summary>

   A logical counter that orders events by causality. Increment on each event, and on receiving a message set it to max(local, received) + 1.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
