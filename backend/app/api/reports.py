"""Reports and Analytics Endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from datetime import date
from typing import List

from app.schemas.report import ReportCreate, ReportResponse
from app.services.report_service import ReportService
from app.utils.db import get_db
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter()
report_service = ReportService()


@router.post("/generate", response_model=ReportResponse, status_code=status.HTTP_201_CREATED)
async def generate_report(
    report_data: ReportCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Generate a new report"""
    try:
        report = report_service.generate_report(db, report_data, current_user)
        return ReportResponse.from_orm(report)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=List[ReportResponse])
async def list_reports(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    report_type: str = Query(None),
):
    """List generated reports"""
    reports = report_service.get_reports(db, current_user, skip, limit, report_type)
    return reports


@router.get("/{report_id}", response_model=ReportResponse)
async def get_report(
    report_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get report details"""
    report = report_service.get_report(db, report_id, current_user)
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")
    return ReportResponse.from_orm(report)


@router.post("/{report_id}/export")
async def export_report(
    report_id: int,
    format: str = Query("pdf", regex="^(pdf|excel|csv)$"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Export report as PDF, Excel, or CSV"""
    try:
        file_path = report_service.export_report(db, report_id, format, current_user)
        return {"file_path": file_path, "format": format}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{report_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_report(
    report_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a report"""
    success = report_service.delete_report(db, report_id, current_user)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")
    return None
