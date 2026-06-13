"""Alert Management Endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from app.schemas.alert import AlertResponse, AlertAcknowledge
from app.services.alert_service import AlertService
from app.utils.db import get_db
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter()
alert_service = AlertService()


@router.get("/", response_model=List[AlertResponse])
async def list_alerts(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    unread_only: bool = Query(False),
    alert_type: str = Query(None),
    severity: str = Query(None),
):
    """List alerts with optional filters"""
    alerts = alert_service.get_alerts(
        db,
        current_user,
        skip,
        limit,
        unread_only,
        alert_type,
        severity,
    )
    return alerts


@router.get("/{alert_id}", response_model=AlertResponse)
async def get_alert(
    alert_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get alert details"""
    alert = alert_service.get_alert(db, alert_id, current_user)
    if not alert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alert not found")
    return AlertResponse.from_orm(alert)


@router.put("/{alert_id}/acknowledge")
async def acknowledge_alert(
    alert_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Mark alert as acknowledged"""
    alert = alert_service.acknowledge_alert(db, alert_id, current_user)
    if not alert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alert not found")
    return {"message": "Alert acknowledged", "alert_id": alert_id}


@router.delete("/{alert_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_alert(
    alert_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete alert"""
    success = alert_service.delete_alert(db, alert_id, current_user)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alert not found")
    return None
