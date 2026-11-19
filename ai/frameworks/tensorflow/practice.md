# Practice: TensorFlow and Keras

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Create a `tf.Variable` and use `GradientTape` to find dy/dx for y = x² + 3x at x = 2 (the answer is 7).
- [ ] Build a `Sequential` model that learns XOR, and train it.
- [ ] Print `model.summary()` and verify the parameter count by hand.

## Level 2 — Medium (apply it)

- [ ] Build a `tf.data` pipeline with `shuffle`, `batch` and `prefetch` for a synthetic dataset, and train with `fit`.
- [ ] Add `EarlyStopping` and `ModelCheckpoint` callbacks, and reload the best saved model.
- [ ] Write a custom training loop with `GradientTape`, and compare its result with `fit`.

## Level 3 — Hard (build and explain)

- [ ] Fine-tune a `keras.applications` model on a small image dataset with augmentation layers.
- [ ] Convert a trained model to LiteRT with quantisation, and compare accuracy, size and speed with the original.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What does `@tf.function` do?

   <details><summary>Show answer</summary>

   It traces Python code into a TensorFlow graph, which is faster and can be exported. Python side effects inside it run only while the function is being traced, not on every call.

   </details>

2. What's the difference between the Keras `Sequential` and Functional APIs?

   <details><summary>Show answer</summary>

   `Sequential` is a straight stack of layers. The Functional API builds any graph of layers: several inputs and outputs, branches, and shared layers.

   </details>

3. What does `dataset.prefetch()` do?

   <details><summary>Show answer</summary>

   It prepares the next batches while the model is working on the current one, so the accelerator doesn't wait for input.

   </details>

4. What does multi-backend Keras 3 mean?

   <details><summary>Show answer</summary>

   The same Keras code can run on TensorFlow, JAX or PyTorch, chosen with the `KERAS_BACKEND` setting. Code that uses backend-specific operations won't carry over.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
