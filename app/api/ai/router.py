from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from app.api.ai.service import run_inference, get_model_metadata, get_stats
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/ai", tags=["AI"])

class PredictRequest(BaseModel):
    text: str = Field(min_length=1, max_length=2000)

class PredictResponse(BaseModel):
    prediction: str
    confidence: float
    model_version: str

class ModelMetadataResponse(BaseModel):
    model: str
    version: str
    status: str    

class StatsResponse(BaseModel):
    total_requests: int
    label_counts: dict
    avg_latency_ms: float
    last_request_at: str | None

@router.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest, _user=Depends(get_current_user)):
    return run_inference(payload.text)

@router.get("/metadata", response_model=ModelMetadataResponse)
def metadata(_user=Depends(get_current_user)):
    return get_model_metadata()

@router.get("/stats", response_model=StatsResponse)
def stats(_user=Depends(get_current_user)):
    return get_stats()