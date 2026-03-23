from flask import Flask, render_template, request, jsonify
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    """Render the calculator interface."""
    try:
        logger.info("Loading calculator interface")
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error rendering template: {str(e)}")
        return "Error loading calculator. Please check server logs.", 500

@app.route('/calculate', methods=['POST'])
def calculate():
    """Perform calculation based on input data."""
    try:
        data = request.get_json()
        if not data:
            logger.warning("No JSON data received")
            return jsonify({"error": "No input provided"}), 400

        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
        operation = data.get('operation', '+')

        logger.info(f"Calculating: {num1} {operation} {num2}")

        result = None
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return jsonify({"error": "Division by zero"}), 400
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})
    except ValueError as e:
        logger.error(f"Value error: {str(e)}")
        return jsonify({"error": "Invalid numbers provided"}), 400
    except Exception as e:
        logger.error(f"Calculation error: {str(e)}")
        return jsonify({"error": "Calculation failed"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

    logger.info(f"Starting Flask application on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
