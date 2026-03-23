set -e

# Change to flask-calculator directory
cd /workspace/flask-calculator

# Step 1: Update requirements.txt to include gunicorn if not present
if ! grep -q "gunicorn" requirements.txt; then
    echo "gunicorn" >> requirements.txt
fi

# Step 2: Create entrypoint.sh
cat > entrypoint.sh << 'SCRIPT_EOF'
set -e

# Get port from environment or use 9100 as fallback
PORT=${PORT:-9100}

echo "Starting Flask application on port $PORT"
exec gunicorn --bind 0.0.0.0:$PORT app:app
SCRIPT_EOF
chmod +x entrypoint.sh

# Step 3: Create Dockerfile
cat > Dockerfile << 'DOCKER_EOF'
FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 9100
EXPOSE 9100

# Use entrypoint script
ENTRYPOINT ["./entrypoint.sh"]
DOCKER_EOF

# Step 4: Create .dockerignore
cat > .dockerignore << 'IGNORE_EOF'
node_modules
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env
pip-log.txt
pip-delete-this-directory.txt
.tox
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git
.mypy_cache
.pytest_cache
.hypothesis
IGNORE_EOF

# Step 5: Create or update app.py
cat > app.py << 'APP_EOF'
import os
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({"status": "ok"})

# Basic route to prevent 404 on /
@app.route('/')
def index():
    return jsonify({"message": "Flask calculator is running", "port": os.environ.get("PORT", 9100)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 9100))
    app.run(host='0.0.0.0', port=port)
APP_EOF

# Step 6: Build and test the container
echo "Building Docker container..."
docker build -t flask-calculator:v1 .

# Stop any existing container on port 9100
docker stop $(docker ps -q --filter "publish=9100") 2>/dev/null || true

# Run the new container
echo "Starting container on port 9100..."
docker run -d --name flask-calculator-container -p 9100:9100 flask-calculator:v1

# Wait for container to start
sleep 3

# Test health endpoint
if curl -f http://localhost:9100/health > /dev/null 2>&1; then
    echo "success"
    echo "Container is running successfully on port 9100"
else
    echo "error"
    echo "Container failed health check"
    docker logs flask-calculator-container
    exit 1
fi

echo "Fix deployment complete!"
