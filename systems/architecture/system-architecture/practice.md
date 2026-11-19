# Practice: System Architecture

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] List the trade-offs of SQL and NoSQL for a to-do app.
- [ ] Estimate storage for a million users posting ten messages a day.
- [ ] Draw a three-tier architecture and label each tier.

## Level 2 — Medium (apply it)

- [ ] Design a URL shortener: requirements, API and data model.
- [ ] Find the single points of failure in a given diagram.
- [ ] Add caching to a read-heavy API and measure the difference.

## Level 3 — Hard (build and explain)

- [ ] Design a chat system for ten million users, including how messages fan out.
- [ ] Write an ADR for splitting a monolith into two services.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What's the difference between latency and throughput?

   <details><summary>Show answer</summary>

   Latency is the time one request takes. Throughput is how many requests are handled per unit of time.

   </details>

2. What does the CAP theorem say?

   <details><summary>Show answer</summary>

   During a network partition, a distributed system must choose between consistency and availability.

   </details>

3. What is a circuit breaker?

   <details><summary>Show answer</summary>

   A pattern that stops calling a failing dependency for a while. It fails fast and prevents cascading failures.

   </details>

4. Why prefer idempotent operations in distributed systems?

   <details><summary>Show answer</summary>

   Retries become safe: repeating the operation has the same effect as doing it once.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
