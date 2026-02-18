# app/ml/hf_model.py
from transformers import pipeline

MODEL_NAME = "sentiment-analysis"
MODEL_VERSION = "v1"

# Loads once when the server starts
_classifier = pipeline("sentiment-analysis")

def predict(text: str) -> dict:
    result = _classifier(text)[0]  # {'label': 'POSITIVE', 'score': 0.999...}
    return {
        "label": result["label"].lower(),
        "confidence": float(result["score"]),
    }
def metadata() -> dict:
    return {
        "model": MODEL_NAME,
        "version": MODEL_VERSION,
        "status": "loaded" if _classifier is not None else "not_loaded",
    }

