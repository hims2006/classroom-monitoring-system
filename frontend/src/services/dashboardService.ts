import api from './api'

export const dashboardService = {
  getSummary: async () => {
    const { data } = await api.get('/api/dashboard/summary')
    return data
  },

  getEngagement: async () => {
    const { data } = await api.get('/api/dashboard/engagement')
    return data
  },

  getRecentAlerts: async (limit: number = 10) => {
    const { data } = await api.get('/api/dashboard/alerts', { params: { limit } })
    return data
  },

  getTrends: async (days: number = 7) => {
    const { data } = await api.get('/api/dashboard/trends', { params: { days } })
    return data
  },
}
