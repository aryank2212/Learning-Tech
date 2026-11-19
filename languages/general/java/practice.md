# Practice: Java

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Write a bank account with deposit, withdraw and an exception for overdrafts.
- [ ] Read numbers from stdin and print the median.
- [ ] Write an `enum Day` with a method `isWeekend()`.

## Level 2 — Medium (apply it)

- [ ] Build an LRU cache using `LinkedHashMap`.
- [ ] Use streams to group employees by department and compute average salaries.
- [ ] Write JUnit tests for a `Calculator` class.

## Level 3 — Hard (build and explain)

- [ ] Write a parallel merge sort using `ForkJoinPool`.
- [ ] Build a REST API with Spring Boot that stores items in H2.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What's the difference between `==` and `.equals()` on Strings?

   <details><summary>Show answer</summary>

   `==` compares references (whether they're the same object). `.equals()` compares the text.

   </details>

2. What does `final` do on a variable and on a class?

   <details><summary>Show answer</summary>

   On a variable, it can be assigned once. On a class, it can't be subclassed.

   </details>

3. What is a checked exception?

   <details><summary>Show answer</summary>

   An exception the compiler forces you to catch or declare. These are subclasses of `Exception` other than `RuntimeException`.

   </details>

4. What is a virtual thread (Java 21)?

   <details><summary>Show answer</summary>

   A lightweight thread managed by the JVM and scheduled onto a few operating-system threads. It lets you write simple blocking code that scales to many concurrent tasks.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
