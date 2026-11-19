# Practice: Go *(suggested)*

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Print the first 20 Fibonacci numbers.
- [ ] Write a function that returns `(value, error)` and handle both.
- [ ] Sort a slice of structs with `sort.Slice`.

## Level 2 — Medium (apply it)

- [ ] Write a worker pool with goroutines and channels that processes 1000 jobs.
- [ ] Write an HTTP handler that returns JSON, and test it with `httptest`.

## Level 3 — Hard (build and explain)

- [ ] Write a token-bucket rate limiter.
- [ ] Write a concurrent crawler limited to depth 2, with context cancellation.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. How do Go functions report errors?

   <details><summary>Show answer</summary>

   They return an `error` value as the last result, and callers check `if err != nil`.

   </details>

2. What does `go f()` do?

   <details><summary>Show answer</summary>

   It starts `f` in a new goroutine, running concurrently with the caller.

   </details>

3. What happens if you write to a nil map?

   <details><summary>Show answer</summary>

   It panics. Reading from a nil map returns zero values. Create maps with `make`.

   </details>

4. Why pass a `context.Context`?

   <details><summary>Show answer</summary>

   To carry cancellation, deadlines and request-scoped values across function calls and goroutines.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
