import { useState } from 'react'

interface Alert {
  id: number
  type: string
  student: string
  severity: 'low' | 'medium' | 'high' | 'critical'
  description: string
  timestamp: string
  acknowledged: boolean
}

export default function Alerts() {
  const [alerts] = useState<Alert[]>([
    { id: 1, type: 'Phone Detected', student: 'Student S5', severity: 'high', description: 'Cell phone detected in hand', timestamp: '2 min ago', acknowledged: false },
    { id: 2, type: 'Sleeping', student: 'Student S7', severity: 'critical', description: 'Student appears to be sleeping', timestamp: '5 min ago', acknowledged: false },
    { id: 3, type: 'Suspicious Interaction', student: 'S3 & S4', severity: 'high', description: 'Close proximity detected', timestamp: '12 min ago', acknowledged: true },
  ])
  const [filter, setFilter] = useState('all')

  const severityColors = {
    low: 'bg-blue-900/20 text-blue-400',
    medium: 'bg-yellow-900/20 text-yellow-400',
    high: 'bg-orange-900/20 text-orange-400',
    critical: 'bg-red-900/20 text-red-400',
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold">Alerts</h1>
        <select value={filter} onChange={(e) => setFilter(e.target.value)} className="input w-40">
          <option value="all">All Alerts</option>
          <option value="unread">Unread Only</option>
          <option value="critical">Critical Only</option>
        </select>
      </div>

      <div className="space-y-3">
        {alerts.map(alert => (
          <div key={alert.id} className="card flex items-center justify-between">
            <div className="flex-1">
              <div className="flex items-center gap-3 mb-2">
                <h3 className="font-semibold">{alert.type}</h3>
                <span className={`badge-${alert.severity}`}>{alert.severity.toUpperCase()}</span>
              </div>
              <p className="text-dark-400 text-sm">{alert.student}</p>
              <p className="text-dark-500 text-xs mt-1">{alert.description}</p>
              <p className="text-dark-500 text-xs mt-1">{alert.timestamp}</p>
            </div>
            <button className={`px-4 py-2 rounded-lg ${
              alert.acknowledged ? 'bg-dark-700 text-dark-400' : 'bg-blue-600 text-white hover:bg-blue-700'
            }`}>
              {alert.acknowledged ? '✓ Acknowledged' : 'Acknowledge'}
            </button>
          </div>
        ))}
      </div>
    </div>
  )
}
