# Practice: ML libraries in other languages

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] List the ML libraries available in your favourite non-Python language, and mark which ones can train and which only run models.
- [ ] Export a scikit-learn pipeline to ONNX with `skl2onnx`, and print the model's input and output names.
- [ ] Run an ONNX model with ONNX Runtime in Python, and compare its output with the original model's.

## Level 2 — Medium (apply it)

- [ ] Run the same ONNX model from a second language (JavaScript, Rust with `ort`, Java, C# or Go), and show the outputs agree to within 1e-5.
- [ ] Train the iris classifier in R (`tidymodels`), Julia (MLJ) or Rust (`linfa`), and compare accuracy with scikit-learn.
- [ ] Load a small model in a browser page with TensorFlow.js or Transformers.js, and display its predictions.

## Level 3 — Hard (build and explain)

- [ ] Build an HTTP service in Go, Rust, Java or C# that serves an ONNX model, with an automated parity test against Python.
- [ ] Quantise a model to int8, and measure accuracy loss, latency and file size in two runtimes.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What is ONNX?

   <details><summary>Show answer</summary>

   An open file format for trained machine-learning models, so a model trained in one framework can be run by another runtime or in another language.

   </details>

2. Why is preprocessing the most common bug when you port a model?

   <details><summary>Show answer</summary>

   The model weights are identical, but input scaling, tokenising or resizing differs, so the inputs the model sees are different and the outputs drift. Test with the same raw inputs in both languages.

   </details>

3. When would you serve with ONNX Runtime instead of the training framework?

   <details><summary>Show answer</summary>

   When you only need inference and want smaller dependencies, lower latency or a different language, because ONNX Runtime has bindings for C, C++, C#, Java, JavaScript and more.

   </details>

4. What does quantisation trade off?

   <details><summary>Show answer</summary>

   It makes models smaller and faster and uses less memory, in return for some loss of accuracy, which you should measure.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
