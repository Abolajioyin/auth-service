# app/ml/hf_model.py
from transformers import pipeline

# Loads once when the server starts
_classifier = pipeline("sentiment-analysis")

def predict(text: str) -> dict:
    result = _classifier(text)[0]  # {'label': 'POSITIVE', 'score': 0.999...}
    return {
        "label": result["label"].lower(),
        "confidence": float(result["score"]),
    }
