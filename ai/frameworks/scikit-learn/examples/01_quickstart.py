# /// script
# requires-python = ">=3.11"
# dependencies = ["scikit-learn"]
# ///
"""scikit-learn quick start: split, fit, evaluate, cross-validate.

Run:  uv run 01_quickstart.py
"""
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=0
)

# A pipeline keeps scaling and the model together, so the scaler only ever
# learns from training data (no leakage).
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=200))
model.fit(X_train, y_train)
pred = model.predict(X_test)

print(f"test accuracy: {accuracy_score(y_test, pred):.3f}")
print(classification_report(y_test, pred, target_names=iris.target_names))

scores = cross_val_score(model, X, y, cv=5)
print(f"5-fold CV accuracy: {scores.mean():.3f} +/- {scores.std():.3f}")
