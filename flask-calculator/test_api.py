import json
import requests

base_url = "http://localhost:5000"

# Test addition
response = requests.post(f"{base_url}/add", json={"a": 5, "b": 3})
print(f"Add test: {response.json()}")

# Test division
response = requests.post(f"{base_url}/divide", json={"a": 10, "b": 2})
print(f"Divide test: {response.json()}")

print("API tests completed")
