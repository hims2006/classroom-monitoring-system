import { useState, useEffect } from 'react'
import KPICard from '../components/dashboard/KPICard'
import EngagementChart from '../components/dashboard/EngagementChart'
import RecentAlerts from '../components/dashboard/RecentAlerts'
import LoadingSpinner from '../components/common/LoadingSpinner'

export default function Dashboard() {
  const [loading, setLoading] = useState(true)
  const [dashData, setDashData] = useState({
    totalStudents: 42,
    engagement: 85,
    alerts: 3,
    phonesDetected: 1,
    drowsy: 2,
    sleeping: 0,
  })

  useEffect(() => {
    setTimeout(() => setLoading(false), 500)
  }, [])

  if (loading) return <LoadingSpinner />

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Dashboard</h1>

      <div className="grid grid-cols-4 gap-4">
        <KPICard title="Students" value={dashData.totalStudents} icon="👥" color="blue" />
        <KPICard title="Engagement" value={`${dashData.engagement}%`} icon="📊" color="green" trend={5} />
        <KPICard title="Alerts" value={dashData.alerts} icon="🚨" color="red" />
        <KPICard title="Phones" value={dashData.phonesDetected} icon="📱" color="yellow" />
      </div>

      <div className="grid grid-cols-3 gap-4">
        <KPICard title="Drowsy" value={dashData.drowsy} icon="😴" color="yellow" />
        <KPICard title="Sleeping" value={dashData.sleeping} icon="😴" color="red" />
        <KPICard title="Suspicious" value={0} icon="🚩" color="yellow" />
      </div>

      <div className="grid grid-cols-2 gap-6">
        <EngagementChart data={[
          { label: 'Mon', value: 78 },
          { label: 'Tue', value: 82 },
          { label: 'Wed', value: 85 },
          { label: 'Thu', value: 80 },
          { label: 'Fri', value: 88 },
        ]} />

        <RecentAlerts alerts={[
          { id: 1, type: 'Phone Detected', student: 'Student S5', time: '2 min ago', severity: 'high' },
          { id: 2, type: 'Sleeping', student: 'Student S7', time: '5 min ago', severity: 'critical' },
          { id: 3, type: 'Distracted', student: 'Student S12', time: '12 min ago', severity: 'medium' },
        ]} />
      </div>
    </div>
  )
}
