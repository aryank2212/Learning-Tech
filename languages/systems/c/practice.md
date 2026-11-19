# Practice: C

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Reverse a string in place.
- [ ] Print the transpose of a 3×3 matrix.
- [ ] Count the lines in a file using `fgets`.

## Level 2 — Medium (apply it)

- [ ] Implement a dynamic array with push and pop, using `realloc`.
- [ ] Write a bounded string copy that never overflows.
- [ ] Parse command-line options with `getopt`.

## Level 3 — Hard (build and explain)

- [ ] Write a simple memory-pool allocator and test it with valgrind.
- [ ] Build a multithreaded word counter with pthreads and a mutex.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What does `sizeof(int)` give on most modern systems?

   <details><summary>Show answer</summary>

   4 (bytes). The size is implementation-defined, so check with `sizeof` rather than assuming.

   </details>

2. What's wrong with `char *s = "hi"; s[0] = 'H';`?

   <details><summary>Show answer</summary>

   String literals are read-only, so writing to one is undefined behaviour (often a crash). Use `char s[] = "hi";` for a modifiable copy.

   </details>

3. What's the difference between `malloc` and `calloc`?

   <details><summary>Show answer</summary>

   `calloc(n, size)` zero-fills the memory and checks the multiplication for overflow. `malloc` returns uninitialised memory.

   </details>

4. What is undefined behaviour? Give one example.

   <details><summary>Show answer</summary>

   Code the standard doesn't define, so the compiler may assume it never happens and produce surprising results. Examples: signed integer overflow, using memory after `free`.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
