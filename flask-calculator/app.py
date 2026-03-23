from flask import Flask, request, jsonify
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'version': '1.0.0'})

# Calculator endpoint with validation
@app.route('/api/calculate/<operation>', methods=['POST'])
def calculate(operation):
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({'error': 'Invalid input: a and b required'}), 400

        a = float(data['a'])
        b = float(data['b'])

        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                return jsonify({'error': 'Division by zero'}), 400
            result = a / b
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        logger.info(f"Calculation: {a} {operation} {b} = {result}")
        return jsonify({'result': result})

    except ValueError as e:
        return jsonify({'error': 'Invalid number format'}), 400
    except Exception as e:
        logger.error(f"Calculation error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Graceful shutdown
@app.route('/shutdown', methods=['POST'])
def shutdown():
    os._exit(0)
    return jsonify({'message': 'Shutting down'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000), debug=False)
