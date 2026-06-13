import api from './api'

export interface LoginCredentials {
  email: string
  password: string
}

export interface User {
  id: number
  username: string
  email: string
  full_name: string
  role: 'admin' | 'teacher'
  is_active: boolean
}

export interface TokenResponse {
  access_token: string
  token_type: string
  user: User
}

export const authService = {
  login: async (credentials: LoginCredentials): Promise<TokenResponse> => {
    const { data } = await api.post('/api/auth/login', credentials)
    return data
  },

  register: async (userData: any): Promise<User> => {
    const { data } = await api.post('/api/auth/register', userData)
    return data
  },

  logout: async (): Promise<void> => {
    await api.post('/api/auth/logout')
  },

  getCurrentUser: async (): Promise<User> => {
    const { data } = await api.get('/api/auth/me')
    return data
  },

  refreshToken: async (): Promise<TokenResponse> => {
    const { data } = await api.post('/api/auth/refresh-token')
    return data
  },
}
