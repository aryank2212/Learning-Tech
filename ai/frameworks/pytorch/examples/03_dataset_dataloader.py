# /// script
# requires-python = ">=3.11"
# dependencies = ["torch"]
# ///
"""Dataset + DataLoader, a learning-rate schedule, early stopping and optional mixed precision.

Run:  uv run 03_dataset_dataloader.py
"""
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset, random_split

torch.manual_seed(0)
device = "cuda" if torch.cuda.is_available() else "cpu"


class Blobs(Dataset):
    """Three Gaussian clusters. A Dataset only needs __len__ and __getitem__."""

    def __init__(self, n_per_class=300):
        centers = torch.tensor([[-2.0, -2.0], [2.0, -2.0], [0.0, 2.5]])
        self.x = torch.cat([c + torch.randn(n_per_class, 2) for c in centers])
        self.y = torch.arange(3).repeat_interleave(n_per_class)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, i):
        return self.x[i], self.y[i]


data = Blobs()
train_set, val_set = random_split(data, [0.8, 0.2], generator=torch.Generator().manual_seed(0))
train_loader = DataLoader(train_set, batch_size=32, shuffle=True)
val_loader = DataLoader(val_set, batch_size=128)

model = nn.Sequential(nn.Linear(2, 16), nn.ReLU(), nn.Linear(16, 3)).to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-2)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=30)

use_amp = device == "cuda"                              # mixed precision only helps on a GPU
scaler = torch.amp.GradScaler("cuda", enabled=use_amp)


def evaluate():
    model.eval()
    total_loss, correct = 0.0, 0
    with torch.inference_mode():
        for xb, yb in val_loader:
            xb, yb = xb.to(device), yb.to(device)
            logits = model(xb)
            total_loss += loss_fn(logits, yb).item() * len(yb)
            correct += (logits.argmax(1) == yb).sum().item()
    return total_loss / len(val_set), correct / len(val_set)


best_loss, best_state, patience, bad = float("inf"), None, 5, 0
for epoch in range(1, 31):
    model.train()
    for xb, yb in train_loader:
        xb, yb = xb.to(device), yb.to(device)
        optimizer.zero_grad()
        with torch.autocast(device_type="cuda", dtype=torch.float16, enabled=use_amp):
            loss = loss_fn(model(xb), yb)
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()
    scheduler.step()
    val_loss, val_acc = evaluate()
    if val_loss < best_loss - 1e-4:
        best_loss, bad = val_loss, 0
        best_state = {k: v.detach().clone() for k, v in model.state_dict().items()}
    else:
        bad += 1
        if bad >= patience:
            print(f"early stop at epoch {epoch}")
            break
    if epoch % 5 == 0:
        print(f"epoch {epoch:2d}  val loss {val_loss:.3f}  val accuracy {val_acc:.3f}")

model.load_state_dict(best_state)
print("final validation (loss, accuracy):", tuple(round(v, 3) for v in evaluate()))
