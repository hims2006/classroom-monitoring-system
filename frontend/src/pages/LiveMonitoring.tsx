import { useState } from 'react'
import LoadingSpinner from '../components/common/LoadingSpinner'

export default function LiveMonitoring() {
  const [isStreaming, setIsStreaming] = useState(false)

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold">Live Monitoring</h1>
        <button
          onClick={() => setIsStreaming(!isStreaming)}
          className={`px-6 py-2 rounded-lg font-semibold transition ${
            isStreaming
              ? 'bg-red-600 hover:bg-red-700'
              : 'bg-green-600 hover:bg-green-700'
          }`}
        >
          {isStreaming ? '⏹ Stop Stream' : '▶ Start Stream'}
        </button>
      </div>

      <div className="grid grid-cols-3 gap-6">
        {/* Video Feed */}
        <div className="col-span-2 card aspect-video bg-dark-700 flex items-center justify-center rounded-lg">
          {isStreaming ? (
            <div className="text-center">
              <div className="inline-block w-16 h-16 bg-red-600 rounded-full mb-4 animate-pulse"></div>
              <p>Live Feed - Camera Active</p>
            </div>
          ) : (
            <div className="text-center text-dark-400">
              <p className="text-lg">📹</p>
              <p>Click "Start Stream" to begin monitoring</p>
            </div>
          )}
        </div>

        {/* Status Panel */}
        <div className="space-y-4">
          <div className="card">
            <h3 className="font-semibold mb-3">Real-time Metrics</h3>
            <div className="space-y-2">
              <div className="flex justify-between">
                <span className="text-dark-400">Students Detected:</span>
                <span className="font-semibold">42</span>
              </div>
              <div className="flex justify-between">
                <span className="text-dark-400">Engagement:</span>
                <span className="font-semibold text-green-400">85%</span>
              </div>
              <div className="flex justify-between">
                <span className="text-dark-400">Alerts:</span>
                <span className="font-semibold text-red-400">3</span>
              </div>
              <div className="flex justify-between">
                <span className="text-dark-400">Phones:</span>
                <span className="font-semibold text-yellow-400">1</span>
              </div>
            </div>
          </div>

          <div className="card">
            <h3 className="font-semibold mb-3">Status Summary</h3>
            <div className="space-y-2 text-sm">
              <p>✓ Moving: 5</p>
              <p>✓ Standing: 2</p>
              <p>⚠ Drowsy: 2</p>
              <p>🔴 Sleeping: 0</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
