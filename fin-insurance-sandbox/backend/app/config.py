import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration class with environment variable validation"""

    @staticmethod
    def get_env_variable(name, default=None, required=False):
        """Safely get environment variable with error handling"""
        value = os.getenv(name, default)
        if required and not value:
            raise ValueError(f"Missing required environment variable: {name}")
        return value

    # Database
    DATABASE_URL = get_env_variable('DATABASE_URL', required=True)
    POSTGRES_USER = get_env_variable('POSTGRES_USER', 'username')
    POSTGRES_PASSWORD = get_env_variable('POSTGRES_PASSWORD', 'password')
    POSTGRES_DB = get_env_variable('POSTGRES_DB', 'fin_insurance_sandbox')

    # Flask
    SECRET_KEY = get_env_variable('SECRET_KEY', 'dev-key-change-in-production', required=True)
    FLASK_ENV = get_env_variable('FLASK_ENV', 'production')

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
