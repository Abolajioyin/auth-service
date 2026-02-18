from fastapi.security import OAuth2PasswordRequestForm

from app.core.dependencies import get_current_user
from fastapi import Depends

from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr


from app.core.security import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

# TEMP in-memory "database"
fake_users_db = {}  # email -> {"email":..., "hashed_password":...}


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.get("/ping")
def ping():
    return {"ok": True}


@router.get("/me")
def me(current_user=Depends(get_current_user)):
    return current_user





@router.post("/register", status_code=201)
def register(payload: RegisterRequest):
    email = payload.email.lower()

    if email in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    fake_users_db[email] = {
        "email": email,
        "hashed_password": get_password_hash(payload.password),
    }
    return {"message": "registered", "email": email}

@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    email = (form_data.username or "").lower().strip()
    password = form_data.password or ""

    user = fake_users_db.get(email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    # IMPORTANT: never let this crash
    try:
        ok = verify_password(password, user["hashed_password"])
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    if not ok:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = create_access_token({"sub": email})
    return {"access_token": token, "token_type": "bearer"}






