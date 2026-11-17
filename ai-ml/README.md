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

## Weekly study plan (about 12 weeks, 6–10 hours a week)
| Weeks | Focus | Output |
|---|---|---|
| 1–2 | Maths refresher (see [maths](../maths/syllabus.md)) | Gradient descent in NumPy |
| 3–4 | Phase 1: classical ML | A house-price or Titanic pipeline |
| 5–6 | Phase 2: neural networks | MNIST from scratch, then in PyTorch |
| 7–8 | Phase 3: CNNs | A CIFAR-10 classifier, fine-tuned |
| 9 | Phase 4: transformers | A small GPT trained on your own text |
| 10–11 | Phase 5: LLM apps | A RAG app with citations |
| 12 | Phase 6 or 7 | A LoRA fine-tune, or an agent (see [agentic AI](../agentic-ai/README.md)) |

## Common pitfalls
- **Data leakage:** fitting preprocessing on the full dataset before the split. Fit transforms inside each training fold only.
- **Reporting training accuracy** as if it showed performance on new data.
- **Tuning on the test set.** Keep it locked until the final evaluation.
- **No baseline.** Always compare against a simple model, such as always predicting the most common class.
- **Unfixed random seeds.** Results can't be reproduced without them.
- **Trusting one run.** Repeat experiments with several seeds and report the spread.

## Mini-glossary
- **Epoch:** one full pass through the training data.
- **Batch:** a group of examples processed together.
- **Loss:** a number measuring how wrong the model is.
- **Gradient:** the direction and size of change that reduces the loss.
- **Overfitting:** learning the training data too closely to generalise.
- **Embedding:** a vector representing text, an image or another item.
- **Token:** the unit an LLM reads and writes, often part of a word.
- **Attention:** the mechanism that lets each position look at the others.
- **Context window:** how much text a model can consider at once.
- **Fine-tuning:** further training of a pretrained model on your own data.
- **Quantisation:** storing weights in fewer bits, so models are smaller and faster.

## Extra resources
- [Hugging Face Hub](https://huggingface.co/models) — pretrained models
- [Hugging Face Datasets](https://huggingface.co/datasets)
- [PyTorch tutorials](https://pytorch.org/tutorials/)
- [Distill.pub](https://distill.pub/) — visual explanations of ML (archived, still excellent)
- Related sections: [agentic AI](../agentic-ai/README.md), [research](../research/README.md), [tech ethics](../tech-ethics/README.md)
