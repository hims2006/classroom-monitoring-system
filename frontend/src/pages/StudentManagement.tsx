import { useState } from 'react'
import LoadingSpinner from '../components/common/LoadingSpinner'

interface Student {
  id: number
  roll_number: string
  name: string
  email: string
  engagement: number
  status: string
}

export default function StudentManagement() {
  const [students] = useState<Student[]>([
    { id: 1, roll_number: 'CS001', name: 'Alice Kumar', email: 'alice@college.edu', engagement: 92, status: 'active' },
    { id: 2, roll_number: 'CS002', name: 'Bob Singh', email: 'bob@college.edu', engagement: 78, status: 'active' },
    { id: 3, roll_number: 'CS003', name: 'Carol Devi', email: 'carol@college.edu', engagement: 65, status: 'active' },
  ])
  const [showForm, setShowForm] = useState(false)

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold">Student Management</h1>
        <button
          onClick={() => setShowForm(!showForm)}
          className="btn-primary"
        >
          + Add Student
        </button>
      </div>

      {showForm && (
        <div className="card">
          <h3 className="text-lg font-semibold mb-4">Add New Student</h3>
          <div className="grid grid-cols-2 gap-4">
            <input type="text" placeholder="Roll Number" className="input" />
            <input type="text" placeholder="Full Name" className="input" />
            <input type="email" placeholder="Email" className="input" />
            <select className="input">✓ Active</select>
          </div>
          <button className="btn-primary mt-4">Add Student</button>
        </div>
      )}

      <div className="card overflow-x-auto">
        <table className="w-full">
          <thead>
            <tr className="border-b border-dark-600">
              <th className="text-left py-3 px-4">Roll Number</th>
              <th className="text-left py-3 px-4">Name</th>
              <th className="text-left py-3 px-4">Email</th>
              <th className="text-left py-3 px-4">Engagement</th>
              <th className="text-left py-3 px-4">Actions</th>
            </tr>
          </thead>
          <tbody>
            {students.map(student => (
              <tr key={student.id} className="border-b border-dark-700 hover:bg-dark-700 transition">
                <td className="py-3 px-4">{student.roll_number}</td>
                <td className="py-3 px-4">{student.name}</td>
                <td className="py-3 px-4 text-dark-400">{student.email}</td>
                <td className="py-3 px-4">
                  <span className={`badge-${student.engagement > 80 ? 'success' : student.engagement > 60 ? 'warning' : 'danger'}`}>
                    {student.engagement}%
                  </span>
                </td>
                <td className="py-3 px-4 text-sm space-x-2">
                  <button className="text-blue-400 hover:text-blue-300">Edit</button>
                  <button className="text-red-400 hover:text-red-300">Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
