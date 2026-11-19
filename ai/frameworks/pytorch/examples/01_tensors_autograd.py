# /// script
# requires-python = ">=3.11"
# dependencies = ["torch"]
# ///
"""Tensors and autograd: the two ideas everything in PyTorch is built on.

Run:  uv run 01_tensors_autograd.py
(On a machine without an NVIDIA GPU, see the CPU-only install in the README.)
"""
import torch

torch.manual_seed(0)

# --- tensors ---------------------------------------------------------------
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.ones(2, 2)
print("a @ b =\n", a @ b)
print("broadcasting a + [10, 20] =\n", a + torch.tensor([10.0, 20.0]))
print("shape, dtype, device:", tuple(a.shape), a.dtype, a.device)
print("reshape/view:", a.reshape(4).tolist(), "| transpose:", a.T.tolist())

# --- autograd --------------------------------------------------------------
x = torch.tensor(2.0, requires_grad=True)
y = x**3 + 2 * x            # dy/dx = 3x^2 + 2 = 14 at x = 2
y.backward()
print("dy/dx at x=2:", x.grad.item(), "(expected 14.0)")

# --- linear regression with autograd only (no nn, no optimizer) -------------
true_w, true_b = 3.0, 2.0
X = torch.linspace(-1, 1, 100).unsqueeze(1)
Y = true_w * X + true_b + 0.05 * torch.randn_like(X)

w = torch.zeros(1, requires_grad=True)
bias = torch.zeros(1, requires_grad=True)
lr = 0.1
for step in range(200):
    loss = ((X * w + bias - Y) ** 2).mean()
    loss.backward()                      # fills w.grad and bias.grad
    with torch.no_grad():                # update without tracking the update itself
        w -= lr * w.grad
        bias -= lr * bias.grad
    w.grad.zero_()                       # gradients accumulate, so clear them
    bias.grad.zero_()

print(f"learned w={w.item():.2f}, b={bias.item():.2f}  (true {true_w}, {true_b})")
