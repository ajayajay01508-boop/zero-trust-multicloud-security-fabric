from fastapi import FastAPI
from app.routes.auth import router as auth_router

app = FastAPI(title="Zero Trust MultiCloud Security Fabric")

# Include Auth Routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])


@app.get("/")
def root():
    return {"message": "API is running successfully 🚀"}
