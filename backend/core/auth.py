from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Authentication"])

# 🔐 OAuth2 scheme (THIS enables Authorize button)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Dummy user
FAKE_USER = {
    "username": "admin",
    "password": "admin"
}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if (
        form_data.username != FAKE_USER["username"]
        or form_data.password != FAKE_USER["password"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    return {
        "access_token": "fake-jwt-token",
        "token_type": "bearer"
    }

@router.get("/secure-data")
def secure_data(token: str = Depends(oauth2_scheme)):
    return {"message": "Secure data accessed"}