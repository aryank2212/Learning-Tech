// Run an ONNX model from JavaScript and check it agrees with Python.
//
// One-time setup, in this folder:   npm install onnxruntime-node
// First create the model with:      uv run 01_sklearn_to_onnx.py   (or 02_pytorch_to_onnx.py)
// Then run:                         node 03_run_onnx_in_node.mjs iris   (or: mlp)
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import * as ort from "onnxruntime-node";

const here = path.dirname(fileURLToPath(import.meta.url));
const name = process.argv[2] ?? "iris";
const expectedFile = path.join(here, "out", `${name}_expected.json`);
if (!fs.existsSync(expectedFile)) {
  console.error(`Missing ${expectedFile}. Run the matching Python example first.`);
  process.exit(1);
}

const spec = JSON.parse(fs.readFileSync(expectedFile, "utf8"));
const session = await ort.InferenceSession.create(path.join(here, "out", spec.model));

const rows = spec.input.length;
const cols = spec.input[0].length;
const input = new ort.Tensor("float32", Float32Array.from(spec.input.flat()), [rows, cols]);

const results = await session.run({ [spec.input_name]: input });
const got = Array.from(results[spec.output_name].data);
const want = spec.expected.flat();

const diff = Math.max(...got.map((v, i) => Math.abs(v - want[i])));
console.log(`${name}: ${rows} rows -> output "${spec.output_name}", largest difference from Python: ${diff.toExponential(2)}`);
if (diff > 1e-5) {
  console.error("Outputs differ: check that preprocessing and dtypes match.");
  process.exit(1);
}
console.log("Same model, same answers, different language.");
