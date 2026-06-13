import { useState } from 'react'

export default function Settings() {
  const [fullName, setFullName] = useState('John Teacher')
  const [email, setEmail] = useState('teacher@classroom.com')
  const [theme, setTheme] = useState('dark')
  const [notifications, setNotifications] = useState(true)

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Settings</h1>

      <div className="card">
        <h3 className="text-lg font-semibold mb-6">Profile Settings</h3>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2">Full Name</label>
            <input type="text" value={fullName} onChange={(e) => setFullName(e.target.value)} className="input" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-2">Email</label>
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} className="input" />
          </div>
          <button className="btn-primary">Save Changes</button>
        </div>
      </div>

      <div className="card">
        <h3 className="text-lg font-semibold mb-6">Preferences</h3>
        <div className="space-y-4">
          <div className="flex justify-between items-center">
            <label>Dark Theme</label>
            <input type="checkbox" checked={theme === 'dark'} className="w-4 h-4" />
          </div>
          <div className="flex justify-between items-center">
            <label>Enable Notifications</label>
            <input type="checkbox" checked={notifications} onChange={(e) => setNotifications(e.target.checked)} className="w-4 h-4" />
          </div>
        </div>
      </div>

      <div className="card border-red-600">
        <h3 className="text-lg font-semibold mb-4 text-red-400">Danger Zone</h3>
        <button className="px-4 py-2 bg-red-600 hover:bg-red-700 rounded-lg">Reset Password</button>
      </div>
    </div>
  )
}
