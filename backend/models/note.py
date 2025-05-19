from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.database import Base

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    original_text = Column(Text, nullable=False)
    summary_text = Column(Text, nullable=False)
    tags = Column(String, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")
