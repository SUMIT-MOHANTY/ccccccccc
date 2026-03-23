from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.exc import IntegrityError
from app.models import Base
from app import db

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, email, password_hash, active=True):
        self.email = email
        self.password_hash = password_hash
        self.active = active

    def save(self):
        """Save user with error handling for constraint violations"""
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError as e:
            db.session.rollback()
            if 'email' in str(e.orig):
                raise ValueError(f"Email {self.email} already exists")
            else:
                raise ValueError(f"Database constraint violation: {str(e.orig)}")
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Failed to save user: {str(e)}")

    def __repr__(self):
        return f'<User {self.email}>'
