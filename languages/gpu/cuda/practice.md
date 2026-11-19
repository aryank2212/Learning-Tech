# Practice: CUDA

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Write a vector-add kernel and check the result on the CPU.
- [ ] Square every element of an array on the GPU.
- [ ] Print your GPU's properties with `cudaGetDeviceProperties`.

## Level 2 — Medium (apply it)

- [ ] Write a parallel sum using shared memory.
- [ ] Build a histogram with atomic operations.
- [ ] Time a kernel with CUDA events.

## Level 3 — Hard (build and explain)

- [ ] Write a tiled matrix multiply, and report what fraction of peak it reaches.
- [ ] Write a prefix sum (scan) that works across many blocks.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What is a warp?

   <details><summary>Show answer</summary>

   A group of 32 threads that execute together in lockstep on an NVIDIA GPU.

   </details>

2. How do you compute a thread's global index in one dimension?

   <details><summary>Show answer</summary>

   `blockIdx.x * blockDim.x + threadIdx.x`.

   </details>

3. What is memory coalescing?

   <details><summary>Show answer</summary>

   When neighbouring threads in a warp access neighbouring addresses, the hardware combines the reads into a few memory transactions.

   </details>

4. Why use shared memory in matrix multiply?

   <details><summary>Show answer</summary>

   To load a tile from slow global memory once and reuse it across the threads in a block, which cuts global memory traffic.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
