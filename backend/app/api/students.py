"""Student Management Endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from app.schemas.student import StudentCreate, StudentUpdate, StudentResponse
from app.services.student_service import StudentService
from app.utils.db import get_db
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter()
student_service = StudentService()


@router.get("/", response_model=List[StudentResponse])
async def list_students(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
):
    """List all students"""
    students = student_service.get_students(db, current_user, skip, limit)
    return students


@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
async def create_student(
    student_data: StudentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new student"""
    try:
        student = student_service.create_student(db, student_data, current_user)
        return StudentResponse.from_orm(student)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(
    student_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get student details"""
    student = student_service.get_student(db, student_id, current_user)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return StudentResponse.from_orm(student)


@router.put("/{student_id}", response_model=StudentResponse)
async def update_student(
    student_id: int,
    student_data: StudentUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update student information"""
    try:
        student = student_service.update_student(db, student_id, student_data, current_user)
        if not student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        return StudentResponse.from_orm(student)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(
    student_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a student"""
    success = student_service.delete_student(db, student_id, current_user)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return None


@router.get("/search/{query}")
async def search_students(
    query: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Search students by name or roll number"""
    students = student_service.search_students(db, query, current_user)
    return {"results": students, "count": len(students)}
