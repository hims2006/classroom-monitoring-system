import { useNavigate } from 'react-router-dom'
import { useAuth } from '../hooks/useAuth'

export default function LandingPage() {
  const navigate = useNavigate()
  const auth = useAuth()

  if (auth.isAuthenticated) {
    navigate('/dashboard')
    return null
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-dark-900 to-dark-800">
      <nav className="flex justify-between items-center px-6 py-4">
        <h1 className="text-2xl font-bold">🎓 AI Classroom Monitor</h1>
        <button onClick={() => navigate('/login')} className="btn-primary">
          Login
        </button>
      </nav>

      <div className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-center mb-20">
          <h2 className="text-5xl font-bold mb-6">Real-time Student Engagement Monitoring</h2>
          <p className="text-xl text-dark-300 mb-8">Using AI & Computer Vision to enhance classroom experience</p>
          <div className="flex gap-4 justify-center">
            <button onClick={() => navigate('/login')} className="btn-primary text-lg px-8 py-3">
              Get Started
            </button>
            <button className="px-8 py-3 border border-blue-600 text-blue-400 rounded-lg hover:bg-blue-600/10 transition">
              Learn More
            </button>
          </div>
        </div>

        <div className="grid grid-cols-3 gap-6">
          {[
            { icon: '📊', title: 'Real-time Monitoring', desc: 'Live engagement tracking' },
            { icon: '📹', title: 'AI Detection', desc: 'Phone & drowsy detection' },
            { icon: '📈', title: 'Analytics', desc: 'Detailed insights & reports' },
          ].map((feature, i) => (
            <div key={i} className="card text-center">
              <div className="text-5xl mb-4">{feature.icon}</div>
              <h3 className="text-lg font-semibold mb-2">{feature.title}</h3>
              <p className="text-dark-400 text-sm">{feature.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
