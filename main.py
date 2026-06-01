from fastapi import FastAPI
from routers import documents, analytics

app = FastAPI(title="SmartDoc_fastAPI")

app.include_router(documents.router)
# app.include_router(analytics.router)

@app.get("/")
def home():
    return {"message": "SmartDoc API running"}