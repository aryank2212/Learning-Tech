# /// script
# requires-python = ">=3.10,<3.14"
# dependencies = ["tensorflow"]
# ///
"""TensorFlow tensors, variables and automatic differentiation with GradientTape.

Run:  uv run --python 3.13 01_tensors_gradienttape.py
(TensorFlow supports Python 3.10 to 3.13 at the time of writing.)
"""
import os

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")   # hide the C++ start-up chatter
import tensorflow as tf

tf.random.set_seed(0)

# --- tensors and variables -------------------------------------------------
a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
b = tf.ones((2, 2))
print("a @ b =\n", (a @ b).numpy())
print("broadcast a + [10, 20] =\n", (a + tf.constant([10.0, 20.0])).numpy())
print("shape, dtype:", a.shape, a.dtype.name)

# --- gradients ---------------------------------------------------------------
x = tf.Variable(2.0)
with tf.GradientTape() as tape:
    y = x**2 + 3 * x                    # dy/dx = 2x + 3 = 7 at x = 2
print("dy/dx at x=2:", tape.gradient(y, x).numpy(), "(expected 7.0)")

# --- linear regression with GradientTape only -------------------------------
true_w, true_b = 3.0, 2.0
X = tf.linspace(-1.0, 1.0, 100)[:, None]
Y = true_w * X + true_b + 0.05 * tf.random.normal((100, 1))

w, bias = tf.Variable(0.0), tf.Variable(0.0)
for _ in range(200):
    with tf.GradientTape() as tape:
        loss = tf.reduce_mean((X * w + bias - Y) ** 2)
    dw, db = tape.gradient(loss, [w, bias])
    w.assign_sub(0.1 * dw)
    bias.assign_sub(0.1 * db)

print(f"learned w={w.numpy():.2f}, b={bias.numpy():.2f}  (true {true_w}, {true_b})")
