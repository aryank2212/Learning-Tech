# ML Libraries in Other Languages

Machine-learning libraries beyond Python (Rust, C and C++, Java, Go, JavaScript, R, Julia and C#), and how to run one trained model from any of them. Python is where machine learning is built, but it isn't the only place it runs. The pattern that connects them: **train in Python, export to ONNX, run anywhere.**

## When you'd leave Python
- **Deploy.** You want fewer dependencies, lower latency, or no Python runtime at all: a server, a phone, a browser, a microcontroller.
- **Integrate.** Your product already runs on Java, Go, C# or C++, and a separate Python service would be one more thing to operate.
- **Fit the job.** R and Julia suit statistics and numerical work. Rust and C++ suit inference engines where speed and memory use matter.

## Which job, which tool
| Job | A good choice |
|---|---|
| Learn and prototype | Python: [scikit-learn](../scikit-learn/README.md) and [PyTorch](../pytorch/README.md) |
| Train a big model | Python: PyTorch or JAX |
| Run a trained model from another language | ONNX Runtime (C, C++, C#, Java, JavaScript, Python; community bindings for Rust and Go) |
| Run a large language model locally | llama.cpp (C and C++), Ollama, or Candle (Rust) |
| Classical ML inside a Java service | Tribuo, Smile or Weka |
| ML in the browser | TensorFlow.js, ONNX Runtime Web, Transformers.js |
| ML on a phone | Core ML, LiteRT, ExecuTorch, ML Kit |
| Statistics-heavy analysis | R (tidymodels) or Julia (MLJ) |

## The bridge: ONNX
ONNX (Open Neural Network Exchange) is a file format for trained models. You train in the framework you like, export a `.onnx` file, and any ONNX Runtime binding can run it. The three examples in [examples/](examples/) show the whole path, and check that the answers agree:
```bash
uv run ai/frameworks/ml-libraries-other-languages/examples/01_sklearn_to_onnx.py   # scikit-learn -> ONNX
uv run ai/frameworks/ml-libraries-other-languages/examples/02_pytorch_to_onnx.py   # PyTorch -> ONNX
cd ai/frameworks/ml-libraries-other-languages/examples
npm install onnxruntime-node
node 03_run_onnx_in_node.mjs iris        # the same model, run from JavaScript
```
You should see a difference of about 1e-7 between Python and JavaScript: same model, same answers. Recent versions of npm may warn that a package's install script was skipped. CPU inference works without it.

The biggest source of bugs when you move a model is **preprocessing**, not the model. If Python scaled, tokenised or resized the input and your new code doesn't do exactly the same, the answers drift. Test with the same raw inputs in both languages.

## At a glance
A dash means there's no library I'd recommend for that job in that language.

| Job | Python | Rust | C++ | Java | Go | JavaScript | R | Julia | C# |
|---|---|---|---|---|---|---|---|---|---|
| Classical ML | scikit-learn | linfa, smartcore | mlpack, dlib | Tribuo, Smile, Weka | golearn | — | tidymodels, mlr3 | MLJ.jl | ML.NET |
| Deep learning | PyTorch, TensorFlow | burn, candle | LibTorch | DJL, Deeplearning4j | Gorgonia, GoMLX | TensorFlow.js | torch, keras3 | Flux.jl, Lux.jl | TorchSharp |
| Run an ONNX model | ONNX Runtime | ort, tract | ONNX Runtime | ONNX Runtime | onnxruntime_go | onnxruntime-node and -web | — | — | ONNX Runtime |

## Language guide

### Rust
- **Arrays and data:** `ndarray` (like NumPy), `polars` (fast DataFrames)
- **Classical ML:** `linfa` (a scikit-learn-style toolkit), `smartcore`
- **Deep learning:** `burn` (a framework with swappable backends), `candle` (from Hugging Face, popular for running transformer models)
- **Using PyTorch and ONNX models:** `tch` (bindings to LibTorch), `ort` (bindings to ONNX Runtime), `tract` (pure-Rust ONNX inference)
- **Tokenising text:** `tokenizers` (Hugging Face's library, written in Rust)

```bash
cargo add ndarray polars linfa smartcore
cargo add burn --features ndarray        # or: --features wgpu, to use the GPU through WebGPU
cargo add candle-core candle-nn candle-transformers
```
Use it when you want one static binary, no Python at run time, and memory safety. Watch out: the libraries are younger and change faster (`burn`, `candle` and `ort` are pre-1.0 or release candidates), and there are fewer pretrained models and tutorials. `tch` links LibTorch, which needs its own setup, and it can conflict with other crates that pin a different version of it, so add crates one at a time.

### C++
- **Run PyTorch models:** LibTorch, PyTorch's C++ API
- **Run exported models:** ONNX Runtime (C++ API), LiteRT, TensorRT (NVIDIA GPUs), OpenCV's `dnn` module
- **Classical ML and maths:** mlpack, dlib, Eigen, xtensor, Armadillo
- **Large language models:** llama.cpp and ggml

On Arch these are in the official repos: `sudo pacman -S eigen opencv dlib xtensor armadillo openblas`. mlpack, ONNX Runtime and llama.cpp are not, so use their releases, a source build, or the AUR. LibTorch is downloaded from [pytorch.org](https://pytorch.org/get-started/locally/).
Use it for games, robotics, trading systems and apps that are already C++. Watch out: building is the hard part (compiler versions, CUDA versions, ABI), so pin versions in CMake.

### Plain C
- **Linear algebra:** BLAS and LAPACK (OpenBLAS), the GNU Scientific Library (GSL)
- **Inference engines:** ggml (the C tensor library under llama.cpp)
- **Small teaching libraries:** genann and kann (tiny neural networks in C), Darknet (the original YOLO framework)

On Arch: `sudo pacman -S openblas lapack gsl`. Use it for firmware and for writing your own kernels. Watch out: manual memory management, so choose C++ or Rust for anything bigger.

### Java and Kotlin
- **Deep Java Library (DJL):** a high-level API that can use PyTorch, TensorFlow or ONNX Runtime underneath
- **Tribuo** (Oracle), **Smile** and **Weka:** classical ML, with Weka also offering a desktop app
- **ONNX Runtime for Java** to run exported models
- **Deeplearning4j:** deep learning on the JVM; check its recent releases before you commit to it
- **Spark MLlib:** distributed machine learning (see [big data analytics](../../../data/analytics/predictive-big-data-analytics/README.md))

The Maven coordinates are `ai.djl:api`, `org.tribuo:tribuo-all`, `nz.ac.waikato.cms.weka:weka-stable`, `com.microsoft.onnxruntime:onnxruntime` and `org.apache.spark:spark-mllib_2.13`. Use it for enterprise services and Spark pipelines.

### Go
- **Numerics:** Gonum
- **Deep learning:** Gorgonia (graph-based), GoMLX (built on XLA)
- **Run exported models:** `onnxruntime_go` (bindings to ONNX Runtime)
- **Classical ML:** golearn (its last release was in 2022, so check it's still right for you)

```bash
go get gonum.org/v1/gonum/mat
go get github.com/yalue/onnxruntime_go
```
Use Go to serve models that were trained elsewhere, in services and tools. Watch out: training support is limited. (Ollama, a popular local-LLM app, is written in Go, but it's an application, not a library.)

### JavaScript and TypeScript
- **TensorFlow.js:** train and run models in the browser or in Node
- **Transformers.js:** run Hugging Face models in the browser and Node, on ONNX Runtime
- **ONNX Runtime Web and ONNX Runtime Node:** run exported models
- **MediaPipe Tasks:** ready-made vision, audio and text tasks
- **ml5.js, brain.js:** small, friendly libraries for learning

```js
import * as tf from "@tensorflow/tfjs";          // npm install @tensorflow/tfjs

const xs = tf.randomNormal([256, 3]);
const w = tf.tensor2d([[1], [-2], [0.5]]);
const ys = xs.matMul(w).add(0.3);                // a known linear rule

const model = tf.sequential({ layers: [tf.layers.dense({ units: 1, inputShape: [3] })] });
model.compile({ optimizer: tf.train.sgd(0.1), loss: "meanSquaredError" });
await model.fit(xs, ys, { epochs: 100, verbose: 0 });

const [kernel] = model.getWeights();
console.log(Array.from(await kernel.data()));    // close to [1, -2, 0.5]
```
Run it as an ES module (a `.mjs` file) with Node. In a browser the library picks WebGL, WebGPU or WebAssembly for speed. In Node it falls back to a plain CPU backend and prints a banner suggesting its native add-on. Use it when you want the data to stay on the user's device, or to avoid server costs. Watch out: model size and download time.

### R
- **Classical ML:** `tidymodels` (the modern route), `caret` (older), `mlr3`, `glmnet`, `ranger`, `xgboost`
- **Deep learning:** `torch` for R (no Python needed) and `keras3`

```r
install.packages(c("tidymodels", "torch"))
```
Use R when the work is statistics-heavy and the output is a report (see [statistical computing](../../../data/statistics/statistical-computing/README.md)).

### Julia
- **Deep learning:** Flux.jl and Lux.jl
- **Classical ML:** MLJ.jl, a common interface to many models
- **Automatic differentiation:** Zygote.jl and Enzyme.jl

```julia
using Pkg; Pkg.add(["Flux", "MLJ"])
```
Use it for scientific computing and differentiable programming, where you want C-like speed without writing C.

### C# and .NET
- **ML.NET** (`Microsoft.ML`): classical ML and pipelines for .NET apps
- **TorchSharp:** PyTorch's engine from .NET
- **ONNX Runtime** (`Microsoft.ML.OnnxRuntime`) for exported models

```bash
dotnet add package Microsoft.ML
dotnet add package Microsoft.ML.OnnxRuntime
dotnet add package TorchSharp-cpu
```
Use it for .NET services and desktop apps.

### Phones and edge devices
- **Apple:** Core ML and Create ML; MLX (arrays and models on Apple silicon, for Python, Swift and C++)
- **Android and iOS:** LiteRT (formerly TensorFlow Lite) and ML Kit
- **PyTorch models on devices:** ExecuTorch

## Files
- [syllabus.md](syllabus.md): phases with projects
- [resources.md](resources.md): documentation and tutorials for every library above
- [practice.md](practice.md): tasks at three levels, and a quiz
- [examples/](examples/): scikit-learn and PyTorch to ONNX, and a Node.js check

## My personal take
*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- Train in Python and ship wherever you need. ONNX makes that easy now, and it saves you from rewriting training code in a language with a much thinner ecosystem.
- Don't switch languages for training unless you have a clear reason. The tutorials, the pretrained models and the people who can help you are all in Python.
- For inference, pick the language your product already uses. A model behind a small Rust, Go or Java service beats a second runtime that nobody on the team knows.
- Always test parity. Run the same raw inputs through both languages and compare numbers. Almost every porting bug I've seen was preprocessing.
- The Rust ML ecosystem is exciting, and I'd watch Burn and Candle closely. I'd still check release notes before building something long-lived on pre-1.0 libraries.
