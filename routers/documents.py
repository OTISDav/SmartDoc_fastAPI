from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.document import DocumentCreate
from app.services import document_service

router = APIRouter(prefix="/documents", tags=["Documents"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_document(doc: DocumentCreate, db: Session = Depends(get_db)):
    return document_service.create_document(db, doc)


@router.get("/")
def get_documents(db: Session = Depends(get_db)):
    return document_service.get_documents(db)