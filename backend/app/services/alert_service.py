"""Alert Service"""

from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.user import User


class AlertService:
    """Alert service"""

    def get_alerts(self, db: Session, current_user: User, skip: int = 0, limit: int = 50, unread_only: bool = False, alert_type: Optional[str] = None, severity: Optional[str] = None) -> list:
        """Get alerts"""
        return []

    def get_alert(self, db: Session, alert_id: int, current_user: User) -> Optional[dict]:
        """Get single alert"""
        return None

    def acknowledge_alert(self, db: Session, alert_id: int, current_user: User) -> Optional[dict]:
        """Acknowledge alert"""
        return None

    def delete_alert(self, db: Session, alert_id: int, current_user: User) -> bool:
        """Delete alert"""
        return False
