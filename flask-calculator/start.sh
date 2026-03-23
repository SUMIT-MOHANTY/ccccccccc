set -e

# Source environment
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

# Install dependencies
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    pip install flask gunicorn
fi

# Determine final port
PORT=${PORT:-$(python -c "import socket; s=socket.socket(); s.bind(('', 0)); p=s.getsockname()[1]; s.close(); print(p)")}
export PORT

echo "Starting Flask app on port $PORT..."
gunicorn app:app -b 0.0.0.0:$PORT --workers 1 --threads 8 --max-requests 1000 --max-requests-jitter 100 --timeout 30
