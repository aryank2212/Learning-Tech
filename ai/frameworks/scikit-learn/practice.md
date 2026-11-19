# Practice: scikit-learn

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Load iris, split it 80/20 with stratification, fit a `LogisticRegression` and print its accuracy.
- [ ] Compare k-nearest-neighbours accuracy on the digits dataset with and without `StandardScaler`.
- [ ] Plot a confusion matrix for a random forest on the digits dataset.

## Level 2 — Medium (apply it)

- [ ] Build a `Pipeline` with a `ColumnTransformer` for numeric and categorical columns, and evaluate it with 5-fold cross-validation.
- [ ] Tune a random forest with `GridSearchCV`; report the best parameters, the cross-validated score and the final test score.
- [ ] Handle class imbalance with `class_weight`, and compare precision-recall AUC with and without it.

## Level 3 — Hard (build and explain)

- [ ] Write a custom transformer (`BaseEstimator`, `TransformerMixin`) and use it inside a pipeline under cross-validation, without leakage.
- [ ] Build a text classification pipeline with `TfidfVectorizer`, then inspect the 20 most confident mistakes and say what they have in common.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. Why use a `Pipeline`?

   <details><summary>Show answer</summary>

   It keeps preprocessing and the model together, so transformers are fit only on the training part of each fold (no leakage) and the same steps run at prediction time.

   </details>

2. What's the difference between `fit_transform` on training data and `transform` on test data?

   <details><summary>Show answer</summary>

   `fit` learns parameters (such as a mean and standard deviation) from the training data only. `transform` applies them to new data. Never fit on the test set.

   </details>

3. When should you use `StratifiedKFold`?

   <details><summary>Show answer</summary>

   For classification, especially with imbalanced classes. It keeps the class proportions the same in every fold.

   </details>

4. Why is loading a pickled model from an untrusted source dangerous?

   <details><summary>Show answer</summary>

   Unpickling can run arbitrary code. Only load files you trust, or use a safer format such as ONNX or `skops`.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
