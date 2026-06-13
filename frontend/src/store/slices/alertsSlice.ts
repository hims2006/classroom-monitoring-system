import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface Alert {
  id: number
  student_id: number | null
  alert_type: string
  severity: 'low' | 'medium' | 'high' | 'critical'
  description: string | null
  is_acknowledged: boolean
  created_at: string
}

interface AlertsState {
  alerts: Alert[]
  unreadCount: number
  loading: boolean
}

const initialState: AlertsState = {
  alerts: [],
  unreadCount: 0,
  loading: false,
}

const alertsSlice = createSlice({
  name: 'alerts',
  initialState,
  reducers: {
    setAlerts: (state, action: PayloadAction<Alert[]>) => {
      state.alerts = action.payload
      state.unreadCount = action.payload.filter(a => !a.is_acknowledged).length
    },
    addAlert: (state, action: PayloadAction<Alert>) => {
      state.alerts.unshift(action.payload)
      if (!action.payload.is_acknowledged) {
        state.unreadCount += 1
      }
    },
    acknowledgeAlert: (state, action: PayloadAction<number>) => {
      const alert = state.alerts.find(a => a.id === action.payload)
      if (alert && !alert.is_acknowledged) {
        alert.is_acknowledged = true
        state.unreadCount -= 1
      }
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload
    },
  },
})

export const { setAlerts, addAlert, acknowledgeAlert, setLoading } = alertsSlice.actions
export default alertsSlice.reducer
