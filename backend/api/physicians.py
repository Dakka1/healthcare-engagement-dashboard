from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.physician import Physician
from sqlalchemy import func

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/physicians")
def list_physicians(state: str = None, specialty: str = None, db: Session = Depends(get_db)):
    query = db.query(Physician)

    if state:
        query = query.filter(func.lower(Physician.state) == state.lower())


    if specialty:
        query = query.filter(func.lower(Physician.specialty) == specialty.lower())

    physicians = query.all()
    return [p.to_api() for p in physicians]