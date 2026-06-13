from app.utils.db import engine
from app.models.base import Base

# Import models so SQLAlchemy registers them
from app.models.user import User
from app.models.student import Student
from app.models.classroom import Classroom


def init_db():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)