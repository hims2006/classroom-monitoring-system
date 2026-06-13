import { useState } from 'react'

export default function Reports() {
  const [reportType, setReportType] = useState('daily')
  const [startDate, setStartDate] = useState('')
  const [endDate, setEndDate] = useState('')

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Reports & Analytics</h1>

      <div className="card">
        <h3 className="text-lg font-semibold mb-4">Generate Report</h3>
        <div className="grid grid-cols-3 gap-4">
          <div>
            <label className="block text-sm font-medium mb-2">Report Type</label>
            <select value={reportType} onChange={(e) => setReportType(e.target.value)} className="input">
              <option value="daily">Daily</option>
              <option value="weekly">Weekly</option>
              <option value="monthly">Monthly</option>
              <option value="custom">Custom</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium mb-2">Start Date</label>
            <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} className="input" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-2">End Date</label>
            <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} className="input" />
          </div>
        </div>
        <button className="btn-primary mt-4">Generate Report</button>
      </div>

      <div className="grid grid-cols-2 gap-6">
        <div className="card">
          <h3 className="text-lg font-semibold mb-4">Summary Statistics</h3>
          <div className="space-y-3">
            <div className="flex justify-between">
              <span className="text-dark-400">Total Students</span>
              <span className="font-semibold">42</span>
            </div>
            <div className="flex justify-between">
              <span className="text-dark-400">Avg. Engagement</span>
              <span className="font-semibold text-green-400">85%</span>
            </div>
            <div className="flex justify-between">
              <span className="text-dark-400">Total Alerts</span>
              <span className="font-semibold text-red-400">127</span>
            </div>
            <div className="flex justify-between">
              <span className="text-dark-400">Attendance Rate</span>
              <span className="font-semibold text-blue-400">95%</span>
            </div>
          </div>
        </div>

        <div className="card">
          <h3 className="text-lg font-semibold mb-4">Export Options</h3>
          <div className="space-y-2">
            <button className="w-full px-4 py-2 bg-dark-700 hover:bg-dark-600 rounded-lg text-left">📄 Download PDF</button>
            <button className="w-full px-4 py-2 bg-dark-700 hover:bg-dark-600 rounded-lg text-left">📊 Download Excel</button>
            <button className="w-full px-4 py-2 bg-dark-700 hover:bg-dark-600 rounded-lg text-left">📋 Download CSV</button>
          </div>
        </div>
      </div>
    </div>
  )
}
