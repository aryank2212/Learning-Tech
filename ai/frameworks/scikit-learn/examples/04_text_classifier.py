# /// script
# requires-python = ">=3.11"
# dependencies = ["scikit-learn"]
# ///
"""A tiny text classifier with TF-IDF. The corpus is a toy, so use it to learn the shape, not for accuracy.

Run:  uv run 04_text_classifier.py
"""
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

texts = [
    "the compiler reported a syntax error in the function",
    "we deployed the new server to the cloud cluster",
    "the database query was slow until we added an index",
    "she refactored the code and fixed the failing test",
    "the neural network trained on a gpu for two hours",
    "the server crashed after the update and we rolled back",
    "a bug in the deployment script broke the build",
    "the api returned an error from the server",
    "the team shipped the release after the tests passed",
    "he wrote a script to deploy the application",
    "the striker scored twice in the second half",
    "our team won the championship after a penalty shootout",
    "the coach changed the lineup before the final match",
    "he ran the marathon in under three hours",
    "the goalkeeper saved a late penalty to win the game",
    "the team scored a late goal to win the match",
    "a late goal sealed the win for the home team",
    "the players trained hard before the season opener",
    "she scored the winning goal in the final",
    "the crowd cheered as the team lifted the trophy",
]
labels = ["tech"] * 10 + ["sports"] * 10

model = make_pipeline(TfidfVectorizer(ngram_range=(1, 2)), LogisticRegression(max_iter=500))
model.fit(texts, labels)

new = ["the home team scored in the final minute", "the server crashed during the deployment"]
for text, pred in zip(new, model.predict(new)):
    print(f"{pred:7s} <- {text}")

# Look inside: which words push towards each class?
vec, clf = model.named_steps["tfidfvectorizer"], model.named_steps["logisticregression"]
names = np.array(vec.get_feature_names_out())
order = np.argsort(clf.coef_[0])
print("most 'sports' terms:", list(names[order[:5]]))
print("most 'tech' terms:  ", list(names[order[-5:]]))
