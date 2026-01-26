from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from uuid import uuid4

from app.core.security import get_password_hash

router = APIRouter(prefix="/auth", tags=["auth"])

# In-memory user store (temporary)
fake_users_db = {}


class RegisterRequest(BaseModel):
    email: EmailStr
    username: str
    password: str


class RegisterResponse(BaseModel):
    id: str
    email: EmailStr
    username: str


@router.post("/register", response_model=RegisterResponse)
def register_user(data: RegisterRequest):
    if data.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_id = str(uuid4())
    hashed_password = get_password_hash(data.password)

    fake_users_db[data.email] = {
        "id": user_id,
        "email": data.email,
        "username": data.username,
        "hashed_password": hashed_password,
    }

    return {
        "id": user_id,
        "email": data.email,
        "username": data.username,
    }
