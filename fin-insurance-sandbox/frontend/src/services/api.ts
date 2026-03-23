import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'

export class PolicyService {
  static async getPolicies() {
    const response = await axios.get(`${API_URL}/policies/`)
    return response.data
  }

  static async createPolicy(policy: any) {
    const response = await axios.post(`${API_URL}/policies/`, policy)
    return response.data
  }
}
