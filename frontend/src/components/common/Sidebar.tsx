import { Link, useLocation } from 'react-router-dom'
import { useSelector } from 'react-redux'
import { RootState } from '../../store'

const menuItems = [
  { path: '/dashboard', label: 'Dashboard', icon: '📊' },
  { path: '/monitoring', label: 'Live Monitoring', icon: '📹' },
  { path: '/students', label: 'Students', icon: '👥' },
  { path: '/attendance', label: 'Attendance', icon: '📋' },
  { path: '/alerts', label: 'Alerts', icon: '🚨' },
  { path: '/reports', label: 'Reports', icon: '📈' },
]

export default function Sidebar() {
  const location = useLocation()
  const auth = useSelector((state: RootState) => state.auth)

  const isActive = (path: string) => location.pathname === path

  return (
    <aside className="bg-dark-800 border-r border-dark-600 w-64 h-screen flex flex-col">
      <div className="flex-1 p-6">
        <nav className="space-y-2">
          {menuItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className={`flex items-center gap-3 px-4 py-2 rounded-lg transition ${
                isActive(item.path)
                  ? 'bg-blue-600/20 text-blue-400 border-l-2 border-blue-600'
                  : 'text-dark-300 hover:bg-dark-700'
              }`}
            >
              <span>{item.icon}</span>
              <span>{item.label}</span>
            </Link>
          ))}
        </nav>
      </div>

      <div className="p-6 border-t border-dark-600">
        <div className="text-sm text-dark-400">
          <p>Role: {auth.user?.role.toUpperCase()}</p>
          <p className="mt-2 text-xs text-dark-500">v1.0.0</p>
        </div>
      </div>
    </aside>
  )
}
