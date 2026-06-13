import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import { logout } from '../../store/slices/authSlice'
import { RootState } from '../../store'

export default function Header() {
  const navigate = useNavigate()
  const dispatch = useDispatch()
  const [showMenu, setShowMenu] = useState(false)
  const auth = useSelector((state: RootState) => state.auth)
  const alerts = useSelector((state: RootState) => state.alerts)

  const handleLogout = () => {
    dispatch(logout())
    navigate('/login')
  }

  return (
    <header className="bg-dark-800 border-b border-dark-600 px-6 py-4 flex justify-between items-center">
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center text-white font-bold">
          AC
        </div>
        <h1 className="text-xl font-bold text-dark-100">Classroom Monitor</h1>
      </div>

      <div className="flex items-center gap-6">
        {/* Notifications */}
        <div className="relative cursor-pointer">
          <div className="text-dark-300 hover:text-dark-100 transition">
            🔔
            {alerts.unreadCount > 0 && (
              <span className="absolute top-0 right-0 w-5 h-5 bg-red-500 text-white text-xs rounded-full flex items-center justify-center">
                {alerts.unreadCount}
              </span>
            )}
          </div>
        </div>

        {/* User Menu */}
        <div className="relative">
          <button
            onClick={() => setShowMenu(!showMenu)}
            className="flex items-center gap-2 px-3 py-2 bg-dark-700 rounded-lg hover:bg-dark-600 transition"
          >
            <span>{auth.user?.full_name}</span>
            <span>▼</span>
          </button>

          {showMenu && (
            <div className="absolute right-0 mt-2 w-48 bg-dark-800 border border-dark-600 rounded-lg shadow-lg z-50">
              <div className="p-2">
                <button
                  onClick={() => navigate('/settings')}
                  className="w-full text-left px-4 py-2 hover:bg-dark-700 rounded"
                >
                  Settings
                </button>
                <button
                  onClick={handleLogout}
                  className="w-full text-left px-4 py-2 hover:bg-dark-700 rounded text-red-400"
                >
                  Logout
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </header>
  )
}
