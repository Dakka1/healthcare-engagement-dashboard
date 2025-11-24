from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.message import Message
from datetime import datetime
from datetime import timedelta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/messages")
def list_messages(
    physician_id: int = Query(
        None,
        description="Filter messages by physician id"
    ),
    start_date: str = Query(
        None,
        description="Start date in ISO format yyyy-mm-dd"
    ),
    end_date: str = Query(
        None,
        description="End date in ISO format yyyy-mm-dd"
    ),
    db: Session = Depends(get_db)
):
    """
    List messages filtered by physician_id and optional date range.
    Dates must be provided in ISO format yyyy-mm-dd.
    end_date is inclusive.
    """

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
            end = datetime.fromisoformat(end_date) + timedelta(days=1)
            query = query.filter(Message.timestamp < end)
        except:
            return {"error": "end_date must be ISO format yyyy-mm-dd"}

    messages = query.all()
    return [m.to_api() for m in messages]