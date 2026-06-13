"""Student Service"""

from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional

from app.models.student import Student
from app.models.classroom import Classroom
from app.models.user import User
from app.schemas.student import StudentCreate, StudentUpdate


class StudentService:
    """Student service"""

    def get_students(self, db: Session, current_user: User, skip: int = 0, limit: int = 50) -> List[Student]:
        """Get students for teacher's classrooms"""
        query = db.query(Student)
        
        if current_user.role.value == "teacher":
            classrooms = db.query(Classroom.id).filter(Classroom.teacher_id == current_user.id).all()
            classroom_ids = [c[0] for c in classrooms]
            query = query.filter(Student.classroom_id.in_(classroom_ids))
        
        return query.offset(skip).limit(limit).all()

    def get_student(self, db: Session, student_id: int, current_user: User) -> Optional[Student]:
        """Get single student"""
        student = db.query(Student).filter(Student.id == student_id).first()
        
        if not student:
            return None
        
        if current_user.role.value == "teacher":
            classroom = db.query(Classroom).filter(
                Classroom.id == student.classroom_id,
                Classroom.teacher_id == current_user.id
            ).first()
            if not classroom:
                return None
        
        return student

    def create_student(self, db: Session, student_data: StudentCreate, current_user: User) -> Student:
        """Create new student"""
        classroom = db.query(Classroom).filter(Classroom.id == student_data.classroom_id).first()
        
        if not classroom:
            raise ValueError("Classroom not found")
        
        if current_user.role.value == "teacher" and classroom.teacher_id != current_user.id:
            raise ValueError("Access denied")
        
        existing = db.query(Student).filter(Student.roll_number == student_data.roll_number).first()
        if existing:
            raise ValueError("Roll number already exists")
        
        student = Student(**student_data.dict())
        db.add(student)
        db.commit()
        db.refresh(student)
        
        return student

    def update_student(self, db: Session, student_id: int, student_data: StudentUpdate, current_user: User) -> Optional[Student]:
        """Update student"""
        student = self.get_student(db, student_id, current_user)
        
        if not student:
            return None
        
        update_data = student_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(student, key, value)
        
        db.commit()
        db.refresh(student)
        
        return student

    def delete_student(self, db: Session, student_id: int, current_user: User) -> bool:
        """Delete student"""
        student = self.get_student(db, student_id, current_user)
        
        if not student:
            return False
        
        db.delete(student)
        db.commit()
        
        return True

    def search_students(self, db: Session, query: str, current_user: User) -> List[Student]:
        """Search students by name or roll number"""
        students = db.query(Student).filter(
            or_(
                Student.name.ilike(f"%{query}%"),
                Student.roll_number.ilike(f"%{query}%")
            )
        )
        
        if current_user.role.value == "teacher":
            classrooms = db.query(Classroom.id).filter(Classroom.teacher_id == current_user.id).all()
            classroom_ids = [c[0] for c in classrooms]
            students = students.filter(Student.classroom_id.in_(classroom_ids))
        
        return students.all()
