# scikit-learn syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md).

### Phase 1 – The estimator API
- [ ] `fit`, `predict`, `transform`, `score`
- [ ] Bundled datasets (iris, digits) and `train_test_split`
- [ ] Stratified splits; why random seeds matter

🛠️ Project: a baseline classifier on iris, with the test set used once.

### Phase 2 – Preprocessing
- [ ] Scaling: `StandardScaler`, `MinMaxScaler`
- [ ] Encoding: `OneHotEncoder`, `OrdinalEncoder`
- [ ] Missing values: `SimpleImputer`
- [ ] `ColumnTransformer` and `Pipeline`
- [ ] Data leakage, and how pipelines prevent it

🛠️ Project: a pipeline for a dataset with numeric, categorical and missing values.

### Phase 3 – Supervised learning
- [ ] Linear and logistic regression; regularisation (Ridge, Lasso, ElasticNet)
- [ ] k-nearest neighbours, decision trees
- [ ] Random forests and gradient boosting (`HistGradientBoosting`)
- [ ] Support vector machines
- [ ] Choosing a model by data size and type

🛠️ Project: compare five models with cross-validation on the same data.

### Phase 4 – Evaluation
- [ ] Classification metrics: accuracy, precision, recall, F1, ROC-AUC, PR-AUC
- [ ] Regression metrics: MAE, RMSE, R²
- [ ] `KFold`, `StratifiedKFold`, `GroupKFold`, `TimeSeriesSplit`
- [ ] Confusion matrices, learning curves, calibration

🛠️ Project: an evaluation report with a baseline, several metrics and an error analysis.

### Phase 5 – Tuning and selection
- [ ] `GridSearchCV` and `RandomizedSearchCV`
- [ ] Successive halving
- [ ] Nested cross-validation for an honest estimate
- [ ] Hyperparameter search with Optuna

🛠️ Project: tune a gradient-boosting model and report an honest score.

### Phase 6 – Unsupervised learning
- [ ] Clustering: k-means, DBSCAN, hierarchical, Gaussian mixtures
- [ ] Dimensionality reduction: PCA, t-SNE
- [ ] Anomaly detection: `IsolationForest`
- [ ] Judging clusters: silhouette score, and the limits of it

🛠️ Project: segment customers, and describe each segment in plain language.

### Phase 7 – Text and features
- [ ] `CountVectorizer`, `TfidfVectorizer`
- [ ] Feature selection and polynomial features
- [ ] `FunctionTransformer` and custom transformers (`BaseEstimator`, `TransformerMixin`)

🛠️ Project: a spam or topic classifier with an error analysis.

### Phase 8 – Interpretation
- [ ] Coefficients and feature importances, and why they can mislead
- [ ] Permutation importance and partial dependence
- [ ] SHAP values (external library)
- [ ] Checking performance by group (see [tech ethics](../../../security/ethics/tech-ethics/README.md))

🛠️ Project: explain a model's top five drivers and check its error rate for each group.

### Phase 9 – Saving and deploying
- [ ] `joblib` persistence, and why you only load files you trust
- [ ] Exporting to ONNX with `skl2onnx`
- [ ] Serving a pipeline behind an API
- [ ] Monitoring for drift

🛠️ Project: package a pipeline, serve it, and call it from another language.

### Phase 10 – Scale and ecosystem
- [ ] `partial_fit` and out-of-core learning
- [ ] `n_jobs` and parallelism
- [ ] XGBoost, LightGBM and CatBoost
- [ ] Imbalanced data with `imbalanced-learn`
- [ ] GPU acceleration with cuML (concept)

🛠️ Project: benchmark scikit-learn against LightGBM on a larger dataset.

### Capstone
🛠️ Project: an end-to-end tabular project with a baseline, a leakage-safe pipeline, tuning, a final test score, an error analysis and a short report.
