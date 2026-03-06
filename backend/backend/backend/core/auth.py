# core/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from core.policy import evaluate_policy  # make sure core/policy.py exists

router = APIRouter()

# OAuth2 scheme (enables Authorize button in Swagger)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Dummy user (for testing)
FAKE_USER = {
    "username": "admin",
    "password": "admin",
    "role": "admin"
}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != FAKE_USER["username"] or form_data.password != FAKE_USER["password"]:
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
    # Here you can implement more checks if needed
    return {"message": "Zero Trust Access Granted", "user": {"sub": FAKE_USER["username"], "role": FAKE_USER["role"], "exp": 123456789}}

# Zero Trust enforcement function
def enforce_zero_trust(user: dict, resource: str, action: str):
    allowed = evaluate_policy(
        subject=user.get("role"),
        resource=resource,
        action=action
    )
    if not allowed:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Zero Trust Policy Denied"
        )




