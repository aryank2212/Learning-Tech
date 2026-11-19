# Practice: C++

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Write a `Stack<T>` class with `push`, `pop` and `top`.
- [ ] Sum a `std::vector` with `std::accumulate`.
- [ ] Read grades from a file into a `std::map` and print each student's average.

## Level 2 — Medium (apply it)

- [ ] Write a `unique_ptr`-like RAII wrapper with move semantics.
- [ ] Remove duplicates from a sorted vector using `<algorithm>`.
- [ ] Write one template function that works for `int` and `std::string`.

## Level 3 — Hard (build and explain)

- [ ] Write a lock-free single-producer, single-consumer ring buffer.
- [ ] Write a ray tracer for spheres that outputs a PPM image.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What does RAII mean?

   <details><summary>Show answer</summary>

   Resource Acquisition Is Initialisation: tie a resource's lifetime to an object's lifetime, so its destructor releases the resource automatically.

   </details>

2. What's the difference between `unique_ptr` and `shared_ptr`?

   <details><summary>Show answer</summary>

   `unique_ptr` has one owner and can only be moved. `shared_ptr` uses reference counting so several owners can share the object.

   </details>

3. What is the rule of zero (and of five)?

   <details><summary>Show answer</summary>

   Rule of zero: design classes so they need no custom special members. Rule of five: if you define any of destructor, copy/move constructors or copy/move assignment, define or delete all five.

   </details>

4. Why can `v.push_back(x)` invalidate iterators?

   <details><summary>Show answer</summary>

   It may reallocate the vector's storage. Old iterators, pointers and references then point to freed memory.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
