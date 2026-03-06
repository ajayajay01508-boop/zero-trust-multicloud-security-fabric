from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from jose import jwt, JWTError

# =====================
# CONFIG
# =====================
SECRET_KEY = "AUREXIA_SECRET_KEY"  # keep this same every time
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

router = APIRouter(prefix="/auth", tags=["Auth"])
bearer_scheme = HTTPBearer()

# =====================
# FAKE USER STORE
# =====================
fake_users_db = {
    "admin": {
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    },
    "john": {
        "username": "john",
        "password": "john123",
        "role": "user"
    },
    "auditor": {
        "username": "audit",
        "password": "audit123",
        "role": "auditor"
    }
}

# =====================
# TOKEN CREATION
# =====================
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# =====================
# LOGIN
# =====================
from fastapi import Form

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    user = fake_users_db.get(username)
    if not user or user["password"] != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={"sub": user["username"], "role": user["role"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": access_token, "token_type": "bearer"}

# =====================
# ZERO TRUST VALIDATION
# =====================
def zero_trust_auth(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Zero Trust: Invalid token"
        )

# =====================
# PROTECTED ENDPOINT
# =====================
@router.get("/secure-data")
def secure_data(user=Depends(zero_trust_auth)):
    return {
        "message": "Zero Trust Access Granted",
        "user": user
    }
@router.get("/admin-data")
def admin_data(user=Depends(zero_trust_auth)):
    if user.get("role") != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admins only"
        )

    return {
        "message": "Admin-level data access granted",
        "user": {
            "sub": user["sub"],
            "role": user["role"]
        }
    }
