import logging
from flask import jsonify

logger = logging.getLogger(__name__)

def register_error_handlers(app):
    """Register application-wide error handlers"""

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "not_found",
            "message": "The requested resource was not found"
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"Internal server error: {str(error)}")
        return jsonify({
            "error": "internal_server_error",
            "message": "An unexpected error occurred"
        }), 500

    @app.errorhandler(Exception)
    def handle_exception(error):
        logger.error(f"Unhandled exception: {str(error)}")
        return jsonify({
            "error": "server_error",
            "message": "An unexpected error occurred"
        }), 500
