# Practice: Operating Systems

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Use `fork()` to print the parent and child process IDs.
- [ ] List the steps of a context switch.
- [ ] Compute the average turnaround time for four jobs under FCFS.

## Level 2 — Medium (apply it)

- [ ] Write a round-robin scheduler simulator.
- [ ] Solve producer–consumer with semaphores.
- [ ] Simulate FIFO and LRU page replacement on one trace.

## Level 3 — Hard (build and explain)

- [ ] Write a malloc with coalescing of free blocks.
- [ ] Add a system call to xv6 and call it from a user program.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What does `fork()` return in the child process?

   <details><summary>Show answer</summary>

   0. The parent receives the child's process ID.

   </details>

2. What are the four conditions for deadlock?

   <details><summary>Show answer</summary>

   Mutual exclusion, hold and wait, no preemption, and circular wait.

   </details>

3. Why does demand paging help?

   <details><summary>Show answer</summary>

   Only the pages a program actually uses are loaded, which saves memory and speeds up start-up.

   </details>

4. What is a context switch, and why is it costly?

   <details><summary>Show answer</summary>

   Saving one thread's state and loading another's. The cost includes saving and restoring registers and disturbing caches and the TLB.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
