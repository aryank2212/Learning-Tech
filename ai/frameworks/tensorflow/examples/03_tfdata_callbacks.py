# /// script
# requires-python = ">=3.10,<3.14"
# dependencies = ["tensorflow", "numpy"]
# ///
"""tf.data input pipelines, callbacks, and a custom training loop beside model.fit.

Run:  uv run --python 3.13 03_tfdata_callbacks.py
"""
import os
import tempfile

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
import keras
import numpy as np
import tensorflow as tf

keras.utils.set_random_seed(0)
rng = np.random.default_rng(0)

# Three Gaussian blobs.
centers = np.array([[-2.0, -2.0], [2.0, -2.0], [0.0, 2.5]], dtype="float32")
X = np.vstack([c + rng.normal(size=(300, 2)) for c in centers]).astype("float32")
y = np.repeat(np.arange(3), 300).astype("int32")
order = rng.permutation(len(y))
X, y = X[order], y[order]
split = int(0.8 * len(y))

train_ds = (tf.data.Dataset.from_tensor_slices((X[:split], y[:split]))
            .shuffle(1000, seed=0).batch(32).prefetch(tf.data.AUTOTUNE))   # overlap input with training
val_ds = tf.data.Dataset.from_tensor_slices((X[split:], y[split:])).batch(128)


def build():
    return keras.Sequential([
        keras.Input(shape=(2,)),
        keras.layers.Dense(16, activation="relu"),
        keras.layers.Dense(3),                          # logits
    ])


loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# --- 1. model.fit with callbacks ---------------------------------------------
model = build()
model.compile(optimizer=keras.optimizers.Adam(3e-2), loss=loss_fn, metrics=["accuracy"])
with tempfile.TemporaryDirectory() as d:
    ckpt = os.path.join(d, "best.keras")
    callbacks = [
        keras.callbacks.EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True),
        keras.callbacks.ModelCheckpoint(ckpt, monitor="val_loss", save_best_only=True),
    ]
    # shuffle=False: the tf.data pipeline already shuffles, and Keras ignores `shuffle` for datasets.
    history = model.fit(train_ds, validation_data=val_ds, epochs=40, callbacks=callbacks, shuffle=False, verbose=0)
    best = keras.models.load_model(ckpt)
    print(f"fit: stopped after {len(history.history['loss'])} epochs, "
          f"reloaded best model accuracy {best.evaluate(val_ds, verbose=0)[1]:.3f}")

# --- 2. the same thing with a custom training loop ----------------------------
model2 = build()
optimizer = keras.optimizers.Adam(3e-2)


@tf.function                                            # traced once into a graph, then fast
def train_step(xb, yb):
    with tf.GradientTape() as tape:
        loss = loss_fn(yb, model2(xb, training=True))
    grads = tape.gradient(loss, model2.trainable_variables)
    optimizer.apply(grads, model2.trainable_variables)
    return loss


for epoch in range(15):
    for xb, yb in train_ds:
        train_step(xb, yb)
correct = sum(int((tf.argmax(model2(xb), axis=1, output_type=tf.int32) == yb).numpy().sum()) for xb, yb in val_ds)
print(f"custom loop: validation accuracy {correct / (len(y) - split):.3f}")
