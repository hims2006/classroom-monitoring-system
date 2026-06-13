interface Alert {
  id: number
  type: string
  student: string
  time: string
  severity: 'low' | 'medium' | 'high' | 'critical'
}

interface RecentAlertsProps {
  alerts: Alert[]
}

const severityColors = {
  low: 'bg-blue-900/20 text-blue-400',
  medium: 'bg-yellow-900/20 text-yellow-400',
  high: 'bg-orange-900/20 text-orange-400',
  critical: 'bg-red-900/20 text-red-400',
}

export default function RecentAlerts({ alerts }: RecentAlertsProps) {
  return (
    <div className="card">
      <h3 className="text-lg font-semibold mb-4">Recent Alerts</h3>
      <div className="space-y-3">
        {alerts.length === 0 ? (
          <p className="text-dark-400">No alerts</p>
        ) : (
          alerts.map(alert => (
            <div key={alert.id} className="flex items-center justify-between p-3 bg-dark-700 rounded-lg">
              <div className="flex-1">
                <p className="text-sm font-medium">{alert.student}</p>
                <p className="text-xs text-dark-400">{alert.type}</p>
              </div>
              <div className="text-right">
                <span className={`px-2 py-1 text-xs rounded ${severityColors[alert.severity]}`}>
                  {alert.severity.toUpperCase()}
                </span>
                <p className="text-xs text-dark-400 mt-1">{alert.time}</p>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  )
}
