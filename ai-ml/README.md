# AI, LLMs & Machine / Deep Learning

From "what is a model" to building and running your own large language model.

## The big picture

```
Maths (linear algebra, calculus, probability)
   └─► Classical ML (regression, trees, clustering)
         └─► Deep learning (neural nets, backprop, CNNs, RNNs)
               └─► Transformers (attention)
                     ├─► Pretrained LLMs: use them via APIs and local models
                     ├─► RAG & agents: connect LLMs to your data and tools
                     └─► Build & train your own (nanoGPT, fine-tuning, RLHF)
```

## Sections

| File | What's in it |
|------|--------------|
| [install.md](install.md) | Python environment, PyTorch with GPU, local LLM runners |
| [syllabus.md](syllabus.md) | Topics in order, with projects |
| [resources.md](resources.md) | Books, courses, papers, videos, datasets, tools |

## Prerequisites

- **Python** (see [languages/python](../languages/python/README.md)), at least Level 2
- **Maths** you can revise as you go: linear algebra (vectors, matrices), calculus (derivatives, chain rule), basic probability

## Hardware reality check

| Goal | Hardware needed |
|------|-----------------|
| Learn ML, classical models, small nets | Any laptop |
| Train small neural nets, CIFAR-10 | Any GPU with 4 GB+ VRAM, or free Colab / Kaggle GPUs |
| Run 7–8B LLMs locally (quantised) | 8 GB+ VRAM, or 16 GB RAM for CPU |
| Fine-tune LLMs | 12–24 GB+ VRAM, or cloud GPUs |
| Train large models | Clusters: not for learning |

No GPU? Use **Google Colab** (free GPU) or **Kaggle Notebooks** to follow the course.
