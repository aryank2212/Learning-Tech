# /// script
# requires-python = ">=3.11"
# dependencies = ["scikit-learn", "pandas"]
# ///
"""A leakage-safe pipeline for mixed numeric and categorical data with missing values.

Run:  uv run 02_tabular_pipeline.py
"""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Synthetic data, so the script runs offline.
rng = np.random.default_rng(0)
n = 800
df = pd.DataFrame({
    "age": rng.integers(18, 70, n).astype(float),
    "income": rng.normal(50_000, 15_000, n),
    "city": rng.choice(["Delhi", "Pune", "Chennai"], n),
    "plan": rng.choice(["basic", "plus"], n),
})
signal = 3 * ((df["income"] - 50_000) / 20_000 + (df["plan"] == "plus") * 0.8 + (df["age"] - 40) / 40)
y = (rng.random(n) < 1 / (1 + np.exp(-signal))).astype(int)
df.loc[rng.choice(n, 50, replace=False), "income"] = np.nan   # missing numbers
df.loc[rng.choice(n, 30, replace=False), "city"] = np.nan     # missing categories

numeric, categorical = ["age", "income"], ["city", "plan"]
prep = ColumnTransformer([
    ("num", Pipeline([("impute", SimpleImputer(strategy="median")),
                      ("scale", StandardScaler())]), numeric),
    ("cat", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                      ("onehot", OneHotEncoder(handle_unknown="ignore"))]), categorical),
])
model = Pipeline([("prep", prep), ("clf", HistGradientBoostingClassifier(random_state=0))])

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.25, stratify=y, random_state=0)

search = RandomizedSearchCV(
    model,
    {"clf__learning_rate": [0.03, 0.1, 0.3],
     "clf__max_leaf_nodes": [7, 15, 31],
     "clf__l2_regularization": [0.0, 0.1, 1.0]},
    n_iter=6, cv=3, scoring="roc_auc", random_state=0,
)
search.fit(X_train, y_train)   # imputing and scaling are re-fit inside every fold

print("best parameters:", search.best_params_)
print(f"cross-validated ROC-AUC: {search.best_score_:.3f}")
test_auc = roc_auc_score(y_test, search.predict_proba(X_test)[:, 1])
print(f"held-out test ROC-AUC (looked at once): {test_auc:.3f}")
