from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.api.ai.service import predict_text
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/ai", tags=["AI"])

class PredictRequest(BaseModel):
    text: str = Field(min_length=1, max_length=2000)

class PredictResponse(BaseModel):
    prediction: str
    confidence: float
    model_version: str

@router.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest, _user=Depends(get_current_user)):
    return predict_text(payload.text)

