# Practice: SQL *(suggested)*

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Select every customer who lives in Berlin.
- [ ] Count orders per month.
- [ ] Insert a row, then update it.

## Level 2 — Medium (apply it)

- [ ] Join three tables to list order totals per customer.
- [ ] Find customers with no orders, using a LEFT JOIN and IS NULL.
- [ ] Use a CTE to find the top three products in each category.

## Level 3 — Hard (build and explain)

- [ ] Write a window-function query that gives a running total and rank per region.
- [ ] Design a library schema in 3NF and justify one index with EXPLAIN output.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What does `WHERE col = NULL` return?

   <details><summary>Show answer</summary>

   No rows. A comparison with NULL is unknown, not true. Use `IS NULL`.

   </details>

2. What's the difference between INNER JOIN and LEFT JOIN?

   <details><summary>Show answer</summary>

   INNER JOIN keeps only matching rows. LEFT JOIN keeps every row from the left table and fills the right side with NULLs when there's no match.

   </details>

3. What does an index do, and what does it cost?

   <details><summary>Show answer</summary>

   It speeds up lookups and sorting on the indexed columns. It costs storage and slows down writes.

   </details>

4. How do `WHERE` and `HAVING` differ?

   <details><summary>Show answer</summary>

   `WHERE` filters rows before grouping. `HAVING` filters groups after aggregation.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
