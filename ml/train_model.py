import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# ---- Load dataset ----
df = pd.read_csv("dataset.csv")

X = df["text"]
y = df["label"]

# ---- Split into train/test ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---- Convert text to TF-IDF features ----
vectorizer = TfidfVectorizer(stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ---- Train classifier ----
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# ---- Evaluate ----
predictions = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy on test set: {accuracy:.2f}")

# ---- Save model + vectorizer for later use ----
joblib.dump(model, "scam_classifier.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model and vectorizer saved successfully.")