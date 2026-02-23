from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.core.dependencies import get_current_user
from app.api.ai.service import run_inference, get_model_metadata

router = APIRouter(prefix="/ai", tags=["AI"])

class PredictRequest(BaseModel):
    text: str

class PredictResponse(BaseModel):
    label: str
    confidence: float

class ModelMetadataResponse(BaseModel):
    model_id: str
    version: str
    status: str

@router.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest, current_user=Depends(get_current_user)):
    return run_inference(payload.text)

@router.get("/metadata", response_model=ModelMetadataResponse)
def metadata(current_user=Depends(get_current_user)):
    return get_model_metadata()
