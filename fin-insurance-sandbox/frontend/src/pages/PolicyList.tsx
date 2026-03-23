import React, { useState, useEffect } from 'react'
import { PolicyService } from '../services/api'

interface Policy {
  id: number
  policy_number: string
  holder_name: string
  premium: number
  coverage_amount: number
  status: string
}

const PolicyList: React.FC = () => {
  const [policies, setPolicies] = useState<Policy[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchPolicies()
  }, [])

  const fetchPolicies = async () => {
    try {
      const data = await PolicyService.getPolicies()
      setPolicies(data)
    } catch (err) {
      setError('Failed to load policies')
    } finally {
      setLoading(false)
    }
  }

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error}</div>

  return (
    <div>
      <h2>Insurance Policies</h2>
      <table>
        <thead>
          <tr>
            <th>Policy Number</th>
            <th>Holder Name</th>
            <th>Premium</th>
            <th>Coverage</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {policies.map(policy => (
            <tr key={policy.id}>
              <td>{policy.policy_number}</td>
              <td>{policy.holder_name}</td>
              <td>${policy.premium}</td>
              <td>${policy.coverage_amount}</td>
              <td>{policy.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default PolicyList
