import { useEffect, useRef, useState } from 'react'

interface WebSocketState {
  data: any
  isConnected: boolean
  error: Error | null
}

export const useWebSocket = (url: string): WebSocketState => {
  const ws = useRef<WebSocket | null>(null)
  const [state, setState] = useState<WebSocketState>({
    data: null,
    isConnected: false,
    error: null,
  })

  useEffect(() => {
    try {
      ws.current = new WebSocket(url)

      ws.current.onopen = () => {
        setState(prev => ({ ...prev, isConnected: true }))
      }

      ws.current.onmessage = (event) => {
        setState(prev => ({ ...prev, data: JSON.parse(event.data) }))
      }

      ws.current.onerror = (error) => {
        setState(prev => ({ ...prev, error: new Error('WebSocket error') }))
      }

      ws.current.onclose = () => {
        setState(prev => ({ ...prev, isConnected: false }))
      }
    } catch (error) {
      setState(prev => ({ ...prev, error: error as Error }))
    }

    return () => {
      if (ws.current) {
        ws.current.close()
      }
    }
  }, [url])

  return state
}
