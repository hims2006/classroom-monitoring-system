# Setup Guide - AI Classroom Monitoring System

## Prerequisites

- Python 3.10+
- Node.js 18+
- MySQL 8.0+
- Redis 7.0+
- Docker & Docker Compose (optional)
- Git

## Quick Start with Docker

The easiest way to get started is using Docker Compose:

```bash
# Clone the repository
git clone https://github.com/hims2006/classroom-monitoring-system.git
cd classroom-monitoring-system

# Create environment file
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local

# Start all services
docker-compose up -d

# Access the application
Frontend: http://localhost:3000
Backend: http://localhost:8000
API Docs: http://localhost:8000/docs
```

## Manual Setup

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env

# Edit .env with your configuration
# - DATABASE_URL
# - JWT_SECRET_KEY
# - REDIS_URL

# Run database migrations (if using Alembic)
alembic upgrade head

# Start the server
uvicorn app.main:app --reload

# Server will be available at http://localhost:8000
```

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Setup environment variables
cp .env.example .env.local

# Edit .env.local if needed
# VITE_API_URL=http://localhost:8000
# VITE_WS_URL=ws://localhost:8000

# Start development server
npm run dev

# Application will be available at http://localhost:3000
```

### 3. Database Setup

```bash
# Create MySQL database
mysql -u root -p

CREATE DATABASE classroom_monitoring CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'classroom_user'@'localhost' IDENTIFIED BY 'classroom_password';
GRANT ALL PRIVILEGES ON classroom_monitoring.* TO 'classroom_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# Run initial SQL schema (if needed)
mysql -u classroom_user -p classroom_monitoring < docs/DATABASE_SCHEMA.md
```

### 4. Redis Setup

```bash
# Start Redis server
redis-server

# Or using Docker
docker run -d -p 6379:6379 redis:7-alpine
```

## Environment Configuration

### Backend (.env)

```env
# Database
DATABASE_URL=mysql+pymysql://classroom_user:classroom_password@localhost:3306/classroom_monitoring
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USER=classroom_user
DATABASE_PASSWORD=classroom_password
DATABASE_NAME=classroom_monitoring

# Redis
REDIS_URL=redis://localhost:6379/0
REDIS_HOST=localhost
REDIS_PORT=6379

# JWT
JWT_SECRET_KEY=your-super-secret-key-change-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# Application
APP_NAME=AI Classroom Monitoring System
APP_VERSION=1.0.0
DEBUG=False
ENVIRONMENT=production

# AI Engine
AI_MODEL_PHONE=yolov8n.pt
AI_CONFIDENCE_THRESHOLD=0.45
AI_MAX_FACES=10
AI_FRAME_RATE=30

# Logging
LOG_LEVEL=INFO
LOG_FILE=./logs/app.log
```

### Frontend (.env.local)

```env
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000
VITE_APP_NAME=AI Classroom Monitoring
VITE_APP_VERSION=1.0.0
```

## Default Credentials

For testing purposes, the system comes with default credentials:

**Admin Account:**
- Email: `admin@classroom.local`
- Password: `Admin@123`

**Teacher Account:**
- Email: `teacher@classroom.local`
- Password: `Teacher@123`

⚠️ **IMPORTANT: Change these credentials in production!**

## Verifying Installation

### 1. Check Backend

```bash
curl http://localhost:8000/health

# Expected response:
# {"status": "healthy", "app": "AI Classroom Monitoring System", ...}
```

### 2. Check API Documentation

Visit `http://localhost:8000/docs` to access the interactive API documentation.

### 3. Check Frontend

Visit `http://localhost:3000` to access the web application.

## Running Tests

### Backend Tests

```bash
cd backend
pytest tests/ -v

# With coverage
pytest tests/ --cov=app --cov-report=html
```

### Frontend Tests

```bash
cd frontend
npm test

# With coverage
npm test -- --coverage
```

## Production Deployment

### Using Docker Compose

```bash
# Build images
docker-compose build

# Start production containers
docker-compose -f docker-compose.yml up -d

# Check logs
docker-compose logs -f
```

### Manual Deployment

1. **Backend**: Deploy using Gunicorn/Nginx
2. **Frontend**: Build and deploy to Nginx/Apache
3. **Database**: Use managed MySQL service
4. **Cache**: Use managed Redis service

See `docs/DEPLOYMENT.md` for detailed production setup.

## Troubleshooting

### Common Issues

**Connection refused error:**
- Ensure MySQL and Redis are running
- Check DATABASE_URL and REDIS_URL in .env

**Import errors:**
- Install all dependencies: `pip install -r requirements.txt`
- Ensure virtual environment is activated

**CORS errors:**
- Check CORS_ORIGINS in config.py
- Ensure frontend URL is in allowed origins

**WebSocket connection failed:**
- Check WS_URL in frontend .env
- Ensure backend is running with WebSocket support

## Support

For issues and support:
- Check documentation in `/docs`
- Review API docs at `http://localhost:8000/docs`
- Open an issue on GitHub

