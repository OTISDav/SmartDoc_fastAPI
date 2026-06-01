from fastapi import FastAPI
from app.routers import documents, analytics

app = FastAPI(title="SmartDoc API")

app.include_router(documents.router)
app.include_router(analytics.router)

@app.get("/")
def home():
    return {"message": "SmartDoc API running"}