from app.ml.hf_model import predict as hf_predict
from app.ml.hf_model import metadata as hf_metadata


def run_inference(text: str) -> dict:
    return hf_predict(text)


def get_model_metadata() -> dict:
    return hf_metadata()