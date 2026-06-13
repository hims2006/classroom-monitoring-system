import api from './api'

export const studentService = {
  getStudents: async (skip: number = 0, limit: number = 50) => {
    const { data } = await api.get('/api/students', { params: { skip, limit } })
    return data
  },

  getStudent: async (id: number) => {
    const { data } = await api.get(`/api/students/${id}`)
    return data
  },

  createStudent: async (studentData: any) => {
    const { data } = await api.post('/api/students', studentData)
    return data
  },

  updateStudent: async (id: number, studentData: any) => {
    const { data } = await api.put(`/api/students/${id}`, studentData)
    return data
  },

  deleteStudent: async (id: number) => {
    await api.delete(`/api/students/${id}`)
  },

  searchStudents: async (query: string) => {
    const { data } = await api.get(`/api/students/search/${query}`)
    return data
  },
}
