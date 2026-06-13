"""User Model"""

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum

from datetime import datetime
import enum




class UserRole(str, enum.Enum):
    """User role enumeration"""
    ADMIN = "admin"
    TEACHER = "teacher"


class User(Base):
    """User model for Admin and Teachers"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.TEACHER, nullable=False, index=True)
    full_name = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, role={self.role})>"
