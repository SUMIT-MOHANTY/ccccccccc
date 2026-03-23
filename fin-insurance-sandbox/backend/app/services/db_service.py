import logging
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

def get_db_session():
    """
    Get database session with retry logic and error handling.
    Returns None on failure.
    """
    from app import db

    max_retries = 2
    retry_count = 0

    while retry_count < max_retries:
        try:
            session: Session = db.session
            # Test connection
            session.execute('SELECT 1')
            return session
        except SQLAlchemyError as e:
            retry_count += 1
            logger.error(f"Database connection failed (attempt {retry_count}): {str(e)}")
            if retry_count >= max_retries:
                return None
            # Brief sleep before retry
            import time
            time.sleep(0.5)

    return None
