# Architecture Guide - AI Classroom Monitoring System

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                       Frontend (React)                          │
│  Browser-based UI with real-time WebSocket updates             │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP/WebSocket
┌────────────────────────────▼────────────────────────────────────┐
│                    API Gateway (FastAPI)                        │
│  REST endpoints + WebSocket endpoints                          │
└────────────────────────────┬────────────────────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼────────┐  ┌────────▼────────┐  ┌───────▼────────┐
│  Services      │  │  AI Engine      │  │  Cache Layer   │
│  (Business     │  │  (Python + CV)  │  │  (Redis)       │
│   Logic)       │  │                 │  │                │
└────────┬────────┘  └────────┬────────┘  └───────┬────────┘
         │                    │                    │
         └────────────────────┼────────────────────┘
                              │
                    ┌─────────▼──────────┐
                    │   MySQL Database   │
                    │                    │
                    │ - Users            │
                    │ - Students         │
                    │ - Attendance       │
                    │ - Alerts           │
                    │ - Reports          │
                    └────────────────────┘
```

## Core Components

### 1. Frontend (React + Tailwind)

**Location:** `/frontend`

**Key Features:**
- Real-time dashboard with live metrics
- Live video monitoring with AI overlays
- Student management interface
- Attendance tracking UI
- Alert notifications system
- Reports and analytics
- Dark theme UI

**Technologies:**
- React 18 for UI framework
- Redux Toolkit for state management
- Tailwind CSS for styling
- Chart.js for data visualization
- Axios for HTTP client
- WebSocket for real-time updates

### 2. Backend API (FastAPI)

**Location:** `/backend/app`

**Architecture:**
```
app/
├── api/                    # API endpoints
│   ├── auth.py            # Authentication routes
│   ├── dashboard.py       # Dashboard metrics
│   ├── students.py        # Student CRUD
│   ├── attendance.py      # Attendance logging
│   ├── alerts.py          # Alert management
│   ├── reports.py         # Report generation
│   └── monitoring.py      # WebSocket endpoints
├── services/              # Business logic layer
│   ├── auth_service.py
│   ├── student_service.py
│   ├── attendance_service.py
│   ├── alert_service.py
│   ├── analytics_service.py
│   └── report_service.py
├── models/                # SQLAlchemy models
│   ├── user.py
│   ├── student.py
│   ├── classroom.py
│   ├── attendance.py
│   ├── engagement_log.py
│   ├── alert.py
│   ├── session.py
│   └── report.py
├── schemas/               # Pydantic schemas
│   ├── user.py
│   ├── student.py
│   ├── attendance.py
│   ├── alert.py
│   └── report.py
├── middleware/            # Custom middleware
│   ├── auth.py
│   ├── logging.py
│   └── error_handling.py
├── utils/                 # Utility functions
│   ├── db.py             # Database connection
│   ├── security.py       # JWT & password handling
│   ├── validators.py     # Input validation
│   ├── logger.py         # Logging setup
│   └── constants.py      # App constants
├── websocket/             # WebSocket handlers
│   ├── connection_manager.py
│   └── frame_streamer.py
└── ai_engine/             # AI module (ML models)
    ├── frame_processor.py
    ├── face_detector.py
    ├── pose_estimator.py
    ├── phone_detector.py
    ├── classifiers.py
    └── alert_trigger.py
```

**Request Flow:**
```
Request → Middleware (Auth, Logging) → Route Handler → Service Layer → Database
                    ↓
          Response → Client
```

### 3. AI Engine (OpenCV + MediaPipe + YOLOv8)

**Location:** `/backend/ai_engine`

**Components:**

1. **Frame Processor**
   - Captures video frames from camera
   - Queues frames for processing
   - Manages frame buffer

2. **Face Detection** (MediaPipe)
   - Detects faces in frame
   - Extracts face landmarks
   - Calculates face encoding

3. **Pose Estimation**
   - Estimates head pose (yaw, pitch, roll)
   - Calculates eye aspect ratio
   - Determines alertness level

4. **Phone Detection** (YOLOv8)
   - Detects mobile phones in frame
   - Calculates confidence score
   - Generates phone detection alerts

5. **Classifiers**
   - Drowsiness detection
   - Engagement scoring
   - Distraction detection
   - Suspicious interaction detection

6. **Alert Trigger**
   - Generates alerts based on classifications
   - Sets severity levels
   - Sends to alert service

### 4. Database (MySQL)

**Schema:**
- 9 main tables
- 2 database views
- Indexes for performance
- Foreign key relationships

**Key Tables:**
- `users`: Teacher/admin accounts
- `students`: Student records with face encodings
- `classrooms`: Classroom information
- `attendance`: Attendance logs
- `engagement_logs`: AI engagement metrics
- `alerts`: Generated alerts
- `sessions`: Monitoring sessions
- `reports`: Generated reports

### 5. Cache Layer (Redis)

**Usage:**
- Session storage
- Real-time alert caching
- WebSocket connection tracking
- Rate limiting
- Temporary metrics cache

## Data Flow

### Real-time Monitoring Flow

```
Camera Input
    ↓
Frame Processor
    ↓
Face Detection (MediaPipe)
    ↓
Pose Estimation (Head Pose)
    ↓
Phone Detection (YOLOv8)
    ↓
Classification Engine
├─ Drowsiness Detection
├─ Engagement Scoring
├─ Distraction Detection
└─ Interaction Detection
    ↓
Alert Trigger
    ↓
Alert Service → Database & Redis
    ↓
WebSocket Broadcast
    ↓
Frontend Real-time Update
```

### Attendance Logging Flow

```
Student Detected
    ↓
Face Encoding Extracted
    ↓
Match Against Known Faces
    ↓
Student Identified
    ↓
Attendance Service
    ↓
Log to Database
    ↓
Update Dashboard
```

## Security Architecture

### Authentication
- JWT-based stateless authentication
- 24-hour token expiration
- Token refresh mechanism
- Secure password hashing (bcrypt)

### Authorization
- Role-based access control (RBAC)
- Teacher can only access own classrooms
- Admin has full access
- Endpoint-level protection

### Data Protection
- HTTPS/WSS for data in transit
- Password hashing for data at rest
- SQL injection prevention (parameterized queries)
- CORS policy enforcement

### Audit Trail
- All user actions logged
- Change tracking (old vs new values)
- IP address tracking
- Timestamp on all records

## Scalability Considerations

### Horizontal Scaling
- Stateless API servers
- Redis for distributed caching
- Database replication capable
- Load balancer ready (Nginx)

### Performance Optimization
- Database indexing strategy
- Query optimization
- Caching layer
- WebSocket connection pooling
- Frame buffer management

### Monitoring
- Application logging
- Error tracking
- Performance metrics
- Database query logs

## Deployment Architecture

### Docker Deployment
```
Docker Host
├── MySQL Container
├── Redis Container
├── FastAPI Backend Container
├── React Frontend Container (via Nginx)
└── Nginx Reverse Proxy
```

### Production Considerations
- Use managed databases (AWS RDS, Azure MySQL)
- Use managed cache (Redis Cloud)
- CDN for static frontend assets
- SSL/TLS certificates
- Rate limiting
- DDoS protection
- Backup strategy

## Extension Points

1. **AI Models**: Replace MediaPipe/YOLOv8 with custom models
2. **Authentication**: Add OAuth2, SAML, SSO
3. **Notifications**: Add email, SMS, push notifications
4. **Storage**: Add cloud storage for reports/images
5. **Analytics**: Add advanced analytics engine
6. **Mobile**: Add mobile app via React Native

