# TensorFlow and Keras

Google's machine-learning platform: Keras for building and training models, TensorFlow for serving them, shrinking them for phones and running them in browsers. Keras is the friendly high-level API, and Keras 3 can also run on JAX or PyTorch.

## Why learn it
- **Keras is quick to learn.** A model is a few lines, and `compile`, `fit` and `evaluate` cover a lot of ground.
- **It has a complete deployment story.** TensorFlow Serving, LiteRT for phones and microcontrollers, and TensorFlow.js for browsers are all mature.
- **Many companies run on it.** You'll meet TensorFlow code in production systems even though research has moved largely to PyTorch.

## Prerequisites
- Python at Level 2 (see [Python](../../../languages/general/python/README.md))
- The ideas behind neural networks (see [AI, LLMs and ML](../../machine-learning/ai-ml/syllabus.md), phase 2)
- It helps to have used [scikit-learn](../scikit-learn/README.md) first

## Install
TensorFlow supports Python 3.10 to 3.13 at the time of writing, so choose 3.13 or 3.12 rather than the newest Python.
```bash
uv init tensorflow-lab --python 3.13 && cd tensorflow-lab
uv add tensorflow
uv run python -c "import tensorflow as tf, keras; print(tf.__version__, keras.__version__)"
```
- **NVIDIA GPU on Linux:** `uv add "tensorflow[and-cuda]"` installs the matching CUDA libraries. They're CUDA 12 libraries, while PyTorch's Linux wheel uses CUDA 13, so keep TensorFlow and PyTorch in separate projects.
- **Windows:** GPU training needs WSL2 (Ubuntu inside Windows); native Windows runs on the CPU.
- **Apple Silicon:** the CPU build works; check the TensorFlow install page for GPU options.

The examples in [examples/](examples/) declare `tensorflow` as their dependency and need Python 3.13 or older:
```bash
uv run --python 3.13 ai/frameworks/tensorflow/examples/02_keras_moons.py
```
On the first run, TensorFlow prints messages from its C++ core (about oneDNN or a missing GPU). They're normal. The examples quieten them by setting `TF_CPP_MIN_LOG_LEVEL`.

## Quick start: learn a rule from data
```python
import keras
import numpy as np

keras.utils.set_random_seed(0)
X = np.random.default_rng(0).normal(size=(256, 3)).astype("float32")
y = (X @ np.array([1.0, -2.0, 0.5], dtype="float32") + 0.3)[:, None]   # a known linear rule

model = keras.Sequential([keras.Input(shape=(3,)), keras.layers.Dense(1)])
model.compile(optimizer=keras.optimizers.SGD(0.1), loss="mse")
model.fit(X, y, epochs=100, batch_size=64, verbose=0)

print(model.layers[0].get_weights()[0].ravel())   # close to [1, -2, 0.5]
```
That's the same problem as the PyTorch quick start, so you can compare the two styles. Keras hides the loop; for control, you write the loop yourself with `tf.GradientTape` (see example 03).

## The core ideas
| Idea | In TensorFlow and Keras | Why it matters |
|---|---|---|
| Tensor and Variable | `tf.constant`, `tf.Variable` | Arrays that can run on accelerators; variables hold weights |
| Gradient tape | `tf.GradientTape` | Records operations so gradients can be computed |
| Layers and models | `keras.layers`, `keras.Sequential`, the Functional API | Build models from parts |
| Training | `compile`, `fit`, `evaluate`, `predict` | A full loop in four calls |
| Input pipelines | `tf.data` | Fast, parallel, prefetched data loading |
| Graphs | `@tf.function` | Compiles Python into a graph for speed and export |
| Deployment | SavedModel, LiteRT, TF.js | Take the model off your laptop |

## Examples in this folder
All four run on a CPU. Python 3.13 or older is needed.
| File | What it shows |
|---|---|
| [01_tensors_gradienttape.py](examples/01_tensors_gradienttape.py) | Tensors, variables, `GradientTape`, and linear regression with no Keras |
| [02_keras_moons.py](examples/02_keras_moons.py) | Define, compile, fit, evaluate; save to `.keras` and reload |
| [03_tfdata_callbacks.py](examples/03_tfdata_callbacks.py) | `tf.data`, `EarlyStopping`, `ModelCheckpoint`, and a custom training loop |
| [04_tf_function_and_backends.py](examples/04_tf_function_and_backends.py) | How `@tf.function` traces Python, and how to see the Keras backend |

## Weekly rhythm
- One piece at a time: first with `fit`, then the same thing with a custom loop, so you see what `fit` does.
- Learn `tf.data` early. Slow input pipelines are the most common reason for slow training.

## Files
- [syllabus.md](syllabus.md): phases with projects
- [resources.md](resources.md): official guides, books, and the deployment tools
- [practice.md](practice.md): tasks at three levels, and a quiz
- [examples/](examples/): four runnable scripts

## My personal take
*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- Honestly: PyTorch is where most research and open models live, and I'd learn it first. TensorFlow and Keras still make sense when your stack uses them, or when you target phones with LiteRT, browsers with TensorFlow.js, or TensorFlow Serving.
- Keras 3 is pleasant for quick models, and it runs on JAX and PyTorch as well. Learning it is a good low-risk bet.
- Write one custom training loop with `GradientTape`. It shows you what `fit` hides, and it's the same idea as PyTorch's loop.
- Be careful with `@tf.function`. Python side effects inside it run only while the function is traced, not on every call, and that surprises almost everyone once.
