import api from './api'

export const alertService = {
  getAlerts: async (skip: number = 0, limit: number = 50, filters?: any) => {
    const { data } = await api.get('/api/alerts', { params: { skip, limit, ...filters } })
    return data
  },

  getAlert: async (id: number) => {
    const { data } = await api.get(`/api/alerts/${id}`)
    return data
  },

  acknowledgeAlert: async (id: number) => {
    const { data } = await api.put(`/api/alerts/${id}/acknowledge`)
    return data
  },

  deleteAlert: async (id: number) => {
    await api.delete(`/api/alerts/${id}`)
  },
}
