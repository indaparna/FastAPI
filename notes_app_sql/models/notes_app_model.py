from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from configurations import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    task_done = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
