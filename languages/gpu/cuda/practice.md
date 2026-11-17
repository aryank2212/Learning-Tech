# Practice: CUDA

Work through the levels in order. Don't open a solution until you've tried each task for at least 30 minutes.

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

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
