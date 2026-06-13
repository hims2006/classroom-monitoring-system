"""Authentication Endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import (
    UserRegister,
    UserLogin,
    UserResponse,
    TokenResponse,
)
from app.services.auth_service import AuthService
from app.utils.db import get_db
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter()
auth_service = AuthService()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserRegister, db: Session = Depends(get_db)):
    """Register a new user (Admin/Teacher)"""
    try:
        user = auth_service.register_user(db, user_data)
        return UserResponse.from_orm(user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/login", response_model=TokenResponse)
async def login(credentials: UserLogin, db: Session = Depends(get_db)):
    """Login user and return JWT token"""
    user = auth_service.authenticate_user(db, credentials.email, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    token = auth_service.create_access_token(user)
    return TokenResponse(access_token=token, token_type="bearer", user=UserResponse.from_orm(user))


@router.post("/logout")
async def logout(current_user: User = Depends(get_current_user)):
    """Logout user (invalidate token)"""
    return {"message": "Logged out successfully"}


@router.post("/refresh-token", response_model=TokenResponse)
async def refresh_token(current_user: User = Depends(get_current_user)):
    """Refresh JWT token"""
    token = auth_service.create_access_token(current_user)
    return TokenResponse(access_token=token, token_type="bearer", user=UserResponse.from_orm(current_user))


@router.get("/verify", response_model=UserResponse)
async def verify_token(current_user: User = Depends(get_current_user)):
    """Verify token and return current user"""
    return UserResponse.from_orm(current_user)


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """Get current user profile"""
    return UserResponse.from_orm(current_user)
