from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.api.ai.router import router as ai_router
from app.api.auth.router import router as auth_router
from app.core.database import engine, Base
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(ai_router)

@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok", "service": "ai-inference"}





