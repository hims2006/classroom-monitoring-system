interface AlertBannerProps {
  type: 'success' | 'error' | 'warning' | 'info'
  message: string
  onClose?: () => void
}

export default function AlertBanner({ type, message, onClose }: AlertBannerProps) {
  const colors = {
    success: 'bg-green-900/20 text-green-400 border-green-600',
    error: 'bg-red-900/20 text-red-400 border-red-600',
    warning: 'bg-yellow-900/20 text-yellow-400 border-yellow-600',
    info: 'bg-blue-900/20 text-blue-400 border-blue-600',
  }

  return (
    <div className={`border ${colors[type]} p-4 rounded-lg mb-4 flex justify-between items-center`}>
      <span>{message}</span>
      {onClose && (
        <button onClick={onClose} className="text-lg hover:opacity-70">
          ✕
        </button>
      )}
    </div>
  )
}
