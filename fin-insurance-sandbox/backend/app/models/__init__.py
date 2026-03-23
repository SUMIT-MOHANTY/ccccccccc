from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import models to register with SQLAlchemy
from .user import User
from .policy import Policy
