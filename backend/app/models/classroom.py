"""Classroom Model"""

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime



class Classroom(Base):
    """Classroom model"""
    __tablename__ = "classrooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    capacity = Column(Integer, default=50)
    location = Column(String(255))
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Classroom(id={self.id}, name={self.name})>"
