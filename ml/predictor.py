import joblib
import os

# Load model + vectorizer once when this module is imported
_dir = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(_dir, "scam_classifier.pkl"))
vectorizer = joblib.load(os.path.join(_dir, "vectorizer.pkl"))


def predict_scam_probability(text: str) -> float:
    """
    Returns a probability (0 to 1) that the given text is a scam,
    based on the trained ML model.
    """
    vec = vectorizer.transform([text])
    probability = model.predict_proba(vec)[0][1]  # probability of class 1 (scam)
    return round(float(probability), 3)