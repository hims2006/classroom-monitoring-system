"""Alert Pydantic Schemas"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class AlertType(str, Enum):
    """Alert type enum"""
    PHONE_DETECTED = "phone_detected"
    SLEEPING = "sleeping"
    DROWSY = "drowsy"
    SUSPICIOUS_INTERACTION = "suspicious_interaction"
    LEFT_SEAT = "left_seat"
    HIGHLY_DISTRACTED = "highly_distracted"


class AlertSeverity(str, Enum):
    """Alert severity enum"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class AlertCreate(BaseModel):
    """Create alert schema"""
    student_id: Optional[int] = None
    classroom_id: int
    session_id: Optional[str] = None
    alert_type: AlertType
    severity: AlertSeverity = AlertSeverity.MEDIUM
    description: Optional[str] = None


class AlertAcknowledge(BaseModel):
    """Acknowledge alert schema"""
    pass


class AlertResponse(BaseModel):
    """Alert response schema"""
    id: int
    student_id: Optional[int]
    classroom_id: int
    session_id: Optional[str]
    alert_type: AlertType
    severity: AlertSeverity
    description: Optional[str]
    is_acknowledged: bool
    acknowledged_by: Optional[int]
    acknowledged_at: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True
