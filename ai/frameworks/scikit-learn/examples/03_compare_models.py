# /// script
# requires-python = ">=3.11"
# dependencies = ["scikit-learn"]
# ///
"""Compare several models fairly with cross-validation, then evaluate the winner once.

Run:  uv run 03_compare_models.py
"""
import tempfile
from pathlib import Path

import joblib
from sklearn.datasets import load_digits
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

models = {
    "logistic regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)),
    "k-nearest neighbours": make_pipeline(StandardScaler(), KNeighborsClassifier()),
    "support vector machine": make_pipeline(StandardScaler(), SVC()),
    "random forest": RandomForestClassifier(n_estimators=200, random_state=0),
    "gradient boosting": HistGradientBoostingClassifier(random_state=0),
}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)

results = {}
for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=cv)
    results[name] = scores.mean()
    print(f"{name:24s} CV accuracy {scores.mean():.3f} +/- {scores.std():.3f}")

best = max(results, key=results.get)
final = models[best].fit(X_train, y_train)
print(f"\nbest by CV: {best}")
print(f"test accuracy (evaluated once): {accuracy_score(y_test, final.predict(X_test)):.3f}")

# Save and reload. Only ever load pickled/joblib files that you trust.
with tempfile.TemporaryDirectory() as d:
    path = Path(d) / "model.joblib"
    joblib.dump(final, path)
    reloaded = joblib.load(path)
    same = (reloaded.predict(X_test) == final.predict(X_test)).all()
    print("reloaded model gives identical predictions:", bool(same))
