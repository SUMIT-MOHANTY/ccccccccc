set -e

# Find next available port starting from 5000
find_port() {
    local port=$1
    while netstat -tuln | grep -q ":$port "; do
        port=$((port + 1))
        echo "Port conflict detected, trying $port..."
    done
    echo $port
}

# Get available port
PORT=$(find_port 5000)
export PORT

# Create runtime configuration
cat <<CONFIG > runtime.env
FLASK_APP=app.py
FLASK_ENV=production
PORT=$PORT
CONFIG

echo "Starting Flask on port $PORT..."
exec flask run --host=0.0.0.0 --port=$PORT
