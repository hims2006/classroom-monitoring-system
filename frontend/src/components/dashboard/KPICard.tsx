interface KPICardProps {
  title: string
  value: number | string
  icon: string
  color?: 'blue' | 'green' | 'red' | 'yellow'
  trend?: number
}

const colorClasses = {
  blue: 'bg-blue-900/20 text-blue-400',
  green: 'bg-green-900/20 text-green-400',
  red: 'bg-red-900/20 text-red-400',
  yellow: 'bg-yellow-900/20 text-yellow-400',
}

export default function KPICard({ title, value, icon, color = 'blue', trend }: KPICardProps) {
  return (
    <div className="card">
      <div className="flex items-start justify-between">
        <div>
          <p className="text-dark-400 text-sm">{title}</p>
          <p className="text-3xl font-bold text-dark-100 mt-2">{value}</p>
          {trend !== undefined && (
            <p className={`text-sm mt-2 ${trend >= 0 ? 'text-green-400' : 'text-red-400'}`}>
              {trend >= 0 ? '↑' : '↓'} {Math.abs(trend)}%
            </p>
          )}
        </div>
        <div className={`text-4xl p-3 rounded-lg ${colorClasses[color]}`}>
          {icon}
        </div>
      </div>
    </div>
  )
}
