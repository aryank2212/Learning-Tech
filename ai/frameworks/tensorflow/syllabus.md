# TensorFlow and Keras syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md).

### Phase 1 – Tensors
- [ ] `tf.constant`, `tf.Variable`, dtypes and shapes
- [ ] Broadcasting; indexing; NumPy interop
- [ ] Eager execution

🛠️ Project: reimplement five NumPy operations with tensors, and check they agree.

### Phase 2 – Automatic differentiation
- [ ] `tf.GradientTape`
- [ ] Persistent tapes; gradients of lists of variables
- [ ] Custom gradients (concept)

🛠️ Project: linear regression with a tape and no Keras.

### Phase 3 – Keras basics
- [ ] `Sequential` and the Functional API
- [ ] Layers, activations, initialisers
- [ ] `compile`, `fit`, `evaluate`, `predict`
- [ ] Losses and metrics

🛠️ Project: an MLP for XOR, then a two-moons classifier.

### Phase 4 – Data pipelines
- [ ] `tf.data.Dataset`: `map`, `shuffle`, `batch`, `prefetch`, `cache`
- [ ] Keras preprocessing layers
- [ ] TFRecord files (concept)

🛠️ Project: a fast input pipeline for an image folder, with a measured speed-up from `prefetch`.

### Phase 5 – Training workflows
- [ ] Callbacks: `EarlyStopping`, `ModelCheckpoint`, `TensorBoard`
- [ ] Learning-rate schedules
- [ ] Custom training loops
- [ ] Mixed precision

🛠️ Project: the same model trained with `fit` and with a custom loop, and a comparison of the results.

### Phase 6 – Vision and transfer learning
- [ ] Convolutional layers
- [ ] `keras.applications` pretrained models
- [ ] Fine-tuning and data augmentation layers

🛠️ Project: fine-tune a pretrained model on a small image dataset.

### Phase 7 – Sequences and language
- [ ] Embeddings; `TextVectorization`
- [ ] LSTM and GRU layers
- [ ] Attention, and transformer blocks
- [ ] KerasHub pretrained models

🛠️ Project: a text classifier, then a small text-generation model.

### Phase 8 – Graphs and performance
- [ ] `@tf.function`, tracing and retracing
- [ ] Input signatures
- [ ] XLA compilation (`jit_compile=True`)
- [ ] Profiling with the TensorBoard profiler

🛠️ Project: speed up a training step and explain each change.

### Phase 9 – Saving and serving
- [ ] The `.keras` format and SavedModel export
- [ ] TensorFlow Serving (Docker), REST and gRPC
- [ ] Model versioning

🛠️ Project: serve a model with TensorFlow Serving, and call it with `curl`.

### Phase 10 – Edge and browser
- [ ] Converting to LiteRT (formerly TensorFlow Lite)
- [ ] Post-training quantisation
- [ ] TensorFlow.js: converting and running in a browser

🛠️ Project: quantise a model, and compare its size, speed and accuracy with the original.

### Phase 11 – Distributed training
- [ ] `tf.distribute.MirroredStrategy`
- [ ] Multi-worker training (concept)
- [ ] TPUs (concept)

🛠️ Project: train with `MirroredStrategy` on several devices, or on CPU replicas if you have one machine.

### Phase 12 – Keras 3 and the wider ecosystem
- [ ] Multi-backend Keras: TensorFlow, JAX, PyTorch
- [ ] What breaks when you switch backend
- [ ] MLOps tools: TensorBoard, experiment tracking, TFX (concept)

🛠️ Project: run the same Keras model on two backends, and note any differences.

### Capstone
🛠️ Project: train, serve and monitor a model, and publish a short report on its accuracy, size and latency.
