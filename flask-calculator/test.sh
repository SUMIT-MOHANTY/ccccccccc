set -e

echo "Testing Flask Calculator..."

# Install curl if not present
if ! command -v curl &> /dev/null; then
    if command -v apt-get &> /dev/null; then
        apt-get update && apt-get install -y curl
    elif command -v yum &> /dev/null; then
        yum install -y curl
    fi
fi

# Start app in background
export PORT=5009
./start.sh &
APP_PID=$!

sleep 5

# Test health endpoint
if curl -f http://localhost:5009/health >/dev/null 2>&1; then
    echo " Health check passed"
else
    echo " Health check failed"
    kill $APP_PID 2>/dev/null || true
    exit 1
fi

# Test API
RESULT=$(curl -s -X POST http://localhost:5009/api/add \
    -H "Content-Type: application/json" \
    -d '{"a": 5, "b": 3}' | \
    python -c "import sys, json; print(json.load(sys.stdin)['result'])" 2>/dev/null || echo "ERROR")

if [ "$RESULT" = "8.0" ] || [ "$RESULT" = "8" ]; then
    echo " Calculator API working"
else
    echo " API test failed"
fi

kill $APP_PID 2>/dev/null || true
echo " All tests completed"
