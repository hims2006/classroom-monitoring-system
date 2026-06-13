"""Student Pydantic Schemas"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime


class StudentCreate(BaseModel):
    """Create student schema"""
    roll_number: str = Field(..., min_length=1, max_length=50)
    name: str = Field(..., min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    classroom_id: int
    enrollment_date: Optional[date] = None


class StudentUpdate(BaseModel):
    """Update student schema"""
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    enrollment_date: Optional[date] = None
    is_active: Optional[bool] = None


class StudentResponse(BaseModel):
    """Student response schema"""
    id: int
    roll_number: str
    name: str
    email: Optional[str]
    classroom_id: int
    enrollment_date: Optional[date]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
