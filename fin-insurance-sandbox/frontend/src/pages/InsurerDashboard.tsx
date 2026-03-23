import React, { useState, useEffect } from 'react';

// TypeScript interfaces
interface Policy {
  id: string;
  holderName: string;
  policyNumber: string;
  premium: number;
  status: 'active' | 'pending' | 'expired';
  risk: 'low' | 'medium' | 'high';
}

interface Claim {
  id: string;
  policyNumber: string;
  claimAmount: number;
  status: 'pending' | 'approved' | 'rejected';
  createdAt: string;
}

interface DashboardStats {
  totalPolicies: number;
  activePolicies: number;
  pendingClaims: number;
  totalRevenue: number;
}

const InsurerDashboard: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [stats, setStats] = useState<DashboardStats>({
    totalPolicies: 0,
    activePolicies: 0,
    pendingClaims: 0,
    totalRevenue: 0,
  });
  const [policies, setPolicies] = useState<Policy[]>([]);
  const [claims, setClaims] = useState<Claim[]>([]);

  // Mock data
  const mockStats: DashboardStats = {
    totalPolicies: 1247,
    activePolicies: 1053,
    pendingClaims: 18,
    totalRevenue: 485600,
  };

  const mockPolicies: Policy[] = [
    {
      id: '1',
      holderName: 'Alice Johnson',
      policyNumber: 'IP2024-001',
      premium: 2500,
      status: 'active',
      risk: 'low',
    },
    {
      id: '2',
      holderName: 'Bob Smith',
      policyNumber: 'IP2024-002',
      premium: 3200,
      status: 'active',
      risk: 'medium',
    },
    {
      id: '3',
      holderName: 'Carol Williams',
      policyNumber: 'IP2024-003',
      premium: 4100,
      status: 'pending',
      risk: 'high',
    },
    {
      id: '4',
      holderName: 'David Brown',
      policyNumber: 'IP2024-004',
      premium: 1800,
      status: 'expired',
      risk: 'low',
    },
  ];

  const mockClaims: Claim[] = [
    {
      id: '1',
      policyNumber: 'IP2024-001',
      claimAmount: 15000,
      status: 'pending',
      createdAt: '2024-01-15',
    },
    {
      id: '2',
      policyNumber: 'IP2024-002',
      claimAmount: 25000,
      status: 'pending',
      createdAt: '2024-01-14',
    },
    {
      id: '3',
      policyNumber: 'IP2024-005',
      claimAmount: 5000,
      status: 'approved',
      createdAt: '2024-01-13',
    },
  ];

  useEffect(() => {
    // Simulate API call
    const loadDashboardData = async () => {
      try {
        setLoading(true);
        // Simulate network delay
        await new Promise(resolve => setTimeout(resolve, 1000));

        setStats(mockStats);
        setPolicies(mockPolicies);
        setClaims(mockClaims);
        setError(null);
      } catch (err) {
        setError('Failed to load dashboard data');
      } finally {
        setLoading(false);
      }
    };

    loadDashboardData();
  }, []);

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'active': return 'bg-green-100 text-green-800';
      case 'pending': return 'bg-yellow-100 text-yellow-800';
      case 'expired': return 'bg-red-100 text-red-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  const getRiskColor = (risk: string) => {
    switch (risk) {
      case 'low': return 'text-green-600';
      case 'medium': return 'text-yellow-600';
      case 'high': return 'text-red-600';
      default: return 'text-gray-600';
    }
  };

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
    }).format(amount);
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="bg-white rounded-lg shadow-md p-6 max-w-md">
          <h2 className="text-xl font-semibold text-red-600 mb-2">Error</h2>
          <p className="text-gray-600">{error}</p>
          <button
            onClick={() => window.location.reload()}
            className="mt-4 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900">Insurer Dashboard</h1>
          <p className="mt-2 text-sm text-gray-600">Manage your insurance portfolio and claims</p>
        </div>

        {/* Stats Overview */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center">
              <div className="p-2 rounded-full bg-blue-100">
                <svg className="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Total Policies</p>
                <p className="text-2xl font-semibold text-gray-900">{stats.totalPolicies}</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center">
              <div className="p-2 rounded-full bg-green-100">
                <svg className="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Active Policies</p>
                <p className="text-2xl font-semibold text-gray-900">{stats.activePolicies}</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center">
              <div className="p-2 rounded-full bg-yellow-100">
                <svg className="w-6 h-6 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                </svg>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Pending Claims</p>
                <p className="text-2xl font-semibold text-gray-900">{stats.pendingClaims}</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center">
              <div className="p-2 rounded-full bg-purple-100">
                <svg className="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Total Revenue</p>
                <p className="text-2xl font-semibold text-gray-900">{formatCurrency(stats.totalRevenue)}</p>
              </div>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Policy Management */}
          <div className="bg-white rounded-lg shadow">
            <div className="px-6 py-4 border-b border-gray-200">
              <h2 className="text-lg font-semibold text-gray-900">Policy Management</h2>
            </div>
            <div className="p-6">
              <div className="space-y-4">
                {policies.slice(0, 3).map((policy) => (
                  <div key={policy.id} className="flex justify-between items-center p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors">
                    <div>
                      <p className="font-medium text-gray-900">{policy.policyNumber}</p>
                      <p className="text-sm text-gray-600">{policy.holderName}</p>
                      <p className={`text-sm font-medium ${getRiskColor(policy.risk)}`}>
                        Risk: {policy.risk}
                      </p>
                    </div>
                    <div className="text-right">
                      <p className="font-semibold text-gray-900">{formatCurrency(policy.premium)}</p>
                      <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${getStatusColor(policy.status)}`}>
                        {policy.status}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
              <button className="mt-4 w-full px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors">
                View All Policies
              </button>
            </div>
          </div>

          {/* Claims Overview */}
          <div className="bg-white rounded-lg shadow">
            <div className="px-6 py-4 border-b border-gray-200">
              <h2 className="text-lg font-semibold text-gray-900">Recent Claims</h2>
            </div>
            <div className="p-6">
              <div className="space-y-4">
                {claims.filter(c => c.status === 'pending').slice(0, 3).map((claim) => (
                  <div key={claim.id} className="p-4 bg-red-50 rounded-lg hover:bg-red-100 transition-colors">
                    <div className="flex justify-between">
                      <div>
                        <p className="font-medium text-gray-900">Claim #{claim.id}</p>
                        <p className="text-sm text-gray-600">Policy: {claim.policyNumber}</p>
                        <p className="text-sm text-gray-500">{new Date(claim.createdAt).toLocaleDateString()}</p>
                      </div>
                      <div className="text-right">
                        <p className="font-semibold text-gray-900">{formatCurrency(claim.claimAmount)}</p>
                        <span className={`inline-flex px-2 py-1 mt-1 text-xs font-semibold rounded-full ${getStatusColor(claim.status)}`}>
                          {claim.status}
                        </span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
              <button className="mt-4 w-full px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 transition-colors">
                Review Claims
              </button>
            </div>
          </div>

          {/* Risk Alerts */}
          <div className="bg-white rounded-lg shadow">
            <div className="px-6 py-4 border-b border-gray-200">
              <h2 className="text-lg font-semibold text-gray-900">Risk Alerts</h2>
            </div>
            <div className="p-6">
              <div className="space-y-3">
                {policies.filter(p => p.risk === 'high').map((policy) => (
                  <div key={policy.id} className="flex justify-between items-center p-3 bg-red-50 border-l-4 border-red-400">
                    <div>
                      <p className="font-medium text-red-800">{policy.policyNumber}</p>
                      <p className="text-sm text-red-600">{policy.holderName}</p>
                    </div>
                    <span className="text-sm text-red-800 font-medium">HIGH RISK</span>
                  </div>
                ))}
                {policies.filter(p => p.risk === 'high').length === 0 && (
                  <p className="text-gray-500 text-center">No high-risk alerts</p>
                )}
              </div>
            </div>
          </div>

          {/* Quick Actions */}
          <div className="bg-white rounded-lg shadow">
            <div className="px-6 py-4 border-b border-gray-200">
              <h2 className="text-lg font-semibold text-gray-900">Quick Actions</h2>
            </div>
            <div className="p-6 space-y-3">
              <button className="w-full px-4 py-3 bg-green-600 text-white rounded-md hover:bg-green-700 transition-colors flex items-center justify-center">
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
                Create New Policy
              </button>
              <button className="w-full px-4 py-3 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors flex items-center justify-center">
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                Generate Report
              </button>
              <button className="w-full px-4 py-3 bg-gray-600 text-white rounded-md hover:bg-gray-700 transition-colors flex items-center justify-center">
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.869 9.869 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                </svg>
                Customer Support
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InsurerDashboard;
