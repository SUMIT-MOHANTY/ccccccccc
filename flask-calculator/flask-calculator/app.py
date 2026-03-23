from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

def calculate(operation, a, b):
    """Perform calculation based on operation type."""
    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        raise ValueError("Invalid number format")

    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operation")

@app.route('/')
def index():
    """Serve the calculator interface."""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_endpoint():
    """API endpoint for calculations."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        operation = data.get('operation')
        a = data.get('a')
        b = data.get('b')

        if operation is None or a is None or b is None:
            return jsonify({'error': 'Missing required fields'}), 400

        result = calculate(operation, a, b)

        # Handle very large numbers
        if abs(result) > 1e308:
            return jsonify({'error': 'Result too large to display'}), 400

        return jsonify({'result': result})

    except ZeroDivisionError as e:
        return jsonify({'error': str(e)}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
