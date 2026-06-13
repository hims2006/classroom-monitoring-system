import { useState } from 'react'

interface AttendanceRecord {
  id: number
  student_name: string
  roll_number: string
  status: 'present' | 'absent' | 'late'
  check_in: string
  check_out: string
}

export default function Attendance() {
  const [records] = useState<AttendanceRecord[]>([
    { id: 1, student_name: 'Alice Kumar', roll_number: 'CS001', status: 'present', check_in: '09:00', check_out: '17:00' },
    { id: 2, student_name: 'Bob Singh', roll_number: 'CS002', status: 'present', check_in: '09:15', check_out: '16:30' },
    { id: 3, student_name: 'Carol Devi', roll_number: 'CS003', status: 'late', check_in: '10:30', check_out: '17:00' },
  ])
  const [date] = useState(new Date().toISOString().split('T')[0])

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold">Attendance Management</h1>
        <input type="date" value={date} className="input w-40" />
      </div>

      <div className="grid grid-cols-4 gap-4">
        <div className="card text-center">
          <p className="text-dark-400">Total Present</p>
          <p className="text-3xl font-bold text-green-400">40</p>
        </div>
        <div className="card text-center">
          <p className="text-dark-400">Absent</p>
          <p className="text-3xl font-bold text-red-400">2</p>
        </div>
        <div className="card text-center">
          <p className="text-dark-400">Late</p>
          <p className="text-3xl font-bold text-yellow-400">1</p>
        </div>
        <div className="card text-center">
          <p className="text-dark-400">Left Early</p>
          <p className="text-3xl font-bold text-orange-400">0</p>
        </div>
      </div>

      <div className="card overflow-x-auto">
        <table className="w-full">
          <thead>
            <tr className="border-b border-dark-600">
              <th className="text-left py-3 px-4">Student</th>
              <th className="text-left py-3 px-4">Roll Number</th>
              <th className="text-left py-3 px-4">Status</th>
              <th className="text-left py-3 px-4">Check In</th>
              <th className="text-left py-3 px-4">Check Out</th>
            </tr>
          </thead>
          <tbody>
            {records.map(record => (
              <tr key={record.id} className="border-b border-dark-700 hover:bg-dark-700">
                <td className="py-3 px-4">{record.student_name}</td>
                <td className="py-3 px-4 text-dark-400">{record.roll_number}</td>
                <td className="py-3 px-4">
                  <span className={`badge-${record.status === 'present' ? 'success' : record.status === 'late' ? 'warning' : 'danger'}`}>
                    {record.status.toUpperCase()}
                  </span>
                </td>
                <td className="py-3 px-4">{record.check_in}</td>
                <td className="py-3 px-4">{record.check_out}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
