from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.message import Message
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/messages")
def list_messages(
    physician_id: int = None,
    start_date: str = None,
    end_date: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(Message)

    if physician_id:
        query = query.filter(Message.physician_id == physician_id)

    if start_date:
        try:
            start = datetime.fromisoformat(start_date)
            query = query.filter(Message.timestamp >= start_date)
        except:
            return {"error": "start_date must be ISO format yyyy-mm-dd"}

    if end_date:
        try:
            end = datetime.fromisoformat(end_date)
            query = query.filter(Message.timestamp <= end_date)
        except:
            return {"error": "end_date must be ISO format yyyy-mm-dd"}

    messages = query.all()
    return [m.to_api() for m in messages]