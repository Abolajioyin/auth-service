from transformers import pipeline

# Load once at startup (VERY IMPORTANT)
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def predict(text: str) -> dict:
    result = classifier(text)[0]
    return {"label": result["label"], "score": float(result["score"])}
