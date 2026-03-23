import logging
from flask import Blueprint, jsonify
from app.services.db_service import get_db_session

api_bp = Blueprint('api', __name__)
logger = logging.getLogger(__name__)

@api_bp.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint with database connectivity test"""
    try:
        session = get_db_session()
        if session:
            return jsonify({
                "status": "ok",
                "database": "connected"
            })
        else:
            return jsonify({
                "status": "degraded",
                "database": "disconnected"
            }), 503
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return jsonify({
            "error": "internal_error",
            "message": "Health check failed"
        }), 500

# Ensure error handlers are imported
from . import errors
