import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface DashboardState {
  totalStudents: number
  engagement: number
  alerts: number
  phonesDetected: number
  drowsy: number
  sleeping: number
  moving: number
  standing: number
  suspicious: number
  loading: boolean
}

const initialState: DashboardState = {
  totalStudents: 0,
  engagement: 0,
  alerts: 0,
  phonesDetected: 0,
  drowsy: 0,
  sleeping: 0,
  moving: 0,
  standing: 0,
  suspicious: 0,
  loading: false,
}

const dashboardSlice = createSlice({
  name: 'dashboard',
  initialState,
  reducers: {
    setDashboardData: (state, action: PayloadAction<Partial<DashboardState>>) => {
      return { ...state, ...action.payload }
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload
    },
  },
})

export const { setDashboardData, setLoading } = dashboardSlice.actions
export default dashboardSlice.reducer
