set -e
echo " Testing calculator API..."
curl -s -X POST http://localhost:5000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation":"add","a":5,"b":3}' | python3 -m json.tool
