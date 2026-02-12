from app.ml.hf_model import predict as hf_predict

def run_inference(input_text: str) -> dict:
    return hf_predict(input_text)
def predict_text(text: str) -> dict:
    return hf_predict(text)




    
