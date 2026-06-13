# API Documentation - AI Classroom Monitoring System

## Base URL
```
http://localhost:8000/api
```

## Authentication
All protected endpoints require a Bearer token in the `Authorization` header:
```
Authorization: Bearer {token}
```

## Endpoints

### Authentication

#### Register User
```
POST /auth/register
Content-Type: application/json

{
  "username": "teacher1",
  "email": "teacher@college.edu",
  "password": "SecurePass123!",
  "full_name": "John Teacher",
  "role": "teacher"
}

Response: 201 Created
{
  "id": 1,
  "username": "teacher1",
  "email": "teacher@college.edu",
  "full_name": "John Teacher",
  "role": "teacher",
  "is_active": true,
  "created_at": "2026-06-12T10:00:00Z",
  "updated_at": "2026-06-12T10:00:00Z"
}
```

#### Login
```
POST /auth/login
Content-Type: application/json

{
  "email": "teacher@college.edu",
  "password": "SecurePass123!"
}

Response: 200 OK
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": { ... }
}
```

#### Verify Token
```
GET /auth/verify
Authorization: Bearer {token}

Response: 200 OK
{
  "id": 1,
  "username": "teacher1",
  "email": "teacher@college.edu",
  "full_name": "John Teacher",
  "role": "teacher",
  "is_active": true,
  "created_at": "2026-06-12T10:00:00Z",
  "updated_at": "2026-06-12T10:00:00Z"
}
```

### Dashboard

#### Get Summary
```
GET /dashboard/summary
Authorization: Bearer {token}

Response: 200 OK
{
  "total_students": 42,
  "engagement_percentage": 85,
  "alerts_count": 3,
  "phones_detected": 1,
  "drowsy_count": 2
}
```

#### Get Class Engagement
```
GET /dashboard/engagement
Authorization: Bearer {token}

Response: 200 OK
{
  "engagement": 85.5,
  "timestamp": "2026-06-12T17:30:00Z"
}
```

### Students

#### List Students
```
GET /students?skip=0&limit=50
Authorization: Bearer {token}

Response: 200 OK
[
  {
    "id": 1,
    "roll_number": "CS001",
    "name": "Alice Kumar",
    "email": "alice@college.edu",
    "classroom_id": 1,
    "enrollment_date": "2026-01-10",
    "is_active": true,
    "created_at": "2026-01-10T00:00:00Z",
    "updated_at": "2026-01-10T00:00:00Z"
  }
]
```

#### Create Student
```
POST /students
Authorization: Bearer {token}
Content-Type: application/json

{
  "roll_number": "CS001",
  "name": "Alice Kumar",
  "email": "alice@college.edu",
  "classroom_id": 1,
  "enrollment_date": "2026-01-10"
}

Response: 201 Created
{
  "id": 1,
  "roll_number": "CS001",
  "name": "Alice Kumar",
  "email": "alice@college.edu",
  "classroom_id": 1,
  "enrollment_date": "2026-01-10",
  "is_active": true,
  "created_at": "2026-06-12T17:30:00Z",
  "updated_at": "2026-06-12T17:30:00Z"
}
```

#### Get Student
```
GET /students/{id}
Authorization: Bearer {token}

Response: 200 OK
{ ... student details ... }
```

#### Update Student
```
PUT /students/{id}
Authorization: Bearer {token}
Content-Type: application/json

{
  "name": "Alice Kumar Updated",
  "email": "alice.new@college.edu"
}

Response: 200 OK
{ ... updated student ... }
```

#### Delete Student
```
DELETE /students/{id}
Authorization: Bearer {token}

Response: 204 No Content
```

#### Search Students
```
GET /students/search/alice
Authorization: Bearer {token}

Response: 200 OK
{
  "results": [ ... ],
  "count": 1
}
```

### Attendance

#### Get Attendance Records
```
GET /attendance?skip=0&limit=50&attendance_date=2026-06-12
Authorization: Bearer {token}

Response: 200 OK
[
  {
    "id": 1,
    "student_id": 1,
    "classroom_id": 1,
    "session_id": "session-001",
    "attendance_date": "2026-06-12",
    "check_in_time": "2026-06-12T09:00:00Z",
    "check_out_time": "2026-06-12T17:00:00Z",
    "duration_minutes": 480,
    "status": "present",
    "method": "auto_ai",
    "notes": null,
    "created_at": "2026-06-12T09:00:00Z"
  }
]
```

