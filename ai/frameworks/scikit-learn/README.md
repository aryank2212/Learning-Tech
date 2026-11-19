# scikit-learn

The standard Python library for classical machine learning: preprocessing, models for classification, regression and clustering, and the tools to evaluate and tune them. It is also the best place to learn the machine-learning workflow before you move on to deep learning.

## Why learn it
- **One consistent API.** Almost everything is `fit`, then `predict` or `transform`. Learn it once and you can use hundreds of models.
- **It teaches the workflow.** Split the data, preprocess, fit, evaluate, tune. You can practise all of it on a laptop, with no GPU.
- **It often wins on tabular data.** For spreadsheet-style data, a well-tuned gradient-boosting model (scikit-learn's `HistGradientBoosting`, XGBoost or LightGBM) usually beats a neural network.

## Prerequisites
- Python at Level 2 (see [Python](../../../languages/general/python/README.md))
- NumPy and pandas basics (see [data science](../../../data/science/data-science/README.md))
- Mean, variance and basic probability (see [maths](../../../foundations/mathematics/maths/syllabus.md))

## Install
```bash
uv init sklearn-lab --python 3.13 && cd sklearn-lab
uv add scikit-learn pandas matplotlib
uv run python -c "import sklearn; print(sklearn.__version__)"
```
Use a project like this rather than your system Python. Each example in [examples/](examples/) also declares its own dependencies, so you can run one directly:
```bash
uv run ai/frameworks/scikit-learn/examples/01_quickstart.py
```

## Quick start
```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=0)

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=200))
model.fit(X_train, y_train)
print(model.score(X_test, y_test))      # accuracy on data the model has never seen: 0.967
```
The pipeline matters: the scaler learns its mean and spread from the training data only, so nothing from the test set leaks into training.

## The API in one table
| Idea | Methods | Examples |
|---|---|---|
| Estimator | `fit(X, y)` | every model and transformer |
| Predictor | `predict`, `predict_proba`, `score` | `LogisticRegression`, `RandomForestClassifier` |
| Transformer | `fit`, `transform`, `fit_transform` | `StandardScaler`, `OneHotEncoder`, `PCA` |
| Pipeline | chains steps, fits them together | `make_pipeline`, `ColumnTransformer` |
| Model selection | splits and searches | `train_test_split`, `cross_val_score`, `GridSearchCV` |

## Examples in this folder
All four run offline in a few seconds.
| File | What it shows |
|---|---|
| [01_quickstart.py](examples/01_quickstart.py) | Split, pipeline, evaluate, cross-validate |
| [02_tabular_pipeline.py](examples/02_tabular_pipeline.py) | Mixed numeric and categorical data with missing values, tuned with `RandomizedSearchCV` |
| [03_compare_models.py](examples/03_compare_models.py) | Five models compared fairly with cross-validation, then the winner tested once, saved and reloaded |
| [04_text_classifier.py](examples/04_text_classifier.py) | TF-IDF text classification, and a look at which words drive each class |

## Weekly rhythm
- One dataset a week: baseline first, then one improvement at a time, and write down what each change did.
- Always keep a test set you only look at once, at the end.

## Files
- [syllabus.md](syllabus.md): phases with projects
- [resources.md](resources.md): the official guide, courses, books and companion libraries
- [practice.md](practice.md): tasks at three levels, and a quiz
- [examples/](examples/): four runnable scripts

## My personal take
*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- Learn this before deep learning. It teaches the whole workflow (split, pipeline, evaluate, tune) on problems small enough to understand.
- Use pipelines from the first day. Most "amazing" results I see in beginner projects come from fitting a scaler or an encoder on all the data before splitting.
- Beat a simple baseline before you reach for anything fancy. A logistic regression that gets 0.85 tells you what a neural network has to beat.
- Don't skip the "Common pitfalls" page in the official docs. It is short and it covers the mistakes I see most.
