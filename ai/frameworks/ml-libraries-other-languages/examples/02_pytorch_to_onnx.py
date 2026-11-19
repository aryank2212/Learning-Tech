# /// script
# requires-python = ">=3.11"
# dependencies = ["torch", "onnx", "onnxscript", "onnxruntime", "numpy"]
# ///
"""Export a PyTorch model to ONNX and check that ONNX Runtime gives the same answers.

Run:  uv run 02_pytorch_to_onnx.py
Then: node 03_run_onnx_in_node.mjs mlp
"""
import json
from pathlib import Path

import numpy as np
import onnxruntime as ort
import torch
from torch import nn

torch.manual_seed(0)
out = Path(__file__).parent / "out"
out.mkdir(exist_ok=True)

model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 3)).eval()   # eval() before exporting
example = torch.randn(5, 4)

batch = torch.export.Dim("batch")                       # the batch size may vary at run time
torch.onnx.export(
    model, (example,), str(out / "mlp.onnx"),
    input_names=["input"], output_names=["logits"],
    dynamic_shapes=({0: batch},),                       # one entry per input: dimension 0 is dynamic
)

session = ort.InferenceSession(str(out / "mlp.onnx"), providers=["CPUExecutionProvider"])
(logits,) = session.run(None, {"input": example.numpy()})
with torch.inference_mode():
    expected = model(example).numpy()
diff = float(np.abs(logits - expected).max())
print(f"largest difference between ONNX Runtime and PyTorch: {diff:.2e}")
assert np.allclose(logits, expected, atol=1e-5), "outputs differ"

# A different batch size works too, because dimension 0 was declared dynamic.
(bigger,) = session.run(None, {"input": np.random.default_rng(0).normal(size=(11, 4)).astype("float32")})
print("batch of 11 gives output shape:", bigger.shape)

(out / "mlp_expected.json").write_text(json.dumps({
    "model": "mlp.onnx",
    "input_name": "input",
    "output_name": "logits",
    "input": example.tolist(),
    "expected": expected.tolist(),
}))
print("saved", out / "mlp.onnx", "and mlp_expected.json")
