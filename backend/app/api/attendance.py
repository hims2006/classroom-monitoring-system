"""Attendance Management Endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from datetime import date
from typing import List

from app.schemas.attendance import AttendanceCreate, AttendanceUpdate, AttendanceResponse
from app.services.attendance_service import AttendanceService
from app.utils.db import get_db
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter()
attendance_service = AttendanceService()


@router.get("/", response_model=List[AttendanceResponse])
async def list_attendance(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    attendance_date: date = Query(None),
):
    """List attendance records"""
    records = attendance_service.get_attendance(
        db, current_user, skip, limit, attendance_date
    )
    return records


@router.post("/log", response_model=AttendanceResponse, status_code=status.HTTP_201_CREATED)
async def log_attendance(
    attendance_data: AttendanceCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Log attendance (AI auto or manual)"""
    try:
        attendance = attendance_service.log_attendance(
            db, attendance_data, current_user
        )
        return AttendanceResponse.from_orm(attendance)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/student/{student_id}")
async def get_student_attendance(
    student_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    limit: int = Query(30, ge=1, le=100),
):
    """Get student attendance history"""
    history = attendance_service.get_student_attendance_history(
        db, student_id, current_user, limit
    )
    return {"records": history, "count": len(history)}


@router.get("/report")
async def get_attendance_report(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    start_date: date = Query(None),
    end_date: date = Query(None),
):
    """Get attendance report"""
    report = attendance_service.get_attendance_report(
        db, current_user, start_date, end_date
    )
    return report
