# Practice: PyTorch

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Create a 3×3 tensor, compute its transpose and its matrix product with itself, and check the result against NumPy.
- [ ] Use autograd to compute dy/dx for y = x³ + 2x at x = 2, and check it by hand (the answer is 14).
- [ ] Move a tensor to the GPU if one is available, and print its device.

## Level 2 — Medium (apply it)

- [ ] Train an MLP on a synthetic two-moons dataset to above 95% validation accuracy, using a proper train/validation split.
- [ ] Write a custom `Dataset` and `DataLoader` for a CSV file, with shuffling and batching.
- [ ] Add a learning-rate scheduler and early stopping to a training loop, and plot the loss curves.

## Level 3 — Hard (build and explain)

- [ ] Fine-tune a pretrained ResNet on a small image dataset, and compare its accuracy with a network trained from scratch.
- [ ] Implement single-head self-attention from scratch, and check it against `torch.nn.functional.scaled_dot_product_attention`.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What does `loss.backward()` do?

   <details><summary>Show answer</summary>

   It computes the gradient of the loss with respect to every tensor that has `requires_grad=True`, and adds the results to each tensor's `.grad`.

   </details>

2. Why call `optimizer.zero_grad()` on every step?

   <details><summary>Show answer</summary>

   Gradients accumulate by default. Without clearing them, each step would add to the gradients of the previous step.

   </details>

3. What's the difference between `model.train()` and `model.eval()`?

   <details><summary>Show answer</summary>

   They switch layers such as dropout and batch normalisation between training and inference behaviour. They don't turn off gradient tracking; `torch.no_grad()` or `torch.inference_mode()` does that.

   </details>

4. Why load checkpoints with `torch.load(path, weights_only=True)`?

   <details><summary>Show answer</summary>

   Loading an arbitrary pickle can run code. `weights_only=True` restricts loading to tensors and safe types, and it is the default in recent PyTorch versions.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
