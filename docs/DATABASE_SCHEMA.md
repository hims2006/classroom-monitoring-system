# Database Schema - AI Classroom Monitoring System

## Overview
This document describes the complete database schema for the AI Classroom Monitoring System.

## Tables

### 1. Users Table
Stores admin and teacher accounts.

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('admin', 'teacher') NOT NULL DEFAULT 'teacher',
    full_name VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_role (role)
);
```

### 2. Classrooms Table
Stores classroom information.

```sql
CREATE TABLE classrooms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    teacher_id INT NOT NULL,
    capacity INT DEFAULT 50,
    location VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_teacher (teacher_id)
);
```

### 3. Students Table
Stores student records with face encoding for AI recognition.

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    roll_number VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    classroom_id INT NOT NULL,
    face_encoding LONGBLOB,
    enrollment_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (classroom_id) REFERENCES classrooms(id) ON DELETE CASCADE,
    INDEX idx_roll (roll_number),
    INDEX idx_classroom (classroom_id)
);
```

### 4. Attendance Table
Logs attendance records with automatic AI logging.

```sql
CREATE TABLE attendance (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    classroom_id INT NOT NULL,
    session_id VARCHAR(100),
    attendance_date DATE NOT NULL,
    check_in_time TIMESTAMP,
    check_out_time TIMESTAMP,
    duration_minutes INT,
    status ENUM('present', 'absent', 'late', 'left_early') DEFAULT 'present',
    method ENUM('auto_ai', 'manual') DEFAULT 'auto_ai',
    notes VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (classroom_id) REFERENCES classrooms(id) ON DELETE CASCADE,
    INDEX idx_student (student_id),
    INDEX idx_date (attendance_date),
    UNIQUE KEY unique_attendance (student_id, attendance_date, session_id)
);
```

### 5. Engagement Logs Table
Stores real-time engagement metrics from AI analysis.

```sql
CREATE TABLE engagement_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    classroom_id INT NOT NULL,
    session_id VARCHAR(100),
    timestamp TIMESTAMP,
    engagement_score INT DEFAULT 100,
    alertness_level ENUM('attentive', 'slight_lean', 'drowsy', 'sleeping') DEFAULT 'attentive',
    is_phone_detected BOOLEAN DEFAULT FALSE,
    is_distracted BOOLEAN DEFAULT FALSE,
    movement_status ENUM('seated', 'moving', 'standing') DEFAULT 'seated',
    eye_aspect_ratio FLOAT,
    head_yaw FLOAT,
    head_pitch FLOAT,
    head_roll FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (classroom_id) REFERENCES classrooms(id) ON DELETE CASCADE,
    INDEX idx_student (student_id),
    INDEX idx_session (session_id),
    INDEX idx_timestamp (timestamp)
);
```

### 6. Alerts Table
Stores all generated alerts.

```sql
CREATE TABLE alerts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    classroom_id INT NOT NULL,
    session_id VARCHAR(100),
    alert_type ENUM(
        'phone_detected',
        'sleeping',
        'drowsy',
        'suspicious_interaction',
        'left_seat',
        'highly_distracted'
    ) NOT NULL,
    severity ENUM('low', 'medium', 'high', 'critical') DEFAULT 'medium',
    description VARCHAR(500),
    is_acknowledged BOOLEAN DEFAULT FALSE,
    acknowledged_by INT,
    acknowledged_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE SET NULL,
    FOREIGN KEY (classroom_id) REFERENCES classrooms(id) ON DELETE CASCADE,
    FOREIGN KEY (acknowledged_by) REFERENCES users(id) ON DELETE SET NULL,
    INDEX idx_type (alert_type),
    INDEX idx_severity (severity),
    INDEX idx_created (created_at)
);
```

### 7. Sessions Table
Tracks monitoring/recording sessions.

