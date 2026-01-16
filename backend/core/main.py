from fastapi import FastAPI

app = FastAPI(
    title="Aurexia Zero Trust Security Fabric",
       version="0.1.0"
)
@app.get("/")
def root():
    return {"status": "Backend is running"}
