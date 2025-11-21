from sqlalchemy import Column, Integer, String, Boolean
from backend.database import Base

class Physician(Base):
    __tablename__ = "physicians"

    physician_id = Column(Integer, primary_key=True, index=True)
    npi = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    specialty = Column(String)
    state = Column(String)
    consent_opt_in = Column(Boolean)
    preferred_channel = Column(String)

    def to_api(self):
        return {
            "id": self.physician_id,
            "name": f"{self.first_name} {self.last_name}",
            "specialty": self.specialty,
            "state": self.state,
            "channel_preference": self.preferred_channel
        }