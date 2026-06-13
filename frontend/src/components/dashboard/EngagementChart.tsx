import { Line } from 'react-chartjs-2'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

interface EngagementChartProps {
  data: { label: string; value: number }[]
}

export default function EngagementChart({ data }: EngagementChartProps) {
  const chartData = {
    labels: data.map(d => d.label),
    datasets: [
      {
        label: 'Engagement %',
        data: data.map(d => d.value),
        borderColor: '#2563EB',
        backgroundColor: 'rgba(37, 99, 235, 0.1)',
        tension: 0.4,
      },
    ],
  }

  const options = {
    responsive: true,
    plugins: {
      legend: {
        labels: { color: '#F1F5F9' },
      },
    },
    scales: {
      y: {
        ticks: { color: '#CBD5E1' },
        grid: { color: '#475569' },
      },
      x: {
        ticks: { color: '#CBD5E1' },
        grid: { color: '#475569' },
      },
    },
  }

  return (
    <div className="card">
      <h3 className="text-lg font-semibold mb-4">Engagement Trend</h3>
      <Line data={chartData} options={options} />
    </div>
  )
}
