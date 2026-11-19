# Practice: Python

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Print a multiplication table up to 12×12.
- [ ] Count word frequencies in a text file.
- [ ] Convert temperatures between Celsius and Fahrenheit, with tests.

## Level 2 — Medium (apply it)

- [ ] Read a CSV with the `csv` module and total the amounts per category.
- [ ] Write a decorator that memoises a function.
- [ ] Write a shape class hierarchy with an abstract base class.

## Level 3 — Hard (build and explain)

- [ ] Build an async web scraper with `asyncio` and `httpx` that respects rate limits.
- [ ] Implement Huffman coding using a heap.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What does `[1, 2, 3][-1]` return?

   <details><summary>Show answer</summary>

   `3`. Negative indexes count from the end.

   </details>

2. Why is `def f(x, items=[])` risky?

   <details><summary>Show answer</summary>

   The default list is created once and shared by every call. Use `items=None` and create a fresh list inside.

   </details>

3. What's the difference between a list and a tuple?

   <details><summary>Show answer</summary>

   Lists are mutable. Tuples are immutable, and are hashable if their items are.

   </details>

4. What does the GIL do in CPython?

   <details><summary>Show answer</summary>

   It lets only one thread run Python bytecode at a time, so CPU-bound threads don't run in parallel. Use multiprocessing or native extensions for that.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
