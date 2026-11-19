# /// script
# requires-python = ">=3.11"
# dependencies = ["scikit-learn", "skl2onnx", "onnxruntime", "numpy"]
# ///
"""Train in Python, export to ONNX, run with ONNX Runtime, and check the answers match.

This is the bridge to every other language: once a model is an .onnx file, any ONNX
Runtime binding (C, C++, C#, Java, JavaScript, Rust, Go...) can run it.

Run:  uv run 01_sklearn_to_onnx.py
Then: node 03_run_onnx_in_node.mjs iris     (see the README for the one-time npm install)
"""
import json
from pathlib import Path

import numpy as np
import onnxruntime as ort
from skl2onnx import to_onnx
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

out = Path(__file__).parent / "out"
out.mkdir(exist_ok=True)

X, y = load_iris(return_X_y=True)
X = X.astype(np.float32)                         # ONNX models normally use float32
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=200)).fit(X, y)

# zipmap=False asks for plain probability arrays instead of a list of dictionaries.
onnx_model = to_onnx(model, X[:1], options={LogisticRegression: {"zipmap": False}})
(out / "iris.onnx").write_bytes(onnx_model.SerializeToString())

session = ort.InferenceSession(str(out / "iris.onnx"), providers=["CPUExecutionProvider"])
input_name = session.get_inputs()[0].name
output_names = [o.name for o in session.get_outputs()]
print("input:", input_name, "| outputs:", output_names)

sample = X[:5]
labels, probabilities = session.run(None, {input_name: sample})
expected = model.predict_proba(sample)
diff = float(np.abs(probabilities - expected).max())
print(f"largest difference between ONNX Runtime and scikit-learn: {diff:.2e}")
assert np.allclose(probabilities, expected, atol=1e-5), "outputs differ"

# Save the inputs and the expected answers, so other languages can prove they agree.
(out / "iris_expected.json").write_text(json.dumps({
    "model": "iris.onnx",
    "input_name": input_name,
    "output_name": output_names[1],
    "input": sample.tolist(),
    "expected": expected.tolist(),
}))
print("saved", out / "iris.onnx", "and iris_expected.json")
