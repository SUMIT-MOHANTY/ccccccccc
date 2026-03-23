set -e
# Find available port
PORT=5000
while lsof -i:$PORT >/dev/null 2>&1; do
    PORT=$((PORT + 1))
done
echo "Using port: $PORT"
export PORT=$PORT
# Run with gunicorn for production
python3 -m gunicorn app:app -b "0.0.0.0:$PORT"