```sql
CREATE TABLE sessions (
    id VARCHAR(100) PRIMARY KEY,
    classroom_id INT NOT NULL,
    teacher_id INT NOT NULL,
    session_name VARCHAR(255),
    start_time TIMESTAMP,
    end_time TIMESTAMP NULL,
    is_active BOOLEAN DEFAULT TRUE,
    total_students INT DEFAULT 0,
    class_engagement FLOAT DEFAULT 0.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (classroom_id) REFERENCES classrooms(id) ON DELETE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_classroom (classroom_id),
    INDEX idx_active (is_active)
);
```

### 8. Reports Table
Stores generated reports.

```sql
CREATE TABLE reports (
    id INT PRIMARY KEY AUTO_INCREMENT,
    classroom_id INT NOT NULL,
    teacher_id INT NOT NULL,
    report_type ENUM('daily', 'weekly', 'monthly', 'custom') NOT NULL,
    report_date DATE,
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    total_students INT,
    avg_engagement FLOAT,
    alert_count INT,
    phone_alerts INT,
    drowsy_alerts INT,
    suspicious_count INT,
    file_path VARCHAR(500),
    export_format ENUM('pdf', 'excel', 'csv') DEFAULT 'pdf',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (classroom_id) REFERENCES classrooms(id) ON DELETE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_teacher (teacher_id),
    INDEX idx_date (report_date)
);
```

### 9. Audit Log Table
Tracks all system changes for security and compliance.

```sql
CREATE TABLE audit_log (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    action VARCHAR(100),
    entity_type VARCHAR(50),
    entity_id INT,
    old_values JSON,
    new_values JSON,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
    INDEX idx_user (user_id),
    INDEX idx_action (action),
    INDEX idx_timestamp (created_at)
);
```

## Views

### Daily Summary View
```sql
CREATE VIEW vw_daily_summary AS
SELECT 
    a.attendance_date AS date,
    c.id AS classroom_id,
    c.name AS classroom_name,
    COUNT(DISTINCT a.student_id) AS students_present,
    COUNT(CASE WHEN a.status = 'late' THEN 1 END) AS late_count,
    COUNT(CASE WHEN a.status = 'absent' THEN 1 END) AS absent_count,
    AVG(el.engagement_score) AS avg_engagement,
    SUM(CASE WHEN al.alert_type = 'phone_detected' THEN 1 ELSE 0 END) AS phone_alerts,
    SUM(CASE WHEN al.alert_type = 'sleeping' THEN 1 ELSE 0 END) AS sleep_alerts
FROM attendance a
JOIN classrooms c ON a.classroom_id = c.id
LEFT JOIN engagement_logs el ON a.student_id = el.student_id 
    AND DATE(el.timestamp) = a.attendance_date
LEFT JOIN alerts al ON a.student_id = al.student_id 
    AND DATE(al.created_at) = a.attendance_date
GROUP BY a.attendance_date, c.id;
```

## Indexes

Key indexes for performance optimization:
- `users`: email, role
- `classrooms`: teacher_id
- `students`: roll_number, classroom_id
- `attendance`: student_id, attendance_date
- `engagement_logs`: student_id, session_id, timestamp
- `alerts`: alert_type, severity, created_at
- `sessions`: classroom_id, is_active
- `reports`: teacher_id, report_date

## Relationships

```
users (1) ---> (N) classrooms
users (1) ---> (N) sessions
users (1) ---> (N) reports
users (1) ---> (N) audit_log

classrooms (1) ---> (N) students
classrooms (1) ---> (N) attendance
classrooms (1) ---> (N) engagement_logs
classrooms (1) ---> (N) alerts
classrooms (1) ---> (N) sessions
classrooms (1) ---> (N) reports

students (1) ---> (N) attendance
students (1) ---> (N) engagement_logs
students (1) ---> (N) alerts

sessions (1) ---> (N) attendance
sessions (1) ---> (N) engagement_logs
sessions (1) ---> (N) alerts
```
