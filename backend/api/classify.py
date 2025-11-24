from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.message import Message
import json
import os

router = APIRouter()

# # Load compliance rules ONCE
# COMPLIANCE_PATH = "backend/data/compliance_policies.json"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPLIANCE_PATH = os.path.join(BASE_DIR, "data", "compliance_policies.json")

with open(COMPLIANCE_PATH, "r") as f:
    COMPLIANCE_RULES = json.load(f)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/classify/{message_id}")
def classify_message(message_id: int, db: Session = Depends(get_db)):
    msg = db.query(Message).filter(Message.message_id == message_id).first()
    if not msg:
        return {"error": f"Message {message_id} not found"}

    text = msg.message_text.lower()

    triggered = []

    for rule in COMPLIANCE_RULES["rules"]:
        rule_keywords = rule.get("keywords_any", [])

        matched = [kw for kw in rule_keywords if kw.lower() in text]

        if matched:
            triggered.append({
                "rule_id": rule["id"],
                "rule_name": rule["name"],
                "matched_keywords": matched,
                "action": rule.get("action"),
                "requires_append": rule.get("requires_append")
            })

    return {
        "message_id": message_id,
        "message_text": msg.message_text,
        "triggered_rules": triggered
    }