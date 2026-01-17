from fastapi import FastAPI
from auth.auth import router as auth_router

app = FastAPI(
    title="Aurexia Zero Trust Security Fabric",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"status": "Backend is running"}

app.include_router(auth_router)
