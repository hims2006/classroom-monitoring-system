"""FastAPI Application Entry Point"""

import os
from app.init_db import init_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager

from app.config import get_settings
from app.api import auth, dashboard, students, attendance, alerts, reports, monitoring
from app.middleware.error_handling import ErrorHandlerMiddleware
from app.utils.logger import setup_logger

logger = setup_logger()
settings = get_settings()

os.makedirs(settings.upload_folder, exist_ok=True)
os.makedirs(settings.log_file.rsplit("/", 1)[0], exist_ok=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager"""
    logger.info(f"Starting {settings.app_name} v{settings.app_version}")
    logger.info(f"Environment: {settings.environment}")
    init_db()
    yield
    logger.info(f"Shutting down {settings.app_name}")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Real-time student engagement monitoring system powered by AI",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.allowed_hosts,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(ErrorHandlerMiddleware)


@app.get("/health", tags=["System"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
    }


app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(
    dashboard.router, prefix="/api/dashboard", tags=["Dashboard"]
)
app.include_router(students.router, prefix="/api/students", tags=["Students"])
app.include_router(
    attendance.router, prefix="/api/attendance", tags=["Attendance"]
)
app.include_router(alerts.router, prefix="/api/alerts", tags=["Alerts"])
app.include_router(reports.router, prefix="/api/reports", tags=["Reports"])
app.include_router(
    monitoring.router, prefix="/api/monitoring", tags=["Monitoring"]
)


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "app": settings.app_name,
        "version": settings.app_version,
        "docs": "/docs",
        "redoc": "/redoc",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level=settings.log_level.lower(),
    )
