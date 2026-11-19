# Practice: Computer Architecture

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Write RISC-V code that sums 1 to 10.
- [ ] Compute the CPI of a five-stage pipeline with no hazards.
- [ ] Explain the difference between direct-mapped and fully associative caches.

## Level 2 — Medium (apply it)

- [ ] Write a cache simulator and report the hit rate for a given access pattern.
- [ ] Count the data hazards in a six-instruction sequence, then add forwarding.
- [ ] Simulate a two-bit branch predictor on a recorded trace.

## Level 3 — Hard (build and explain)

- [ ] Build a five-stage pipelined RISC-V subset in Verilog.
- [ ] Write an AVX loop and measure its speedup over scalar code.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What does CPI mean?

   <details><summary>Show answer</summary>

   Cycles per instruction: the average number of clock cycles an instruction takes.

   </details>

2. What are the three kinds of pipeline hazard?

   <details><summary>Show answer</summary>

   Structural, data and control hazards.

   </details>

3. What's the difference between temporal and spatial locality?

   <details><summary>Show answer</summary>

   Temporal: recently used data is likely to be used again soon. Spatial: data near recently used addresses is likely to be used soon.

   </details>

4. What is false sharing?

   <details><summary>Show answer</summary>

   Different cores update different variables that sit on the same cache line, so coherence traffic slows them all down.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
