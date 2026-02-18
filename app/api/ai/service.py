from app.ml.hf_model import predict as hf_predict
from app.ml.hf_model import metadata as hf_metadata
from app.api.ai.metrics import metrics

def run_inference(input_text: str) -> dict:
    start = time.perf_counter()
    result = hf_predict(input_text)
    latency_ms = (time.perf_counter() - start) * 1000
   # result must include "label"
    metrics.record(label=result["label"], latency_ms=latency_ms)
    return hf_predict(input_text)

def get_model_metadata() -> dict:
    return hf_metadata()

def get_stats() -> dict:
    return {
        "total_requests": metrics.total_requests,
        "label_counts": metrics.label_counts,
        "avg_latency_ms": metrics.avg_latency_ms,
        "last_request_at": metrics.last_request_at,
    }

def predict_text(text: str) -> dict:
    return hf_predict(text)




    
