"""Report Pydantic Schemas"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from enum import Enum


class ReportType(str, Enum):
    """Report type enum"""
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    CUSTOM = "custom"


class ExportFormat(str, Enum):
    """Export format enum"""
    PDF = "pdf"
    EXCEL = "excel"
    CSV = "csv"


class ReportCreate(BaseModel):
    """Create report schema"""
    classroom_id: int
    report_type: ReportType
    period_start: date
    period_end: date


class ReportResponse(BaseModel):
    """Report response schema"""
    id: int
    classroom_id: int
    teacher_id: int
    report_type: ReportType
    report_date: Optional[date]
    period_start: date
    period_end: date
    total_students: Optional[int]
    avg_engagement: Optional[float]
    alert_count: Optional[int]
    phone_alerts: Optional[int]
    drowsy_alerts: Optional[int]
    suspicious_count: Optional[int]
    file_path: Optional[str]
    export_format: ExportFormat
    created_at: datetime

    class Config:
        from_attributes = True
