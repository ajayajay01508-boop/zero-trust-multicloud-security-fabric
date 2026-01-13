from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt
import datetime

app = FastAPI()

# SECRET (later move to env variable)
SECRET_KEY = "ZERO_TRUST_SECRET"
ALGORITHM = "HS256"

# ---------- Models ----------
class LoginRequest(BaseModel):
    username: str
    password: str

# ---------- Routes ----------
@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.post("/login")
def login(data: LoginRequest):
    # simple demo validation
    if data.username != "admin" or data.password != "admin123":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    payload = {
        "sub": data.username,
        "role": "admin",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": token,
        "token_type": "bearer"
    }