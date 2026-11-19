# ML frameworks and libraries

The tools you actually use to build machine-learning systems. This group has four guides, and this page helps you choose between them.

| Guide | What it is | Start here if you want to… |
|---|---|---|
| [scikit-learn](scikit-learn/README.md) | Classical machine learning: pipelines, models, evaluation | learn the ML workflow, or work with tabular data |
| [PyTorch](pytorch/README.md) | Deep learning with tensors and automatic differentiation | train neural networks, or read and reuse research code |
| [TensorFlow and Keras](tensorflow/README.md) | Deep learning with strong deployment tools | build quick models, or ship to phones and browsers |
| [ML libraries in other languages](ml-libraries-other-languages/README.md) | Rust, C++, Java, Go, JavaScript, R, Julia, C# and ONNX | run models outside Python |

## Which one first?
1. **scikit-learn first.** It teaches the whole workflow (split, preprocess, fit, evaluate, tune) on small problems, and it is what you'll use for most tabular data.
2. **PyTorch second.** It's where most research code and open models live, and the concepts (tensors, gradients, training loops) carry over to every other framework.
3. **TensorFlow and Keras when your stack needs them.** Learn it for phones (LiteRT), browsers (TensorFlow.js), TensorFlow Serving, or a team that already uses it. Keras 3 also runs on PyTorch and JAX.
4. **Other languages when you deploy.** Train in Python, export to ONNX, and run in the language your product uses.

## Side by side
| | scikit-learn | PyTorch | TensorFlow and Keras |
|---|---|---|---|
| Best at | Classical ML, tabular data | Research, flexibility, open models | Deployment, quick models |
| Style | Estimators with `fit` and `predict` | Python code and explicit loops | Layers with `compile` and `fit` (or custom loops) |
| GPU | No (see cuML for GPU versions) | Yes | Yes |
| Debugging | Easy | Easy: ordinary Python | Easier in eager mode; harder inside `@tf.function` |
| Deployment | `joblib`, ONNX | `torch.export`, ONNX, ExecuTorch | SavedModel, TensorFlow Serving, LiteRT, TensorFlow.js |
| You'll meet it in | Data science, analytics | Papers, Hugging Face, LLMs | Production systems, mobile apps |

JAX is a fourth option: NumPy-like arrays with automatic differentiation and compilation, popular in research and available as a Keras 3 backend. It's on the [roadmap](../../ROADMAP.md).

## Python versions
Pick the Python version that suits the most restrictive library you need. At the time of writing (November 2026):

| Library | Python versions |
|---|---|
| scikit-learn | 3.11 and newer |
| PyTorch | 3.11 and newer |
| TensorFlow | 3.10 to 3.13 |

So **Python 3.13** works for all of them. Check each project's install page, because these ranges change.

## One project per framework
Install PyTorch and TensorFlow in separate projects. They bundle different versions of the CUDA libraries (at the time of writing, PyTorch's Linux wheel uses CUDA 13 and TensorFlow's GPU extra uses CUDA 12), and mixing them in one environment can cause conflicts. With `uv`, a project per framework costs nothing.

## Hardware, briefly
- **No GPU?** Everything here runs on a CPU. Use the CPU builds, and free Colab or Kaggle GPUs when you need one.
- **NVIDIA GPU?** Install the CUDA build of PyTorch or `tensorflow[and-cuda]`. See the install sections in each guide.
- **Apple Silicon?** PyTorch uses the GPU through `mps`.

## Related in this repo
[AI, LLMs and ML](../machine-learning/ai-ml/README.md) · [Agentic AI](../agents/agentic-ai/README.md) · [Data science](../../data/science/data-science/README.md) · [CUDA](../../languages/gpu/cuda/README.md) · [Python](../../languages/general/python/README.md)
