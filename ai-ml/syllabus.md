# AI/ML syllabus

Work through the phases in order. Each phase ends with a project. Tick items in [progress/TRACKER.md](../progress/TRACKER.md).

## Phase 0 – Maths you'll actually use (2–4 weeks)
- [ ] Vectors, dot products, matrix multiplication
- [ ] Derivatives, partial derivatives, the chain rule
- [ ] Gradient descent by hand on a simple function
- [ ] Probability: distributions, expectation, Bayes' rule
- [ ] Watch 3Blue1Brown's *Essence of Linear Algebra* and *Essence of Calculus*

🛠️ **Project:** implement gradient descent for linear regression in NumPy, no ML libraries.

## Phase 1 – Classical machine learning (3–4 weeks)
- [ ] Train / validation / test split, overfitting, cross-validation
- [ ] Linear and logistic regression
- [ ] Decision trees, random forests
- [ ] k-means clustering
- [ ] Metrics: accuracy, precision, recall, F1, ROC-AUC
- [ ] Feature engineering and scikit-learn `Pipeline`

🛠️ **Project:** predict house prices or classify Titanic survivors (Kaggle) with a clean pipeline.

## Phase 2 – Neural networks (4 weeks)
- [ ] Neurons, activations, forward pass
- [ ] Loss functions and backpropagation
- [ ] Write a neural net from scratch in NumPy
- [ ] Rebuild it in PyTorch: tensors, autograd, `nn.Module`, optimisers
- [ ] Training loop, batching, GPU with `.to("cuda")`

🛠️ **Project:** classify handwritten digits (MNIST) from scratch, then with PyTorch.

## Phase 3 – Deep learning for vision and sequences (4 weeks)
- [ ] Convolutional networks (CNN)
- [ ] Data augmentation, regularisation, dropout, batch norm
- [ ] Transfer learning with pretrained models (ResNet, ViT)
- [ ] Recurrent networks (RNN, LSTM), why they were replaced

🛠️ **Project:** image classifier on CIFAR-10 or your own photos, fine-tuned from a pretrained model.

## Phase 4 – Transformers and LLMs (6 weeks)
- [ ] Tokenisation (BPE), embeddings
- [ ] Self-attention and multi-head attention, from scratch
- [ ] Positional encodings, layer norm, residual connections
- [ ] Decoder-only models (GPT) and how text generation works
- [ ] Sampling: temperature, top-p, greedy
- [ ] Hugging Face `transformers`: load, run, inspect a model

🛠️ **Project:** build a small GPT following Karpathy's *Let's build GPT*, then train it on text you choose.

## Phase 5 – Using LLMs in apps (4 weeks)
- [ ] Prompt engineering: system prompts, few-shot, structured output (JSON)
- [ ] Calling an LLM API (Anthropic, OpenAI) with streaming
- [ ] Tool use / function calling
- [ ] Embeddings and vector search
- [ ] RAG: chunk documents, embed, retrieve, generate
- [ ] Evaluation: test sets for LLM outputs

🛠️ **Project:** chat with your own PDFs (RAG), with citations.

## Phase 6 – Adapting and running models (4–6 weeks)
- [ ] Quantisation (4-bit, 8-bit) and why it fits models in memory
- [ ] Running local models with Ollama and llama.cpp
- [ ] LoRA and QLoRA fine-tuning (Hugging Face `peft`, `trl`)
- [ ] Dataset preparation for instruction tuning
- [ ] Inference speed: batching, KV cache

🛠️ **Project:** fine-tune a small model (≈1B parameters) on a task of your choice with LoRA.

## Phase 7 – Agents and production (ongoing)
- [ ] Agent loops: plan, act, observe
- [ ] MCP (Model Context Protocol) servers and clients
- [ ] Logging, cost tracking, rate limits, retries
- [ ] Deploying a model behind an API (FastAPI)
- [ ] Safety basics: prompt injection, data leakage

🛠️ **Project:** an agent that answers questions using a search tool and your own notes.

## Phase 8 – Research track (optional)
- [ ] Read a paper per week (see [resources.md](resources.md))
- [ ] Reproduce one small result from a paper
- [ ] Write up what you learned in a blog post or in your own notes
