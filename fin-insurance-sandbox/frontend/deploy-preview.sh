set -e

echo "Starting preview deployment on port 5173..."

# Clean up any existing containers
docker-compose -f docker-compose.preview.yml down --remove-orphans 2>/dev/null || true

# Build and start
docker-compose -f docker-compose.preview.yml up --build -d

echo "Preview deployment started!"
echo "Access the application at: http://localhost:5173"
echo ""
echo "To stop the preview: docker-compose -f docker-compose.preview.yml down"
