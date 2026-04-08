import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("dataset.csv")

# Input and output
X = data["complaint"]
y = data["priority"]

# Convert text into numbers
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vectorized, y)

# Prediction function
def predict_priority(text):
    text_vector = vectorizer.transform([text])
    result = model.predict(text_vector)
    return result[0]