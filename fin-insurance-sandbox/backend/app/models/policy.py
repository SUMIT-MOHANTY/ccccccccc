from app import db
from datetime import datetime

class Policy(db.Model):
    __tablename__ = 'policies'

    id = db.Column(db.Integer, primary_key=True)
    policy_number = db.Column(db.String(50), unique=True, nullable=False)
    holder_name = db.Column(db.String(100), nullable=False)
    premium = db.Column(db.Numeric(10, 2), nullable=False)
    coverage_amount = db.Column(db.Numeric(12, 2), nullable=False)
    status = db.Column(db.String(20), default='ACTIVE')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'policy_number': self.policy_number,
            'holder_name': self.holder_name,
            'premium': float(self.premium),
            'coverage_amount': float(self.coverage_amount),
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
