import api from './api'

export const attendanceService = {
  getAttendance: async (skip: number = 0, limit: number = 50, date?: string) => {
    const { data } = await api.get('/api/attendance', { params: { skip, limit, attendance_date: date } })
    return data
  },

  logAttendance: async (attendanceData: any) => {
    const { data } = await api.post('/api/attendance/log', attendanceData)
    return data
  },

  getStudentAttendance: async (studentId: number, limit: number = 30) => {
    const { data } = await api.get(`/api/attendance/student/${studentId}`, { params: { limit } })
    return data
  },

  getAttendanceReport: async (startDate?: string, endDate?: string) => {
    const { data } = await api.get('/api/attendance/report', { params: { start_date: startDate, end_date: endDate } })
    return data
  },
}
