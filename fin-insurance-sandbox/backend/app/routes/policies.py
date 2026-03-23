from flask import Blueprint, jsonify, request
from app.models.policy import Policy
from app import db

policies_bp = Blueprint('policies', __name__, url_prefix='/api/policies')

@policies_bp.route('/', methods=['GET'])
def get_policies():
    try:
        policies = Policy.query.all()
        return jsonify([policy.to_dict() for policy in policies]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@policies_bp.route('/', methods=['POST'])
def create_policy():
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ['policy_number', 'holder_name', 'premium', 'coverage_amount']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Create policy
        policy = Policy(
            policy_number=data['policy_number'],
            holder_name=data['holder_name'],
            premium=data['premium'],
            coverage_amount=data['coverage_amount']
        )

        db.session.add(policy)
        db.session.commit()

        return jsonify(policy.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
