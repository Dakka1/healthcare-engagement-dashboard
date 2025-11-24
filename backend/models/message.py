from sqlalchemy import Column, Integer, String, Float
from backend.database import Base

class Message(Base):
    __tablename__ = "messages"

    message_id = Column(Integer, primary_key=True, index=True)
    physician_id = Column(Integer, index=True)
    channel = Column(String)
    direction = Column(String)
    timestamp = Column(String)
    message_text = Column(String)
    campaign_id = Column(String)
    topic = Column(String)
    compliance_tag = Column(String)
    sentiment = Column(String)
    delivery_status = Column(String)
    response_latency_sec = Column(Float)

    def to_api(self):
        return {
            "id": self.message_id,
            "physician_id": self.physician_id,
            "timestamp": self.timestamp,
            "topic": self.topic,
            "sentiment": self.sentiment
        }