#### Log Attendance
```
POST /attendance/log
Authorization: Bearer {token}
Content-Type: application/json

{
  "student_id": 1,
  "classroom_id": 1,
  "session_id": "session-001",
  "attendance_date": "2026-06-12",
  "status": "present",
  "method": "auto_ai",
  "notes": "Automatic detection via face recognition"
}

Response: 201 Created
{ ... attendance record ... }
```

#### Get Attendance Report
```
GET /attendance/report?start_date=2026-06-01&end_date=2026-06-12
Authorization: Bearer {token}

Response: 200 OK
{
  "period_start": "2026-06-01",
  "period_end": "2026-06-12",
  "total_days": 10,
  "present_count": 420,
  "absent_count": 10,
  "late_count": 5,
  "attendance_rate": 95.5
}
```

### Alerts

#### List Alerts
```
GET /alerts?skip=0&limit=50&unread_only=false&alert_type=phone_detected&severity=high
Authorization: Bearer {token}

Response: 200 OK
[
  {
    "id": 1,
    "student_id": 5,
    "classroom_id": 1,
    "session_id": "session-001",
    "alert_type": "phone_detected",
    "severity": "high",
    "description": "Mobile phone detected in student's hand",
    "is_acknowledged": false,
    "acknowledged_by": null,
    "acknowledged_at": null,
    "created_at": "2026-06-12T14:32:00Z"
  }
]
```

#### Acknowledge Alert
```
PUT /alerts/{id}/acknowledge
Authorization: Bearer {token}

Response: 200 OK
{
  "message": "Alert acknowledged",
  "alert_id": 1
}
```

#### Delete Alert
```
DELETE /alerts/{id}
Authorization: Bearer {token}

Response: 204 No Content
```

### Reports

#### Generate Report
```
POST /reports/generate
Authorization: Bearer {token}
Content-Type: application/json

{
  "classroom_id": 1,
  "report_type": "daily",
  "period_start": "2026-06-12",
  "period_end": "2026-06-12"
}

Response: 201 Created
{
  "id": 1,
  "classroom_id": 1,
  "teacher_id": 1,
  "report_type": "daily",
  "report_date": "2026-06-12",
  "period_start": "2026-06-12",
  "period_end": "2026-06-12",
  "total_students": 42,
  "avg_engagement": 85.5,
  "alert_count": 3,
  "phone_alerts": 1,
  "drowsy_alerts": 2,
  "suspicious_count": 0,
  "file_path": "/reports/report_2026-06-12.pdf",
  "export_format": "pdf",
  "created_at": "2026-06-12T17:30:00Z"
}
```

#### List Reports
```
GET /reports?skip=0&limit=50&report_type=daily
Authorization: Bearer {token}

Response: 200 OK
[ ... list of reports ... ]
```

#### Export Report
```
POST /reports/{id}/export?format=pdf
Authorization: Bearer {token}

Response: 200 OK
{
  "file_path": "/reports/report_2026-06-12.pdf",
  "format": "pdf"
}
```

### Real-time (WebSocket)

#### Live Feed
```
WS /ws/live-feed

Message format:
{"type": "start"}  -> Start streaming
{"type": "stop"}   -> Stop streaming
{"type": "frame", "data": "base64_encoded_image"}
```

#### Alerts Stream
```
WS /ws/alerts

Broadcast format:
{
  "type": "phone_detected",
  "student_id": 5,
  "severity": "high",
  "timestamp": "2026-06-12T14:32:00Z"
}
```

#### Metrics Stream
```
WS /ws/metrics

Broadcast format:
{
  "type": "metrics_update",
  "students_detected": 42,
  "engagement": 85.5,
  "active_alerts": 3,
  "timestamp": "2026-06-12T14:32:00Z"
}
```

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Invalid input data"
}
```

### 401 Unauthorized
```json
{
  "detail": "Token expired" or "Invalid token"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

## Rate Limiting

API endpoints are rate-limited to prevent abuse:
- 100 requests per minute for authenticated users
- 10 requests per minute for public endpoints

## Pagination

List endpoints support pagination:
- `skip` (default: 0) - Number of records to skip
- `limit` (default: 50, max: 100) - Number of records to return

## Filtering

List endpoints support filtering:
- `alert_type` - Filter alerts by type
- `severity` - Filter alerts by severity
- `report_type` - Filter reports by type
- `attendance_date` - Filter attendance by date

## Sorting

Results are sorted by most recent first (created_at DESC) by default.
