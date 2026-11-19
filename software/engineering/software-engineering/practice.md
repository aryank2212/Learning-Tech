# Practice: Software Engineering

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Write user stories with acceptance criteria for a to-do app.
- [ ] Write five unit tests for one function.
- [ ] Write a README that gets a stranger running the project in five steps.

## Level 2 — Medium (apply it)

- [ ] Write a GitHub Actions workflow that runs your tests on every push.
- [ ] Refactor duplicated code into one function, keeping the tests green.
- [ ] Write an ADR that chooses a database for a project.

## Level 3 — Hard (build and explain)

- [ ] Write a blameless postmortem for a simulated outage.
- [ ] Add a feature flag and plan a canary rollout.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What is the test pyramid?

   <details><summary>Show answer</summary>

   Many fast unit tests, fewer integration tests, and a small number of slow end-to-end tests.

   </details>

2. Why use feature flags?

   <details><summary>Show answer</summary>

   They separate deploying code from releasing a feature, so you can roll out gradually and switch it off quickly.

   </details>

3. What's the difference between merge and rebase?

   <details><summary>Show answer</summary>

   Merge keeps history and adds a merge commit. Rebase rewrites your commits on top of another base for a linear history. Don't rebase branches others share.

   </details>

4. What is a blameless postmortem?

   <details><summary>Show answer</summary>

   A write-up of an incident that focuses on system and process causes and what to improve, not on punishing individuals.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
