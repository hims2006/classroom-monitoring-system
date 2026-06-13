import { useState, useEffect } from 'react'

interface FetchState<T> {
  data: T | null
  loading: boolean
  error: Error | null
}

export const useFetch = <T>(url: string, dependencies: any[] = []): FetchState<T> => {
  const [state, setState] = useState<FetchState<T>>({
    data: null,
    loading: true,
    error: null,
  })

  useEffect(() => {
    const fetchData = async () => {
      try {
        setState(prev => ({ ...prev, loading: true }))
        // Mock fetch implementation
        setState(prev => ({ ...prev, loading: false }))
      } catch (error) {
        setState(prev => ({ ...prev, error: error as Error, loading: false }))
      }
    }

    fetchData()
  }, dependencies)

  return state
}
