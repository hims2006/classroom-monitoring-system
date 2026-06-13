"""Attendance Pydantic Schemas"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from enum import Enum


class AttendanceStatus(str, Enum):
    """Attendance status enum"""
    PRESENT = "present"
    ABSENT = "absent"
    LATE = "late"
    LEFT_EARLY = "left_early"


class AttendanceMethod(str, Enum):
    """Attendance method enum"""
    AUTO_AI = "auto_ai"
    MANUAL = "manual"


class AttendanceCreate(BaseModel):
    """Create attendance schema"""
    student_id: int
    classroom_id: int
    session_id: Optional[str] = None
    attendance_date: date
    status: AttendanceStatus = AttendanceStatus.PRESENT
    method: AttendanceMethod = AttendanceMethod.AUTO_AI
    notes: Optional[str] = None


class AttendanceUpdate(BaseModel):
    """Update attendance schema"""
    status: Optional[AttendanceStatus] = None
    notes: Optional[str] = None


class AttendanceResponse(BaseModel):
    """Attendance response schema"""
    id: int
    student_id: int
    classroom_id: int
    session_id: Optional[str]
    attendance_date: date
    check_in_time: Optional[datetime]
    check_out_time: Optional[datetime]
    duration_minutes: Optional[int]
    status: AttendanceStatus
    method: AttendanceMethod
    notes: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
