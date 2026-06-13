# AI Classroom Monitoring System - Complete Setup

## 🎯 Quick Links

- [API Documentation](./docs/API_DOCUMENTATION.md)
- [Database Schema](./docs/DATABASE_SCHEMA.md)
- [Setup Guide](./docs/SETUP_GUIDE.md)
- [Architecture Guide](./docs/ARCHITECTURE.md)

## 📋 Project Status

✅ **Complete Backend** - 42 files
✅ **Complete Frontend** - 43 files  
✅ **Docker Setup** - Production ready
✅ **Database Schema** - Fully documented
✅ **API Documentation** - Complete with examples

## 🚀 Getting Started

### Option 1: Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/hims2006/classroom-monitoring-system.git
cd classroom-monitoring-system

# Create environment files
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local

# Start all services
docker-compose up -d

# Access application
Frontend: http://localhost:3000
Backend API: http://localhost:8000
API Docs: http://localhost:8000/docs
```

### Option 2: Manual Setup

See [SETUP_GUIDE.md](./docs/SETUP_GUIDE.md) for detailed instructions.

## 🔑 Default Credentials

**Admin Account:**
- Email: `admin@classroom.local`
- Password: `Admin@123`

**Teacher Account:**
- Email: `teacher@classroom.local`
- Password: `Teacher@123`

⚠️ **Change these in production!**

## 📁 Project Structure

```
classroom-monitoring-system/
├── backend/
│   ├── app/
│   │   ├── api/              # API endpoints
│   │   ├── services/         # Business logic
│   │   ├── models/           # Database models
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── middleware/       # Custom middleware
│   │   ├── utils/            # Helper functions
│   │   ├── websocket/        # WebSocket handlers
│   │   └── ai_engine/        # AI/ML models
│   ├── requirements.txt      # Python dependencies
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── pages/            # Page components
│   │   ├── services/         # API services
│   │   ├── store/            # Redux store
│   │   ├── hooks/            # Custom hooks
│   │   └── styles/           # CSS files
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   ├── Dockerfile
│   └── .env.example
├── docs/
│   ├── API_DOCUMENTATION.md
│   ├── DATABASE_SCHEMA.md
│   ├── SETUP_GUIDE.md
│   └── ARCHITECTURE.md
├── docker-compose.yml
└── README.md
```

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.10+
- **Database**: MySQL 8.0
- **Cache**: Redis 7.0
- **Authentication**: JWT
- **ORM**: SQLAlchemy

### AI Engine
- **OpenCV**: Computer vision
- **MediaPipe**: Face detection & pose estimation
- **YOLOv8**: Object detection (phones)
- **NumPy/Pandas**: Data processing

### Frontend
- **Framework**: React 18
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State**: Redux Toolkit
- **HTTP**: Axios
- **Real-time**: WebSocket
- **Charts**: Chart.js

## 📊 Core Features

### AI Capabilities
✅ Multi-student face detection (up to 50+)
✅ Real-time engagement scoring
✅ Drowsiness detection
✅ Phone usage detection
✅ Head pose estimation
✅ Suspicious interaction detection
✅ Automatic attendance logging
✅ Movement tracking

### Web Application
✅ Interactive dashboard with KPIs
✅ Live video monitoring
✅ Student management (CRUD)
✅ Attendance tracking
✅ Real-time alerts system
✅ Analytics & reports (PDF/Excel/CSV)
✅ Role-based access (Admin/Teacher)
✅ Dark theme UI
✅ WebSocket real-time updates

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/register` - Register user
- `POST /api/auth/login` - Login
- `GET /api/auth/me` - Get current user
- `POST /api/auth/refresh-token` - Refresh JWT

### Dashboard
- `GET /api/dashboard/summary` - KPI overview
- `GET /api/dashboard/engagement` - Real-time engagement
- `GET /api/dashboard/alerts` - Recent alerts
- `GET /api/dashboard/trends` - Historical trends

### Students
- `GET /api/students` - List students
- `POST /api/students` - Create student
- `GET /api/students/{id}` - Get details
- `PUT /api/students/{id}` - Update student
- `DELETE /api/students/{id}` - Delete student

### Attendance
- `GET /api/attendance` - List attendance
- `POST /api/attendance/log` - Log attendance
- `GET /api/attendance/report` - Attendance report

### Alerts
- `GET /api/alerts` - List alerts
- `PUT /api/alerts/{id}/acknowledge` - Mark as read
- `DELETE /api/alerts/{id}` - Delete alert

### Reports
- `POST /api/reports/generate` - Generate report
- `GET /api/reports` - List reports
- `POST /api/reports/{id}/export` - Export (PDF/Excel/CSV)

### Real-time (WebSocket)
- `WS /ws/live-feed` - Video stream
- `WS /ws/alerts` - Alert notifications
- `WS /ws/metrics` - Metrics updates

## 📖 Documentation

### Setup
See [SETUP_GUIDE.md](./docs/SETUP_GUIDE.md) for:
- Prerequisites
- Docker setup
- Manual installation
- Environment configuration
- Database initialization
- Testing

### API
See [API_DOCUMENTATION.md](./docs/API_DOCUMENTATION.md) for:
- Complete endpoint reference
- Request/response examples
- Authentication
- Error handling
- Rate limiting
- WebSocket details

### Database
See [DATABASE_SCHEMA.md](./docs/DATABASE_SCHEMA.md) for:
- Table definitions
- Relationships
- Indexes
- Views
- Sample queries

### Architecture
See [ARCHITECTURE.md](./docs/ARCHITECTURE.md) for:
- System overview
- Component descriptions
- Data flow
- Security design
- Scalability considerations

## 🐳 Docker Deployment

### Services
- **MySQL**: `localhost:3306`
- **Redis**: `localhost:6379`
- **Backend API**: `localhost:8000`
- **Frontend**: `localhost:3000`
- **Nginx (optional)**: `localhost:80`

### Commands

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f backend

# Stop services
docker-compose down

# Rebuild images
docker-compose build --no-cache

# Database access
docker-compose exec mysql mysql -u root -p

# Backend shell
docker-compose exec backend bash
```

## 🧪 Testing

### Backend
```bash
cd backend
pytest tests/ -v
pytest tests/ --cov=app
```

### Frontend
```bash
cd frontend
npm test
npm test -- --coverage
```

## 📦 Deployment

### Production Checklist
- [ ] Change default credentials
- [ ] Set strong JWT_SECRET_KEY
- [ ] Enable HTTPS/WSS
- [ ] Configure CORS properly
- [ ] Setup database backups
- [ ] Enable rate limiting
- [ ] Configure monitoring
- [ ] Setup error tracking
- [ ] Enable audit logging
- [ ] Configure CDN for frontend

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

MIT License - See LICENSE file for details

## 📧 Support

For issues and support:
- Open an issue on GitHub
- Check documentation in `/docs`
- Review API docs at `http://localhost:8000/docs`

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [MediaPipe Documentation](https://developers.google.com/mediapipe)
- [YOLOv8 Documentation](https://docs.ultralytics.com/)

---

**Made with ❤️ for educators and institutions**

Version 1.0.0 | Last Updated: 2026-06-12
