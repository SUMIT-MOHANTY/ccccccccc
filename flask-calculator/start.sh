set -e

echo "Starting Flask application..."

# Use environment variable or default
PORT=${PORT:-5000}

# Check if port is available
if netstat -tuln | grep -q ":${PORT}"; then
    echo "Port ${PORT} is already in use, using port 5001 instead"
    PORT=5001
fi

echo "Starting flask on port ${PORT}"
python app.py
