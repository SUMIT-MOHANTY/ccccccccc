import requests
import sys

try:
    response = requests.get('http://localhost:5000', timeout=2)
    if response.status_code == 200:
        print("Health check passed")
        sys.exit(0)
    else:
        print(f"Health check failed: {response.status_code}")
        sys.exit(1)
except Exception as e:
    print(f"Health check failed: {e}")
    sys.exit(1)
