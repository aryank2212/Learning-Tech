# Practice: DSA & Advanced DSA

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Reverse a singly linked list.
- [ ] Solve two-sum with a hash map.
- [ ] Check balanced brackets with a stack.

## Level 2 — Medium (apply it)

- [ ] Find the k most frequent elements using a heap.
- [ ] Find the shortest path through a grid with BFS.
- [ ] Find the longest increasing subsequence in O(n log n).

## Level 3 — Hard (build and explain)

- [ ] Build a segment tree with range sum and point update.
- [ ] Solve an assignment problem with min-cost max-flow.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What's the time complexity of binary search?

   <details><summary>Show answer</summary>

   O(log n), on a sorted array.

   </details>

2. When is a hash-map lookup O(1)?

   <details><summary>Show answer</summary>

   On average, with a good hash function and a bounded load factor. The worst case is O(n).

   </details>

3. Why use a heap to find the k largest items?

   <details><summary>Show answer</summary>

   A min-heap of size k keeps the k largest seen so far, giving O(n log k) overall.

   </details>

4. What must be true of edge weights for Dijkstra's algorithm?

   <details><summary>Show answer</summary>

   They must be non-negative. With negative edges use Bellman–Ford.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
