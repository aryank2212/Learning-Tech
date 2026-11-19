# Practice: Statistical Computing

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Compute the mean, median and interquartile range of a sample.
- [ ] Simulate 1,000 coin flips and plot the running proportion.
- [ ] Compute a 95% confidence interval for a mean using the t-distribution.

## Level 2 — Medium (apply it)

- [ ] Compute a bootstrap confidence interval for a median.
- [ ] Fit a logistic regression and report odds ratios.
- [ ] Run a permutation test for two groups.

## Level 3 — Hard (build and explain)

- [ ] Find the maximum-likelihood estimates for a gamma distribution using optimisation.
- [ ] Fit a Beta–Binomial model in PyMC and check convergence.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What does a 95% confidence interval mean?

   <details><summary>Show answer</summary>

   If you repeated the procedure many times, about 95% of the intervals would contain the true parameter.

   </details>

2. What is a p-value?

   <details><summary>Show answer</summary>

   The probability of data at least this extreme if the null hypothesis were true. It is not the probability that the null hypothesis is true.

   </details>

3. Why use the bootstrap?

   <details><summary>Show answer</summary>

   It estimates uncertainty by resampling the data with replacement, without strong assumptions about the distribution.

   </details>

4. What is the multiple-testing problem?

   <details><summary>Show answer</summary>

   Run many tests and some will look significant by chance. Control it with Bonferroni or the false discovery rate (Benjamini–Hochberg).

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
