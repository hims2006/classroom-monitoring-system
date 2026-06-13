"""Student Model"""

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime, LargeBinary, ForeignKey

from datetime import datetime




class Student(Base):
    """Student model"""
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    roll_number = Column(String(50), unique=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100))
    classroom_id = Column(Integer, ForeignKey("classrooms.id", ondelete="CASCADE"), nullable=False, index=True)
    face_encoding = Column(LargeBinary)
    enrollment_date = Column(Date)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, roll={self.roll_number})>"
