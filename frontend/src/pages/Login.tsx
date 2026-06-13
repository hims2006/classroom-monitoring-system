import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useDispatch } from 'react-redux'
import { setUser } from '../store/slices/authSlice'
import { authService } from '../services/authService'
import AlertBanner from '../components/common/AlertBanner'

export default function Login() {
  const navigate = useNavigate()
  const dispatch = useDispatch()
  const [email, setEmail] = useState('teacher@classroom.com')
  const [password, setPassword] = useState('Teacher@123')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError(null)

    try {
      const response = await authService.login({ email, password })
      dispatch(setUser({ user: response.user, token: response.access_token }))
      navigate('/dashboard')
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Login failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-dark-900">
      <div className="card w-full max-w-md">
        <div className="text-center mb-6">
          <h1 className="text-3xl font-bold">🎓 Classroom Monitor</h1>
          <p className="text-dark-400 mt-2">Sign in to your account</p>
        </div>

        {error && <AlertBanner type="error" message={error} onClose={() => setError(null)} />}

        <form onSubmit={handleLogin} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="input"
              placeholder="your@email.com"
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="input"
              placeholder="Enter your password"
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full btn-primary py-3 font-semibold disabled:opacity-50"
          >
            {loading ? 'Signing in...' : 'Sign In'}
          </button>
        </form>

        <p className="text-center text-dark-400 text-sm mt-6">
          Demo credentials provided above
        </p>
      </div>
    </div>
  )
}
