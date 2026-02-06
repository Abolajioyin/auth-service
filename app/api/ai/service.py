# app/api/ai/service.py

def run_inference(input_text: str) -> dict:
    """
    Dummy AI inference logic.
    Replace this later with a real ML model.
    """
    # Fake "model" logic
    score = len(input_text) % 2

    return {
        "label": "positive" if score == 1 else "negative",
        "confidence": 0.87
    }
from pathlib import Path
import joblib

MODEL_PATH = Path("ml") / "artifacts" / "sentiment_model.joblib"
MODEL_VERSION = "v1"

_model = None

def load_model():
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_text(text: str) -> dict:
    model = load_model()
    proba_pos = float(model.predict_proba([text])[0][1])
    prediction = "positive" if proba_pos >= 0.5 else "negative"
    confidence = proba_pos if prediction == "positive" else (1.0 - proba_pos)

    return {
        "prediction": prediction,
        "confidence": round(confidence, 4),
        "model_version": MODEL_VERSION,
    }
