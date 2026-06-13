"""Authentication Service"""

from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Optional
import jwt

from app.config import get_settings
from app.models.user import User
from app.schemas.user import UserRegister
from app.utils.security import hash_password, verify_password

settings = get_settings()


class AuthService:
    """Authentication service"""

    def register_user(self, db: Session, user_data: UserRegister) -> User:
        """Register a new user"""
        existing = db.query(User).filter(
            (User.email == user_data.email) | (User.username == user_data.username)
        ).first()
        
        if existing:
            raise ValueError("User already exists")
        
        user = User(
            username=user_data.username,
            email=user_data.email,
            password_hash=hash_password(user_data.password),
            full_name=user_data.full_name,
            role=user_data.role,
        )
        
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return user

    def authenticate_user(self, db: Session, email: str, password: str) -> Optional[User]:
        """Authenticate user with email and password"""
        user = db.query(User).filter(User.email == email).first()
        
        if not user or not verify_password(password, user.password_hash):
            return None
        
        if not user.is_active:
            return None
        
        return user

    def create_access_token(self, user: User) -> str:
        """Create JWT access token"""
        payload = {
            "sub": str(user.id),
            "email": user.email,
            "username": user.username,
            "role": user.role.value,
            "exp": datetime.utcnow() + timedelta(hours=settings.jwt_expiration_hours),
            "iat": datetime.utcnow(),
        }
        
        token = jwt.encode(
            payload,
            settings.jwt_secret_key,
            algorithm=settings.jwt_algorithm,
        )
        
        return token

    def verify_token(self, token: str) -> Optional[dict]:
        """Verify and decode JWT token"""
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret_key,
                algorithms=[settings.jwt_algorithm],
            )
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
