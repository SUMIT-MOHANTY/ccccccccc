from flask import Flask, render_template, jsonify, request
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Health check endpoint
@app.route('/health')
def health():
    return jsonify({"status": "healthy", "port": os.getenv('PORT', 5000)})

# Calculator API endpoint
@app.route('/api/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        operation = data.get('operation')
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))

        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            return jsonify({"error": "Invalid operation"}), 400

        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                return jsonify({"error": "Division by zero"}), 400
            result = a / b

        return jsonify({"result": result})
    except Exception as e:
        logger.error(f"Calculation error: {e}")
        return jsonify({"error": str(e)}), 500

# Main UI route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
