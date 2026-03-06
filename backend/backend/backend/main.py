from fastapi import FastAPI, Depends
from auth.auth import router as auth_router
from auth.auth import zero_trust_auth
from core.policy import evaluate_policy

app = FastAPI(
    title="Aurexia Zero Trust Security Fabric",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.get("/admin-data")
def admin_data(user: dict = Depends(zero_trust_auth)):
    role = user.get("role")
    evaluate_policy(role, resource="admin", action="read")
    return {"message": "Admin access granted"}

# ✅ THIS LINE IS WHAT MAKES /auth SHOW
app.include_router(auth_router)
