set -e

cd /workspace/fin-insurance-sandbox/frontend

# Find available port
find_free_port() {
  local port=5173
  while lsof -i:$port >/dev/null 2>&1; do
    port=$((port + 1))
  done
  echo $port
}

PORT=$(find_free_port)
if [ "$PORT" != "5173" ]; then
  echo "Port 5173 in use, starting on port $PORT instead"
fi

echo "Starting application on port $PORT..."
npm run dev -- --host 0.0.0.0 --port "$PORT"
