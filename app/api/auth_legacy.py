print("AUTH ROUTER LOADED")

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr

from app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token
)
router = APIRouter(prefix="/auth", tags=["auth"])

# TEMP in-memory user store
fake_users_db = {}


# =====================
# Schemas
# =====================
class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# =====================
# Register
# =====================
@router.post("/register", status_code=201)
def register_user(payload: RegisterRequest):
    if payload.email in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    fake_users_db[payload.email] = {
        "email": payload.email,
        "hashed_password": get_password_hash(payload.password)
    }

    return {"message": "User registered successfully"}


# =====================
# Login
# =====================
@router.post("/login", response_model=TokenResponse)
def login_user(payload: LoginRequest):
    user = fake_users_db.get(payload.email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    if not verify_password(payload.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={"sub": payload.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


