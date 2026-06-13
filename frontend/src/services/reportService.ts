import api from './api'

export const reportService = {
  generateReport: async (reportData: any) => {
    const { data } = await api.post('/api/reports/generate', reportData)
    return data
  },

  getReports: async (skip: number = 0, limit: number = 50, reportType?: string) => {
    const { data } = await api.get('/api/reports', { params: { skip, limit, report_type: reportType } })
    return data
  },

  getReport: async (id: number) => {
    const { data } = await api.get(`/api/reports/${id}`)
    return data
  },

  exportReport: async (id: number, format: 'pdf' | 'excel' | 'csv') => {
    const { data } = await api.post(`/api/reports/${id}/export`, {}, { params: { format } })
    return data
  },

  deleteReport: async (id: number) => {
    await api.delete(`/api/reports/${id}`)
  },
}
