import pytest
from app import create_app, db
from app.models.policy import Policy

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_policies_empty(client):
    response = client.get('/api/policies/')
    assert response.status_code == 200
    assert response.json == []

def test_create_policy(client):
    data = {
        'policy_number': 'POL001',
        'holder_name': 'John Doe',
        'premium': 100.50,
        'coverage_amount': 100000.00
    }
    response = client.post('/api/policies/', json=data)
    assert response.status_code == 201
    assert response.json['policy_number'] == 'POL001'
