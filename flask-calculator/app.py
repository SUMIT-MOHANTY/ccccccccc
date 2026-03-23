"""
Minimal Flask backend for flask-calculator.
Provides /api/calculate endpoint with bulletproof error handling.
"""

from flask import Flask, request, jsonify
import json
import math

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    """Serve the calculator interface."""
    return app.send_static_file('../templates/index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    """
    Handle calculator API requests.

    Expected JSON body: {"a": number, "b": number, "op": operation}
    Returns: {"result": calculated_value} or {"error": "message"}
    """
    try:
        # Validate content type
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400

        data = request.get_json()
        if data is None:
            return jsonify({"error": "Invalid JSON"}), 400

        # Validate required fields
        if 'a' not in data or 'b' not in data or 'op' not in data:
            return jsonify({"error": "Missing required fields: a, b, op"}), 400

        # Extract and validate numbers
        try:
            a = float(data['a'])
            b = float(data['b'])
        except (ValueError, TypeError):
            return jsonify({"error": "Invalid number format"}), 400

        # Validate operations
        valid_ops = {'+', '-', '*', '/'}
        op = data['op']
        if op not in valid_ops:
            return jsonify({"error": "Invalid operation. Use: +, -, *, /"}), 400

        # Perform calculation
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                return jsonify({"error": "Division by zero"}), 400
            result = a / b

        # Handle NaN/Infinity
        if math.isnan(result) or math.isinf(result):
            return jsonify({"error": "Invalid calculation result"}), 400

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": "server error"}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
