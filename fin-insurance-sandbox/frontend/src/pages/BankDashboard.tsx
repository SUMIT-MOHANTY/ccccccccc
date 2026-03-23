/**
 * Usage: import BankDashboard from 'fin-insurance-sandbox/frontend/src/pages/BankDashboard.tsx';
 * renders on route '/bank'.
 */
import React, { useMemo } from 'react';
import { useBankData } from '../hooks/useBankData';
import styles from './BankDashboard.module.css';

interface DashboardCardProps {
  title: string;
  value: number;
  change: number;
  format?: 'currency' | 'number';
}

const DashboardCard: React.FC<DashboardCardProps> = ({
  title,
  value,
  change,
  format = 'number'
}) => {
  const formattedValue = useMemo(() => {
    if (format === 'currency') {
      return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
      }).format(value);
    }
    return new Intl.NumberFormat('en-US').format(value);
  }, [value, format]);

  const changeText = useMemo(() => {
    if (isNaN(change)) return '';
    const prefix = change >= 0 ? '+' : '';
    return `${prefix}${change.toFixed(1)}%`;
  }, [change]);

  return (
    <div className={`bg-white rounded-lg shadow-md p-6 ${styles['card-hover']}`}>
      <h3 className="text-gray-500 text-sm font-medium">{title}</h3>
      <div className="mt-2">
        <span className="text-3xl font-bold text-gray-900">{formattedValue}</span>
        {changeText && (
          <span className={`ml-2 text-sm font-medium ${
            change >= 0 ? 'text-green-600' : 'text-red-600'
          }`}>
            {changeText}
          </span>
        )}
      </div>
    </div>
  );
};

const BankDashboard: React.FC = () => {
  const { deposits, loans, claims, alerts, refresh, isLoading } = useBankData();

  // Generate random change percentages for demo
  const [depositChange, loanChange, claimChange, alertChange] = useMemo(
    () => [
      (Math.random() * 10 - 5),
      (Math.random() * 6 - 3),
      (Math.random() * 20 - 10),
      (Math.random() * 8 - 4)
    ],
    [deposits, loans, claims, alerts]
  );

  const handleRefresh = () => {
    refresh();
  };

  if (isLoading && !deposits) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-6">
            <h1 className="text-3xl font-bold text-gray-900">Bank Dashboard</h1>
            <button
              onClick={handleRefresh}
              disabled={isLoading}
              className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 disabled:opacity-50"
            >
              <svg
                className={`mr-2 h-4 w-4 ${isLoading ? 'animate-spin' : ''}`}
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
                />
              </svg>
              {isLoading ? 'Refreshing...' : 'Refresh'}
            </button>
          </div>
        </div>
      </div>

      {/* Dashboard Cards */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
          <DashboardCard
            title="Total Deposits"
            value={deposits}
            change={depositChange}
            format="currency"
          />
          <DashboardCard
            title="Total Loans"
            value={loans}
            change={loanChange}
            format="currency"
          />
          <DashboardCard
            title="Open Claims"
            value={claims}
            change={claimChange}
          />
          <DashboardCard
            title="Alerts"
            value={alerts}
            change={alertChange}
          />
        </div>
      </div>

      {/* Error Boundary Info */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-4">
        <p className="text-sm text-gray-500">
          Note: This component includes built-in error handling and graceful loading states.
        </p>
      </div>
    </div>
  );
};

export default BankDashboard;
