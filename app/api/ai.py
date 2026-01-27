from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/predict")
def predict(data: dict, user=Depends(get_current_user)):
    """
    Protected AI inference endpoint
    """
    return {
        "user": user["email"],
        "prediction": "positive",
        "confidence": 0.87
    }

