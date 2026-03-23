/**
 * Custom hook for mock bank dashboard data
 * Returns: { deposits, loans, claims, alerts, refresh, isLoading }
 */
import { useState, useEffect, useCallback } from 'react';

interface BankData {
  deposits: number;
  loans: number;
  claims: number;
  alerts: number;
}

interface UseBankDataReturn {
  deposits: number;
  loans: number;
  claims: number;
  alerts: number;
  refresh: () => Promise<void>;
  isLoading: boolean;
}

export const useBankData = (): UseBankDataReturn => {
  const [data, setData] = useState<BankData>({
    deposits: 0,
    loans: 0,
    claims: 0,
    alerts: 0
  });
  const [isLoading, setIsLoading] = useState(false);

  const fetchData = useCallback(async () => {
    setIsLoading(true);
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 500 + Math.random() * 500));

    // Generate mock data
    setData({
      deposits: Math.floor(Math.random() * 1000000) + 500000,
      loans: Math.floor(Math.random() * 800000) + 200000,
      claims: Math.floor(Math.random() * 50) + 10,
      alerts: Math.floor(Math.random() * 30) + 5
    });
    setIsLoading(false);
  }, []);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  return {
    ...data,
    refresh: fetchData,
    isLoading
  };
};
