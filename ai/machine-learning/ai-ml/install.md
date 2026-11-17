# AI/ML install guide

Built for Omarchy/Arch with an NVIDIA GPU, but the Python steps work everywhere.

## 1. Python environment with uv

```bash
sudo pacman -S --needed uv python
mkdir -p ~/ai-learning && cd ~/ai-learning
uv init --python 3.13 ml-playground
cd ml-playground
uv add numpy pandas matplotlib scikit-learn jupyter ipykernel seaborn
```

Run a notebook: `uv run jupyter lab`

Each project gets its own `.venv`. Keep big datasets and model files outside the repo (add them to `.gitignore`).

## 2. PyTorch with GPU (CUDA)

Check the driver first:

```bash
nvidia-smi
```

Pick the CUDA build from the official selector at https://pytorch.org/get-started/locally/. Example for CUDA 12.6 (check the page for the current version):

```bash
uv add torch torchvision --index-url https://download.pytorch.org/whl/cu126
```

Verify the GPU works:

```bash
uv run python -c "import torch; print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0) if torch.cuda.is_available() else '')"
```

Expected: `True` and your GPU name. If it prints `False`:
1. Run `nvidia-smi` and note the CUDA version at the top.
2. Reinstall torch with the matching `cu1xx` index URL.
3. Reboot after driver updates.

## 3. Hugging Face (models, datasets, tokenizers)

```bash
uv add transformers datasets accelerate huggingface_hub
uv run huggingface-cli login     # optional, needed for gated models
```

Create a free token at https://huggingface.co/settings/tokens. Never commit tokens to git.

## 4. Local LLM runners (no API cost)

**Ollama** (easiest):

```bash
sudo pacman -S ollama
sudo systemctl enable --now ollama
ollama pull llama3.2          # small, fast model
ollama run llama3.2
```

**llama.cpp** (learn how inference works): build from https://github.com/ggml-org/llama.cpp with CMake, using `-DGGML_CUDA=ON` for GPU.

**LM Studio** is also installed on this machine if you prefer a GUI.

## 5. Cloud alternatives (free tiers)

- **Google Colab:** https://colab.research.google.com – Runtime → Change runtime type → GPU
- **Kaggle Notebooks:** https://www.kaggle.com/code – free GPU quota each week

## 6. API keys for LLM apps

```bash
export ANTHROPIC_API_KEY="..."   # set in your shell, not in code
export OPENAI_API_KEY="..."      # if you use OpenAI
```

Store keys in a `.env` file and add `.env` to `.gitignore`. Use the `python-dotenv` package to load them.

## 7. Verify

```bash
uv run python -c "import numpy, pandas, sklearn, torch; print('all imports ok')"
ollama list
```
