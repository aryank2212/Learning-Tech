# /// script
# requires-python = ">=3.11"
# dependencies = ["torch"]
# ///
"""A complete training loop: data -> model -> loss -> optimizer -> validation -> save/load.

Run:  uv run 02_mlp_two_moons.py
"""
import math
import tempfile
from pathlib import Path

import torch
from torch import nn

torch.manual_seed(0)
device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
print("device:", device)


def make_moons(n, noise=0.15):
    """Two interleaving half-circles, generated with torch so no extra libraries are needed."""
    t = torch.rand(n // 2) * math.pi
    top = torch.stack([torch.cos(t), torch.sin(t)], dim=1)
    bottom = torch.stack([1 - torch.cos(t), 0.5 - torch.sin(t)], dim=1)
    X = torch.cat([top, bottom]) + noise * torch.randn(n, 2)
    y = torch.cat([torch.zeros(n // 2), torch.ones(n // 2)])
    perm = torch.randperm(n)
    return X[perm], y[perm]


X, y = make_moons(1000)
X_train, y_train, X_val, y_val = X[:800], y[:800], X[800:], y[800:]
X_train, y_train, X_val, y_val = (t.to(device) for t in (X_train, y_train, X_val, y_val))

model = nn.Sequential(nn.Linear(2, 32), nn.ReLU(), nn.Linear(32, 32), nn.ReLU(), nn.Linear(32, 1)).to(device)
loss_fn = nn.BCEWithLogitsLoss()           # expects raw scores (logits), not probabilities
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-2)


def accuracy(inputs, targets):
    model.eval()                            # switches dropout/batch-norm to inference behaviour
    with torch.inference_mode():            # no gradient tracking: faster and uses less memory
        pred = (model(inputs).squeeze(1) > 0).float()
    return (pred == targets).float().mean().item()


for epoch in range(1, 301):
    model.train()
    optimizer.zero_grad()
    loss = loss_fn(model(X_train).squeeze(1), y_train)
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
        print(f"epoch {epoch:3d}  loss {loss.item():.3f}  val accuracy {accuracy(X_val, y_val):.3f}")

# Save only the weights, then load them back safely.
with tempfile.TemporaryDirectory() as d:
    path = Path(d) / "moons.pt"
    torch.save(model.state_dict(), path)
    clone = nn.Sequential(nn.Linear(2, 32), nn.ReLU(), nn.Linear(32, 32), nn.ReLU(), nn.Linear(32, 1)).to(device)
    clone.load_state_dict(torch.load(path, weights_only=True))   # weights_only avoids running pickled code
    clone.eval()
    with torch.inference_mode():
        same = torch.allclose(clone(X_val), model.eval()(X_val))
    print("reloaded model matches:", same)
