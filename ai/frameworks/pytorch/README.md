# PyTorch

The most widely used framework for deep learning research and for open models. You write ordinary Python, PyTorch tracks the maths for you (automatic differentiation), and the same code runs on a CPU or a GPU.

## Why learn it
- **It reads like normal Python.** You can print a tensor, step through a model with a debugger, and see the error where it happens.
- **Most new models ship PyTorch code.** Papers, Hugging Face models and open-source projects use it, so you can read and reuse what you find.
- **It scales from a laptop to a cluster.** The same ideas carry from a ten-line model to multi-GPU training.

## Prerequisites
- Python at Level 2 (see [Python](../../../languages/general/python/README.md))
- NumPy-style array thinking, and what a derivative and a gradient are (see [maths](../../../foundations/mathematics/maths/syllabus.md), phases 1–4)
- The ideas in [AI, LLMs and ML](../../machine-learning/ai-ml/syllabus.md), phase 2 (neural networks) help, but you can learn them here

## Install
Pick the build that matches your machine. Use a project, not your system Python.

**Any machine, CPU only** (smaller download; fine for learning). In `pyproject.toml`:
```toml
[project]
name = "pytorch-lab"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["torch", "torchvision"]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true

[tool.uv.sources]
torch = { index = "pytorch-cpu" }
torchvision = { index = "pytorch-cpu" }
```
then run `uv sync`.

**NVIDIA GPU on Linux or Windows:**
```bash
uv init pytorch-lab --python 3.13 && cd pytorch-lab
uv add torch torchvision
```
On Linux the default wheel is a CUDA build, and it is large because it bundles the CUDA libraries. If you need a particular CUDA version, copy the exact command from the selector at [pytorch.org/get-started/locally](https://pytorch.org/get-started/locally/); the index name looks like `cu132` and changes as CUDA does.

**Apple Silicon:** the default wheel works, and PyTorch uses the GPU through `mps`. **AMD (ROCm) and Intel (XPU)** builds are also published; use the selector.

Check it:
```python
import torch
print(torch.__version__, "| CUDA:", torch.cuda.is_available(), "| MPS:", torch.backends.mps.is_available())
```
Each example in [examples/](examples/) declares `torch` as its dependency, so `uv run ai/frameworks/pytorch/examples/01_tensors_autograd.py` works too. That downloads the default build; for CPU only, run the scripts inside the project above.

## Quick start: learn a rule from data
```python
import torch
from torch import nn

device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(0)

X = torch.randn(256, 3, device=device)
true_w = torch.tensor([1.0, -2.0, 0.5], device=device)
y = (X @ true_w + 0.3).unsqueeze(1)           # a known linear rule

model = nn.Linear(3, 1).to(device)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for step in range(100):
    optimizer.zero_grad()                      # 1. clear old gradients
    loss = nn.functional.mse_loss(model(X), y) # 2. forward pass and loss
    loss.backward()                            # 3. backward pass: fill .grad
    optimizer.step()                           # 4. update the weights

print(f"loss {loss.item():.6f}", model.weight.data.flatten().tolist())
```
Those four numbered lines are the heart of every PyTorch training loop, from this toy to a large language model.

## The core ideas
| Idea | In PyTorch | Why it matters |
|---|---|---|
| Tensor | `torch.Tensor` | An array that can live on a GPU and track gradients |
| Autograd | `requires_grad`, `.backward()` | Computes derivatives for you |
| Module | `nn.Module` | A model is a class; its layers are attributes |
| Optimiser | `torch.optim.AdamW` | Updates parameters from gradients |
| Data | `Dataset`, `DataLoader` | Batching, shuffling, parallel loading |
| Device | `.to(device)` | Move tensors and models to the GPU |

## Examples in this folder
All four run on a CPU in seconds.
| File | What it shows |
|---|---|
| [01_tensors_autograd.py](examples/01_tensors_autograd.py) | Tensors, broadcasting, `backward()`, and linear regression with no `nn` at all |
| [02_mlp_two_moons.py](examples/02_mlp_two_moons.py) | A full training loop, validation, and safe save and load |
| [03_dataset_dataloader.py](examples/03_dataset_dataloader.py) | A custom `Dataset`, a learning-rate schedule, early stopping, optional mixed precision |
| [04_attention_from_scratch.py](examples/04_attention_from_scratch.py) | Self-attention written by hand and checked against PyTorch's own |

## Weekly rhythm
- One idea a week, written first as raw tensor code, then with `nn` and the optimisers.
- Before training on real data, make the model overfit one small batch. If it can't, there's a bug.

## Files
- [syllabus.md](syllabus.md): phases with projects
- [resources.md](resources.md): the official tutorials, courses, books and libraries
- [practice.md](practice.md): tasks at three levels, and a quiz
- [examples/](examples/): four runnable scripts

## My personal take
*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- PyTorch is my pick for deep learning. It's the one I'd learn first, because the code, the debugging and most of the models you'll want all live there.
- Write one training loop by hand before you use Lightning or a trainer class. You'll debug everything faster once you know what the framework is doing for you.
- Overfit a single batch first. It catches most bugs: wrong shapes, wrong loss, forgotten `zero_grad`, labels that don't match.
- Don't chase speed too early. Correct and slow beats fast and wrong; `torch.compile` and mixed precision come after the model works.
