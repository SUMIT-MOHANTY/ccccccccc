from flask import Flask, request, jsonify
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("flask_app.log")
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Flask Calculator API is running 🚀",
        "endpoints": {
            "health": "/health",
            "add": "/add",
            "subtract": "/subtract"
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify the app is running"""
    logger.info("Health check endpoint called")
    return jsonify({"status": "healthy"}), 200

@app.route('/add', methods=['POST'])
def add():
    """Addition endpoint"""
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            logger.warning("Invalid input: missing required fields")
            return jsonify({"error": "Missing required fields 'a' and 'b'"}), 400

        try:
            a = float(data['a'])
            b = float(data['b'])
        except (ValueError, TypeError):
            logger.warning("Invalid input: values must be numbers")
            return jsonify({"error": "Values must be numbers"}), 400

        result = a + b
        logger.info(f"Addition: {a} + {b} = {result}")
        return jsonify({"result": result})
    except Exception as e:
        logger.error(f"Unexpected error in add endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/subtract', methods=['POST'])
def subtract():
    """Subtraction endpoint"""
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            logger.warning("Invalid input: missing required fields")
            return jsonify({"error": "Missing required fields 'a' and 'b'"}), 400

        try:
            a = float(data['a'])
            b = float(data['b'])
        except (ValueError, TypeError):
            logger.warning("Invalid input: values must be numbers")
            return jsonify({"error": "Values must be numbers"}), 400

        result = a - b
        logger.info(f"Subtraction: {a} - {b} = {result}")
        return jsonify({"result": result})
    except Exception as e:
        logger.error(f"Unexpected error in subtract endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting Flask application on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)
