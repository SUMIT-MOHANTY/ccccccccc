from flask import Flask, request, jsonify, render_template
import math
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

def safe_eval(expression):
    """Safely evaluate mathematical expression"""
    try:
        # Only allow numbers and basic operators
        allowed_chars = '0123456789+-*/(). '
        if not all(c in allowed_chars for c in expression):
            raise ValueError("Invalid characters")

        # Check for dangerous expressions
        dangerous = ['__', 'import', 'eval', 'exec']
        if any(d in expression for d in dangerous):
            raise ValueError("Invalid expression")

        result = eval(expression)
        return float(result)
    except Exception as e:
        logging.error(f"Calculation error: {str(e)}")
        raise ValueError(str(e))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression', '')

        if not expression.strip():
            return jsonify({'error': 'Empty expression'}), 400

        result = safe_eval(expression)
        return jsonify({'result': result, 'success': True})

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logging.error(f"Server error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
