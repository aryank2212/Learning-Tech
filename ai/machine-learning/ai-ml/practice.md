# Practice: AI, LLMs & Machine / Deep Learning

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Fit y = 2x + 1 by gradient descent in NumPy.
- [ ] Split the iris dataset and report test accuracy.
- [ ] Plot underfitting and overfitting with polynomial models.

## Level 2 — Medium (apply it)

- [ ] Build a neural network from scratch that learns XOR.
- [ ] Train an MNIST classifier in PyTorch to 97% or better on the test set.
- [ ] Fine-tune a small transformer for sentiment analysis.

## Level 3 — Hard (build and explain)

- [ ] Train a small GPT on a text you choose.
- [ ] LoRA fine-tune a 1B-parameter model and evaluate it honestly.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What is overfitting?

   <details><summary>Show answer</summary>

   The model learns noise and quirks of the training data, so it does worse on new data.

   </details>

2. What does gradient descent do?

   <details><summary>Show answer</summary>

   It repeatedly moves the parameters a small step in the direction that reduces the loss (the negative gradient).

   </details>

3. What does attention do in a transformer?

   <details><summary>Show answer</summary>

   It lets each token weigh and combine information from other tokens, using queries, keys and values.

   </details>

4. Why use LoRA for fine-tuning?

   <details><summary>Show answer</summary>

   It trains small low-rank adapter matrices instead of all the weights, which makes fine-tuning much cheaper.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
