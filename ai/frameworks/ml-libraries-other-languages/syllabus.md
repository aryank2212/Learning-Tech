# ML libraries in other languages: syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md). Do it after you've trained at least one model in [scikit-learn](../scikit-learn/README.md) or [PyTorch](../pytorch/README.md).

### Phase 1 – Choose the job
- [ ] Training, inference and data preparation are different jobs
- [ ] Model formats: ONNX, SavedModel, GGUF, safetensors
- [ ] What a runtime does, and what a framework does

🛠️ Project: write a one-page decision note for a model you want to ship: where it runs, in which language, and why.

### Phase 2 – Numerical foundations in other languages
- [ ] Arrays and matrices: Rust `ndarray`, C++ Eigen, Java Smile, Go Gonum, Julia arrays, R matrices
- [ ] Row-major and column-major layouts
- [ ] Linking BLAS and LAPACK

🛠️ Project: implement matrix multiplication and a linear solve in two languages, and compare their speed.

### Phase 3 – Classical ML outside Python
- [ ] Rust: `linfa`, `smartcore`
- [ ] Java: Weka, Tribuo, Smile
- [ ] R: `tidymodels`; Julia: MLJ; C#: ML.NET; C++: mlpack, dlib

🛠️ Project: train the same classifier on the same data in three languages, and compare accuracy, code length and run time.

### Phase 4 – Deep learning outside Python
- [ ] Rust: `burn`, `candle`, `tch`
- [ ] C++: LibTorch
- [ ] Java: DJL; JavaScript: TensorFlow.js; Julia: Flux and Lux; R: `torch`; C#: TorchSharp

🛠️ Project: train a small multilayer perceptron in a non-Python language.

### Phase 5 – The ONNX bridge
- [ ] Export from scikit-learn (`skl2onnx`) and from PyTorch (`torch.onnx.export`)
- [ ] Running with ONNX Runtime in Python
- [ ] Dynamic shapes, opsets and data types
- [ ] Checking numerical parity

🛠️ Project: run [the three examples](examples/), then export a model of your own and prove parity.

### Phase 6 – Run it in another language
- [ ] ONNX Runtime from JavaScript, Java, C#, C++, Rust (`ort`) or Go
- [ ] Reproducing preprocessing exactly (scaling, tokenising, resizing)
- [ ] Golden tests: raw input in, expected numbers out

🛠️ Project: run your exported model from a second language, and add a parity test that fails when outputs drift.

### Phase 7 – The browser and devices
- [ ] TensorFlow.js, ONNX Runtime Web and Transformers.js
- [ ] WebGPU and WebAssembly backends
- [ ] LiteRT, Core ML, ExecuTorch (concepts)
- [ ] Model size, download time, privacy benefits

🛠️ Project: run an image or text classifier entirely in a browser page.

### Phase 8 – Serving
- [ ] An HTTP or gRPC service in Go, Rust, Java or C# that calls an ONNX model
- [ ] Batching, timeouts, health checks, versioning
- [ ] Measuring latency and throughput

🛠️ Project: a small service that serves your model, with a load test and a parity test.

### Phase 9 – Speed and size
- [ ] Quantisation: int8 and 4-bit
- [ ] GPU backends: CUDA, Metal, Vulkan/WebGPU
- [ ] Profiling inference

🛠️ Project: quantise a model and measure accuracy loss, speed and size in two runtimes.

### Phase 10 – Capstone
🛠️ Project: ship one model in two languages, with parity tests, a benchmark, and a short write-up of what you'd choose in production and why.
