# /// script
# requires-python = ">=3.10,<3.14"
# dependencies = ["tensorflow"]
# ///
"""How @tf.function traces Python, and how to see which Keras backend you're using.

Run:  uv run --python 3.13 04_tf_function_and_backends.py
"""
import os

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
import keras
import tensorflow as tf

print("Keras backend:", keras.backend.backend(), "(set KERAS_BACKEND=jax or torch before importing keras to switch)")

traces = 0


@tf.function
def square_sum(x):
    global traces
    traces += 1                         # plain Python: runs only while TensorFlow *traces* the function
    tf.print("tf.print runs on every call:", tf.reduce_sum(x))
    return tf.reduce_sum(x * x)


square_sum(tf.constant([1.0, 2.0, 3.0]))
square_sum(tf.constant([4.0, 5.0, 6.0]))   # same shape and dtype: reuses the graph, no new trace
print("traces after two calls with the same shape:", traces)
square_sum(tf.constant([1.0, 2.0]))        # a new shape triggers a new trace
print("traces after a different shape:", traces)

# input_signature fixes the shape, so there's only ever one trace:
@tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32)])
def mean(x):
    return tf.reduce_mean(x)

print("mean of 3 values:", mean(tf.constant([1.0, 2.0, 3.0])).numpy(), "| of 5 values:", mean(tf.ones(5)).numpy())
print("times `mean` was traced:", mean.experimental_get_tracing_count())
