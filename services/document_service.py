from app.models.document import Document
from app.redis import redis_client

def create_document(db, doc):
    new_doc = Document(**doc.dict())
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)

    redis_client.set(f"doc:{new_doc.id}", new_doc.title)

    return new_doc


def get_documents(db):
    return db.query(Document).all()