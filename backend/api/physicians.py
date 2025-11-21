from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.physician import Physician

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
        query = query.filter(Physician.state == state)

    if specialty:
        query = query.filter(Physician.specialty == specialty)

    physicians = query.all()
    return [p.to_api() for p in physicians]