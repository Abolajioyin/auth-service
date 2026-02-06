from pathlib import Path
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Tiny starter dataset (fast, CPU-light). Replace later with real data.
TRAIN_DATA = [
    ("I love this", 1),
    ("This is amazing", 1),
    ("Best thing ever", 1),
    ("I hate this", 0),
    ("This is terrible", 0),
    ("Worst experience", 0),
    ("Not good at all", 0),
    ("Very satisfied", 1),
]

def main():
    X = [t for t, y in TRAIN_DATA]
    y = [y for t, y in TRAIN_DATA]

    model = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2))),
            ("clf", LogisticRegression(max_iter=200)),
        ]
    )

    model.fit(X, y)

    artifacts_dir = Path("ml") / "artifacts"
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    model_path = artifacts_dir / "sentiment_model.joblib"
    joblib.dump(model, model_path)

    # Quick sanity test
    sample = "I really love this project"
    proba = model.predict_proba([sample])[0][1]
    label = "positive" if proba >= 0.5 else "negative"

    print(f"✅ Saved: {model_path}")
    print(f"🧪 Test: '{sample}' -> {label} ({proba:.2f})")

if __name__ == "__main__":
    main()
