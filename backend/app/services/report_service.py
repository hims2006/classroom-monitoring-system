"""Report Service"""

from sqlalchemy.orm import Session
from typing import Optional

from app.models.user import User
from app.schemas.report import ReportCreate


class ReportService:
    """Report service"""

    def generate_report(self, db: Session, report_data: ReportCreate, current_user: User):
        """Generate report"""
        return None

    def get_reports(self, db: Session, current_user: User, skip: int = 0, limit: int = 50, report_type: Optional[str] = None) -> list:
        """Get reports"""
        return []

    def get_report(self, db: Session, report_id: int, current_user: User):
        """Get report details"""
        return None

    def export_report(self, db: Session, report_id: int, format: str, current_user: User) -> str:
        """Export report"""
        return ""

    def delete_report(self, db: Session, report_id: int, current_user: User) -> bool:
        """Delete report"""
        return False
