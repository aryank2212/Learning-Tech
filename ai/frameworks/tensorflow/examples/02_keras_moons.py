# /// script
# requires-python = ">=3.10,<3.14"
# dependencies = ["tensorflow", "numpy"]
# ///
"""Keras in four steps: define, compile, fit, evaluate. Then save and reload.

Run:  uv run --python 3.13 02_keras_moons.py
"""
import os
import tempfile

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
import keras
import numpy as np

keras.utils.set_random_seed(0)


def make_moons(n, noise=0.15):
    rng = np.random.default_rng(0)
    t = rng.uniform(0, np.pi, n // 2)
    top = np.c_[np.cos(t), np.sin(t)]
    bottom = np.c_[1 - np.cos(t), 0.5 - np.sin(t)]
    X = np.vstack([top, bottom]) + noise * rng.normal(size=(n, 2))
    y = np.r_[np.zeros(n // 2), np.ones(n // 2)]
    order = rng.permutation(n)
    return X[order].astype("float32"), y[order].astype("float32")


X, y = make_moons(1000)
X_train, y_train, X_test, y_test = X[:800], y[:800], X[800:], y[800:]

model = keras.Sequential([
    keras.Input(shape=(2,)),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid"),
])
model.compile(optimizer=keras.optimizers.Adam(1e-2), loss="binary_crossentropy", metrics=["accuracy"])
model.summary()

history = model.fit(X_train, y_train, epochs=60, batch_size=32, validation_split=0.2, verbose=0)
print(f"last validation accuracy: {history.history['val_accuracy'][-1]:.3f}")

loss, acc = model.evaluate(X_test, y_test, verbose=0)
print(f"test accuracy: {acc:.3f}")

with tempfile.TemporaryDirectory() as d:
    path = os.path.join(d, "moons.keras")
    model.save(path)                                   # one file: architecture + weights + optimizer
    reloaded = keras.models.load_model(path)
    same = np.allclose(model.predict(X_test, verbose=0), reloaded.predict(X_test, verbose=0), atol=1e-6)
    print("reloaded model gives the same predictions:", same)
