import { configureStore } from '@reduxjs/toolkit'
import authReducer from './slices/authSlice'
import dashboardReducer from './slices/dashboardSlice'
import alertsReducer from './slices/alertsSlice'

const store = configureStore({
  reducer: {
    auth: authReducer,
    dashboard: dashboardReducer,
    alerts: alertsReducer,
  },
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch

export default store
