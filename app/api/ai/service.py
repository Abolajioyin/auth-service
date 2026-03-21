def run_inference(text: str) -> dict:
    return {
        "input": text,
        "prediction": "mock_result",
        "confidence": 0.95,
        "note": "live inference coming soon"
    }

def get_model_metadata() -> dict:
    return {
        "model": "distilbert-base-uncased",
        "version": "1.0.0",
        "status": "model loading disabled on free tier",
        "inputs": ["text"]
    }
