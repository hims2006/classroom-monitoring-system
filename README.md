# 🎓 AI Classroom Monitoring System

**Real-time student engagement monitoring powered by AI**

A production-ready web application that uses computer vision and machine learning to monitor student engagement, detect drowsiness, identify phone usage, and track attendance in real-time.

## 🌟 Features

### Core AI Capabilities
- ✅ **Multi-student Detection** - Real-time face detection for up to 50+ students
- ✅ **Engagement Scoring** - Automatic engagement percentage calculation
- ✅ **Drowsiness Detection** - Alert when students show signs of sleepiness
- ✅ **Phone Detection** - YOLOv8-based phone detection and usage tracking
- ✅ **Head Pose Estimation** - Detects if students are looking away or sleeping
- ✅ **Suspicious Interaction Detection** - Identifies proximity-based cheating attempts
- ✅ **Automatic Attendance** - AI-powered attendance logging
- ✅ **Movement Tracking** - Detects if students are standing or moving

### Web Application Features
- 📊 **Interactive Dashboard** - Real-time KPIs and metrics
- 📹 **Live Monitoring** - Live video feed with real-time student status
- 👥 **Student Management** - CRUD operations for student records
- 📋 **Attendance Tracking** - Automatic and manual attendance logging
- 🚨 **Alert System** - Real-time notifications for critical events
- 📈 **Analytics & Reports** - Daily, weekly, monthly reports with exports
- 🔐 **Role-based Access** - Admin and Teacher roles with separate permissions
- 🌙 **Dark Theme UI** - Modern, professional dark-mode interface

## 🏗️ Tech Stack

### Backend
- **FastAPI** - Modern async Python web framework
- **Python 3.10+** - Core language
- **SQLAlchemy** - ORM for database operations
- **MySQL** - Relational database
- **Redis** - Caching and real-time data
- **WebSocket** - Real-time communication

### AI Engine
- **OpenCV** - Computer vision
- **MediaPipe** - Face detection and pose estimation
- **YOLOv8** - Object detection (phone detection)
- **NumPy/Pandas** - Data processing

### Frontend
- **React 18** - UI framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Redux Toolkit** - State management
- **Chart.js** - Data visualization
- **Axios** - HTTP client

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- MySQL 8.0+
- Docker & Docker Compose (optional)

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env

uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env.local

npm run dev
```

Access at `http://localhost:3000`

## 📖 Documentation

See `/docs` directory for detailed guides.

## 🔐 Default Credentials

- **Admin**: `admin@classroom.local` / `Admin@123`
- **Teacher**: `teacher@classroom.local` / `Teacher@123`

## 📝 License

MIT License
