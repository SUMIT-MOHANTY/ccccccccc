set -e
cd /workspace
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Running tests..."
python -m pytest -v --tb=short
