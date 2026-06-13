"""Dashboard Endpoints"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.services.analytics_service import AnalyticsService
from app.utils.db import get_db
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter()
analytics_service = AnalyticsService()


@router.get("/summary")
async def get_dashboard_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get dashboard summary with KPIs"""
    summary = analytics_service.get_dashboard_summary(db, current_user)
    return summary


@router.get("/engagement")
async def get_engagement(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get real-time class engagement"""
    engagement = analytics_service.get_class_engagement(db, current_user)
    return engagement


@router.get("/alerts")
async def get_recent_alerts(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    limit: int = 10,
):
    """Get recent alerts"""
    alerts = analytics_service.get_recent_alerts(db, current_user, limit)
    return {"alerts": alerts, "count": len(alerts)}


@router.get("/trends")
async def get_trends(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    days: int = 7,
):
    """Get historical trends"""
    trends = analytics_service.get_engagement_trends(db, current_user, days)
    return trends
