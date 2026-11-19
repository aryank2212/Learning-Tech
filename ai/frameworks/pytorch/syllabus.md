# PyTorch syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md).

### Phase 1 – Tensors
- [ ] Creating tensors; dtypes; shapes
- [ ] Indexing, slicing, `reshape` and `view`
- [ ] Broadcasting rules
- [ ] Moving to a device; NumPy interop

🛠️ Project: reimplement five NumPy operations with tensors, and check they agree.

### Phase 2 – Autograd
- [ ] `requires_grad` and `.backward()`
- [ ] Gradient accumulation, and `zero_grad`
- [ ] `torch.no_grad()`, `torch.inference_mode()` and `.detach()`
- [ ] What the computation graph is

🛠️ Project: linear regression with autograd only, no `nn` and no optimiser.

### Phase 3 – Models with `nn.Module`
- [ ] `nn.Linear`, activations, `nn.Sequential`
- [ ] Writing your own `nn.Module`
- [ ] Loss functions; `parameters()` and `state_dict()`
- [ ] Initialisation

🛠️ Project: an MLP that solves XOR, then a two-moons classifier.

### Phase 4 – The training loop
- [ ] Optimisers: SGD, Adam, AdamW
- [ ] `model.train()` and `model.eval()`
- [ ] Validation, metrics, and learning-rate schedules
- [ ] Checkpointing and reproducibility (seeds)

🛠️ Project: a training script with validation, early stopping and a saved best model.

### Phase 5 – Data
- [ ] `Dataset` and `DataLoader`
- [ ] Batching, shuffling, `num_workers`
- [ ] Transforms and augmentation
- [ ] `torchvision` datasets

🛠️ Project: a custom `Dataset` over a folder of images or a CSV file.

### Phase 6 – Computer vision
- [ ] Convolutional layers, pooling, batch normalisation
- [ ] Pretrained models from `torchvision.models`
- [ ] Transfer learning and fine-tuning
- [ ] Data augmentation

🛠️ Project: fine-tune a pretrained ResNet on a small dataset, and compare it with training from scratch.

### Phase 7 – Sequences and transformers
- [ ] Embeddings
- [ ] RNNs and LSTMs, and why transformers replaced them
- [ ] Attention, masks, positional information
- [ ] `nn.TransformerEncoder` and `F.scaled_dot_product_attention`

🛠️ Project: a character-level language model that generates text.

### Phase 8 – GPUs and performance
- [ ] Devices and `.to(device)`
- [ ] Mixed precision with `torch.autocast`
- [ ] `torch.compile`
- [ ] Profiling with `torch.profiler`
- [ ] Gradient accumulation and gradient checkpointing

🛠️ Project: make one training loop at least twice as fast, and report each change's effect.

### Phase 9 – Saving, exporting and deploying
- [ ] `state_dict` and `torch.load(..., weights_only=True)`
- [ ] `torch.export` and ONNX export
- [ ] Running the exported model with ONNX Runtime
- [ ] Edge deployment with ExecuTorch (concept)

🛠️ Project: export a model to ONNX and check that its outputs match PyTorch's.

### Phase 10 – Training at scale
- [ ] `torchrun` and `DistributedDataParallel`
- [ ] FSDP (concept)
- [ ] Higher-level tools: Lightning and Hugging Face Accelerate

🛠️ Project: train on two processes on one machine with DDP, and compare the speed.

### Phase 11 – Debugging and testing
- [ ] Reading shape errors
- [ ] Finding NaNs; `torch.autograd.set_detect_anomaly`
- [ ] The overfit-one-batch test
- [ ] Unit tests for models and data pipelines

🛠️ Project: a test suite for a model that checks shapes, gradients and determinism.

### Phase 12 – The ecosystem
- [ ] Hugging Face `transformers`
- [ ] `timm` for vision models
- [ ] TorchMetrics, TensorBoard, Weights & Biases

🛠️ Project: fine-tune a pretrained transformer and write a model card.

### Capstone
🛠️ Project: reproduce a small result from a paper in PyTorch, with a seed study, a written comparison to the paper, and the code published.
